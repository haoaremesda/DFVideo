from scrapy import cmdline

# 或者['scrapy', 'crawl', 'jobbole']
cmdline.execute('scrapy crawl DfVideoSpider'.split())

# 直接存入为csv文件
# cmdline.execute('scrapy crawl baidu -o baidu.csv'.split())