import binascii
import json
import os
import random
import re
import time

import scrapy
from Crypto.Cipher import AES
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..PrpCrypt import PrpCrypt
from ..items import DfvideoItem
import base64
from hashlib import md5
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class DfvideospiderSpider(CrawlSpider):
    name = 'DfVideoSpider'
    # allowed_domains = ['www.luffycity.com']
    start_urls = ['https://api.luffycity.com/api/v1/course/free/127/sections/?courseType=free&id=127']

    custom_settings = {
        'CONCURRENT_ITEMS': 60,  # 设定同时处理的结果个数
        'CONCURRENT_REQUESTS': 30,  # 设置同时处理的请求个数
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10    #并发请求的个数
    }

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse
        )

    def parse(self, response, **kwargs):
        item = DfvideoItem()
        sections_data = response.json()
        for i in sections_data["data"]["chapters"]:
            dirs = "../bb/" + i["name"] + "/"
            info = {"chapters_name": i["name"], "dirs": dirs}
            if not os.path.exists(dirs): os.makedirs(dirs)
            for s in i["sections"]:
                info["order"] = s["order"]
                yield scrapy.Request(url=f"https://api.luffycity.com/api/v1/play/{s['id']}/?play_id={s['id']}", callback=self.auth_info, meta=info)

    def auth_info(self, response):
        auth_info_data = response.json()
        t = {"chapters_name": response.meta["chapters_name"], "order": response.meta["order"], "dirs": response.meta["dirs"], "name": auth_info_data["data"]["name"], "auth_info": auth_info_data["data"]["auth_info"]}
        yield scrapy.Request(
            url=f"https://player.polyv.net/secure/{t['auth_info']['vid']}.json",
            callback=self.secure_json,
            meta=t
        )

    def secure_json(self, response):
        secure_data = response.json()["body"]
        data = self.decrypt_data(response.meta["auth_info"]["vid"], secure_data)
        pid = str(round(time.time()*1e3)) + "X" + str(random.randint(1e7, 2e7-1))
        token = {"seed_const": data['seed_const'],"token": response.meta["auth_info"]["token"], "name": response.meta["name"], "chapters_name": response.meta["chapters_name"], "dirs": response.meta["dirs"], "order": response.meta["order"]}
        yield scrapy.Request(
            url=f"{data['hls'][-1:][0]}?pid={pid}&device=desktop",
            callback=self.parse_secure,
            meta=token
        )

    def parse_secure(self, response):
        KEY_URL = re.findall(r'URI="(.*?)"', response.text)[0]
        R = KEY_URL.index("/", 9)
        start_url = KEY_URL[:R+1]
        end_url = KEY_URL[R:]
        keys_url = start_url + "playsafe" + end_url + "?token=" + response.meta["token"]
        used_key_data = requests.get(url=keys_url, headers=self.settings.getdict("DEFAULT_REQUEST_HEADERS"), verify=False).content
        ky = md5(str(response.meta["seed_const"]).encode()).hexdigest()
        used_key = ky[:16].encode()
        used_iv = b'\x01\x02\x03\x05\x07\x0b\r\x11\x13\x17\x1d\x07\x05\x03\x02\x01'
        aes = AES.new(used_key, AES.MODE_CBC, used_iv)
        key = aes.decrypt(used_key_data)[:16]
        iv = binascii.unhexlify(re.findall(r'IV=(.*?)\n', response.text)[0][2:])
        aes = AES.new(key, AES.MODE_CBC, iv)
        ts_url_list = set(re.findall(r'#EXTINF:\d+.\d+,\n(.*?)\n', response.text))
        mp4_path = response.meta["dirs"] + str(response.meta["order"]) + "." + response.meta["name"] + ".mp4"
        with open(mp4_path, mode='ab') as f:
            for i in ts_url_list:
                re_content = requests.get(url=i, headers=self.settings.getdict("DEFAULT_REQUEST_HEADERS"), verify=False).content
                # while len(re_content) % 16 != 0:
                #     re_content += b"0"
                f.write(aes.decrypt(re_content))
                yield None

    def decrypt_data(self, vid, text):
        keys_obj = md5(str(vid).encode()).hexdigest()
        key, iv = keys_obj[0:16], keys_obj[16:32]
        aes = PrpCrypt(key, iv)
        decrypt_byte = aes.decrypt(text)
        decrypt_text = base64.b64decode(decrypt_byte).decode()
        result = json.loads(decrypt_text)
        return result