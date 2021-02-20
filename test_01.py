import hashlib
import json

import m3u8
import requests
import binascii as bns
from Crypto.Cipher import AES
import base64
from collections import Iterable

import multiprocessing

# m3u8_obj = m3u8.load("https://hls.videocc.net/d1977c4d68/7/d1977c4d68a4f3729a4ada015326b117_3.m3u8?pid=1611995044280X11180762&device=desktop")
# for seg in m3u8_obj.segments:
#     print(seg.uri)
# url = "https://ab-dts.videocc.net/d1977c4d68/51/1566886439000/e/2e/48/8e_3/d1977c4d68a28a816ce92f82a32e488e_3_1.ts?pid=1612418633823X1553681&device=desktop"
# a = requests.get(url=url, verify=False)
# print(a.content)
# for i in a.content:
#     zz.append(i)
# print(zz)

# print(multiprocessing.cpu_count())

def aa(t):
    w = []
    y = 0
    t_length = len(t)
    while y < t_length:
        r = ord(t[y:y+1])
        y += 1
        if 37 == r:
            w.append(int(t[y:2], 16))
            y += 2
        else:
            w.append(r)
    return w

# q = aa("7eabe3a1649ffa2b")

def niah(haystack, needle, path=None):
    if path is None:
        path = []
    if isinstance(haystack, dict):
        if needle in haystack:
            #print(path)
            path.append(needle)
            return(path)
        for k, v in haystack.items():
            result = niah(v, needle, path + [k])
            if result is not None:
                return result
    elif isinstance(haystack, list):
        for idx, v in enumerate(haystack):
            result = niah(v, needle, path + [idx])
            if result is not None:
                return result


# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/get", data=json.dumps(payload))
# pass
#
# keys = "0bad7e13e198025f778f4991fe894e9db048047ed8e15e49b48363d0e091f850"
#
# ky = b"7eabe3a1649ffa2b3ff8c02ebfd5659f"
#
# vid = "d1977c4d68ffb46a2f3be2011fbb629d_d"
# a = "94a12508d0fac5aeaf5da47e91992b3548cc044b3236ced2d57d8ca81db8f7836a5f7ab60e0817ec5a3160e46921b356f0daa93465ee68bd801c700d43c749f53930c77e3dd4a60347bbfce918bbe1147113ac997e33b832205d380540729c52bd40e8d4ce9d986dc5c1f522fdbe9562e7aaa0bd491389c58425ca56a5d1c6b4d90dc9fc25cc1e54cd1718d0d0137c5e323c59ccbfef26e85554d6f2f14c72686625c6e571235c76d657a772ac4de9421c88b813fe4aeebffc5768f10b57fedb7ec2e634fc1756aeee7b2824c6d51e8b1602c9d8aff8a5c1d7e00f031ea135f286d13ab7bb0fe31eab21e3c63f4435bb17dc16dcaf5d877684abb578a2a40db4e17909b44a3527c9440d576abee5b7d275585e424b351242a8c530ec52f6c2893eb73bcae6f022c38bb51ac831c42a61086644cb14b2d87984d14afbad71336182170754a8f5fe09ba552a835f0db373652b1e99e277230ddf24c4c66c28aa6d8c6531eb50484509866f62946df8491af5d50e7715849b3d556ff6c52fa648783683c8651723af6fd757951d35e5b1a69e27bfe85054c382e70b41794e71f85a826bfac3a8d88aa8703aeadd69996314a36892dcd3cf077a80608c32396b401e41bed6e91da27ba5d59716277c2fd3e91113dab83c988e06f16ed41ddf9e10246affc8197be3ac2eb069e0aea07a4e662e6ed5fdc66db087d68edf92394cef6452fba41c4233550d554e3b0a4ed268f5ca556a6e0ca16086c60901b9fbd952bac6b8a9d2a803e0f7e6825d640df2e036e258914c62fac60d716d8b62b06a903e7d5184ebf83615a0fc2b6852da854fa473a4e3894a0a6481c4c1961afc8f698e37d08090c267dce8e30cbdeadb95dd063be84dd54e4a355782119e49b63df0b911aa3b86a397d66198a64bcbc9c63c176f9f1309f4cb892db8f370107a00a09c55f13f3a5378c0826c1c6b7c276630d0bff586e125ad5b765f211f4ec4882e861fbd40b031e878b33a1d7e659da6965be12760cec8454d6b2d239137d17787a07a7481fab21330299c391865246239acf4f78e6b2d18553e12ee18788cc005c9f9c08df53ba033acac3a80b661e8cc2db200199f6efad90dee93d1836ee7fe123523ee9190af53f2e2d1b095b3ff1f1f98924e87ecd36289a2ca5236c002350bc854c6edea09384f60aedf53183b5627cfd139064dbe494dde235a42ea86e3ac3f495f435d9b6f2d7159b0c9d1c3a3ef4a0aeb8024669670d01a3dc36d0ea23e0d6a8d458d62389dd173fe20e342655fdf4c9baf98e2b88df0c45ddc4c13ed4c9bfac374f1e8887c8faf53966b34c566478f2dfccd49e5b13b2eddfea9449e41eb61159310e8ead52fd92cd7e40b8d5af610043bbcb47b185430521dfc7811601e3fc66d50b3f16cefd3f4c511b945e1d2ef7a53b630f87a1d4651251270744e880ad97179fae67b1d451f2c6d5fb63b641f036490e3cf94f5e9b793c9937a930f5317fde8bab1d32f8ef3d50d2d84648e50a708ed46bb71080a332c1ea95317dffdd19270871cb2c4acd2e6932e3080b1dafcf5657a698cca5abea42bfb87d125fa85baf915d4c7e1a3836e9666e6932b68946b9eda6207acdbac448710135491d175bc183b3bc89b78bf71cda21738712c538d51eef0428a6a97be8bcc5d7321e852117a5023adb269816ec5387758566d2ce05e99441469e7db1c13ee06d1a734c0c119c5842c531832db25898016183241b73cc3454732813084a900a37299da2b43fc30873fc9cf6e166f384b1ccdc1e677a648ade81192936c9911c41efeaec6e42041902fb1b225e7b220457f63299e589a281f3b3ec29d7a81b10d85fdcd98163a8431f080b6933bf0e2cc630498abbfdeda0dc3001b0b4f191f579bf475378d85129205208836d5aaf3d9b307acd1b79aa3cbf5b151a3d9ee8fa944491ab29ab8c673a3729c1dc34ff0889c87f91b70f6c63035d174cf47ea57ea50a67057c4a2313f97fc40bebf9435470c1e2e37656e5f7fe2ada45f4e75b8e6f67da671cc8a561e95cc9b1034a077110e96a897ae82b2d872ee33341cb8bc85e2d4880a40dd83e79ea04b0ad51932a558da679ad87cc4def944826eebe87e4e43c967ea4ea7edc649df96c6af0cdc5aa72a42b513162864b95cdb9a0efa0b5b0bff56d61937f0de317b7887d7d408317d3b70d4d156b7535999bbe3dea44f17eae5650d77a51114cb953fc7fb1c9e5d3144ecf4d476acb84d83c715a786a97ef6a356f7efa3a9aac1e9576c35d963d770bb05cceec46a3b5a2947cd3ac385941391a57c5f4a316108d63e42a4e437d77daaeb5f8f66418d75bdda9d3eb3d8f282409614ebaccee31c4c72fbf9dd87301ffc1d63e6241326c28f1f2d674c8631dfc82d9940c0e209aa93d873b70cf0a7f96feb5b5e7ba82404d58a48f71712203a1c9e9cf6d02b0edddc3aa2fb6de1e7650e5b7fd27b64fe9304b87c377df0c2a6d585f4e5a53058f646d28f5faf1e267900b0c5ae246fef0f0dc1aae1a88dfb5aaffcc0ea29dd6d11993853385fa44c76985c3b2b65bf9389f7f7fde010a479345181160aba1802eab3e25d400202729716c64ee12f5cf74d81260d85fb03f91ded0549b3e1046736eb9841ae3d84df94b50abad8c2f9ff46e10fca63e34b878441d348d45339da9d79e5f41efd40cb4e0b837f7e3ac512c7cf9f700970a1ed9ac27a38b7843dabf0504499b07e2a6c0c1960737b88937c0e0e60177abfd81c0d0cfca00059cb61b4a3f1a2b62982c237299cc9b46d2586b76e4f0a99bdab3b8268543af5e0b81ade965773c2bfac698be3d1a21ea4071d0d90e629f3defdffa01b2baac35ed6b097469fcbbb7f7c31a8859ca14bde855ca65d7db2da20567160ea4fe1878285fc393e26c418a23cd50cb7b9ce0ecfcad2e48fd97180544578fb0de019bfbed4c2c82ced7963b87c131ad9c3478a239b95726800f3ab3f0bd8bcf0016bfc69ebdaddd56821de53732504f1eddf8721abe34f3feb59cf47d12ca3eede4da04e90448f73d5cfd4f35cf9482e6980f6f2101087ae4c3c377b3d94f06df57da670e881b5ba3b839bbb3b023465efa9693dceefc9c8deb12250da358a690b1c41bbb85c98f2cb2feaa3c626dabf3e2a98497fa0ce56d057a4345c54ecaa8042420f700b3c0c2c6b6c632bc3c170696f9559b286982af394b280bd482ad20f41414d618f9a30a32ea40110aced327af9efc21f2908f6c54d09d511b9d7f7fd5c352fc7df1adb81a05f54a595eff635dd58d31c3a91bf35b7791b74df1662716eeddaeba4c2abb21d07384d746c9dbecb45d8c1223c0e376b5e23fca495e969dcdcbb759709ab8e3b0b3e604a70483d64c2c86fdb8f1c5795cfa56ee192d3eb6ae6db19552bcc4dd5f557f8d0d8a3954f380c23489e634400d105b7ebc13bc74c322cbfd98804a4bd809153e1e12d8c956215c21215fb4cf3dfe9617773f653556d79cc01ec69ad7d953691cfbdef79ae939486a210999b1fe6bcaaadd2cc1b193c540fca7659768fb1c284e7472b469d40f4a0c2b58daa5f8fd68be1288013d94ab8638ff211d0e5cefe95d67bf0395523b3538b5b36ae0882f9f1f4702383c64bd476cfac74ccd2b5508e1b74e3217887e2700c329c95482c71f8b08930f18074b57909407015b39d4345cb5fbceded38c6b2c50774bb914c01317b47e4730bd103729bd36a2e9f1fbb0b4e5c0df5bdd354c57a703d206a79c50871f9efc53eb18e50d06a4310716b93bfcc60475aac6a28c3ce5e7df8ed3b9f04f42bc343a2772d861f73e3e109286f5848ba2abb24d0bba9b90fba647ed90cd47881924985346a653993bd3ad5795c58c8691bba72ff9c4ead4183c412ad5c01dc9689b457bc724417e6d241ae0b8889a9f14f674297ea3faad7d904982ca40e8f98d6f02665f0ea56ce9b53617a2903d0125e70707b98bd256906db92765187d8700f55daa0b67e569e9b618cef7b665281b66a290d86ede40e78a3bc7b012b6851628fc7f31a7f3d50653d8ce74e8fa076fcad3a717e58e0fbaceb990184c5e9b1d8794f2ee3751f5228d2df2869ebdcd44f6487551b8757b59f0916670cdb5d460d94fb3c4ab6a31710ad8cfe5f11f8e59cf5a2a31576a170ecbb4bb23b633377b34b0ba2213b3d40dc562d2262af749efa29d14e509c6a2700bccb778ebcf29247d933fd1b078de193fa46c5e84ee50044f79353b433adeef62b064e67fa5099236c5838a23cc64234383fe461fba71ab18e23ff38640bc01b75e7b84664a9d965767be51e2f2446f7695799e2f87a392c3cc1bdb45f3d697084284c240de9a4b0d94568928a1a8db0a13a49f31f40dc6e2dab20678155f3e1f7e74fcb6c93481ad15b7e2a0af13e213ac32ce7afbac9bd44f93f81f605b50e9e385b596dcb7e50eb70b2923e8298c1232e6b57015c4dcd134a30ee3ae3ff754e8058815a0e22d077a2db28fb1af3c039599a74401f50f8fdcc68cc0077ca7ad60fc1c89a1206477a13895dee10325b16bef5baf9cb1ea8d90d977611945297f6e130afc36b34c3efd59a4b4415e6f36d5bf4adfbeed2cbcd1769e4cf102f070bd44d9ccb7036381f896fa59c263013dbd2fcb72663795906768b4c4ccddf7a1ef8a37c7a604e43513bf02755f6d7aa8892277b550b4522f88eeef3ed355d8a3ab2c6a1e0463f8331dc4eca00f308bd5a99048e55bc6239c8ba582ad52b0c140cd5e94227d9c60d40e7daac87edbf13e66898151a442e13fa9b2d0d6a2592539cbf662ff922e7288d7e21aef7eccdb87e310de480757da6fbef28686846a25359780d9c9f353e5186c3202ed78d078bbac0bfa5488f44eb6a475edc6780aaad1ab235ee0de58e8562bd29cb5403a9dd2eee22afb3ea9405131fa7b385da361841e7a0617ece6d9457b9b1601ae65d7e58df3662e3c92903fdf0648034206c67d3d2165bdcb1f0a1a6d09834c56bca2e935e55407e450e4ae4951dfa761853b68c5bfa4c3fb677df7a46d0fc80b89d1a18b3ceeb59687cc086a9dc868e4430c6c6a4c5666e8837acd2e9f13ed005c85711e2c760899a716d687f9e71f0f88b880a5246b517da724eb907662e23343aaf2371d1a6b783eddf9f0cb0db37bf0acf1b261298a80ae442e2546f2c9cc4b1a96b5c7f455154080e27e5a5771d30a47b91dc6bb23ae52bdbcc253c8dec3eb6d023639caebca6e46c384c0ea379aca7606bc18812a52cd95c9d0027c560e54cd0b0339c819d58efd1efc55910f5670d13f4bc2e5829653c3357fbbf547856e8238968f411ae31dce580e4c6993c7a46db89398a0904e2d05e4eaf77162e4276e6252f1f0dbcb39bf49301dedfdf5a7dca02eb1064ddf4fb4c2cd4f3e7e21302663f4ffcdfecf1ddb03b5d62303633dc2498d6b5582fd0a73d3664661bf7ef5acfa8232ffa8756822162eee1ef67199c345034a95cb6b7a3606687af1592457e87c6cdb83ef80665708eea01b2154bf991e97e48f639be5abfeef3641500be553fc5b5f901543e9e0db119a4384155e0baffbb030ec8248f815c1bbcf521950b7dc87f68d2cd592ce7eafd103fc90a6fc4299ece159bcbbb1568b2172035c4f82a91c55b6d99a3881a7a56d438b6aa48db7a894af8fb18f0501e7e52baae876ea7a4324e9362059c9cb3370683b42e02a7d67573450a848b852473fa1b376b480db90eb66a1f7cf05644584e29b384cb2ce90e43294acda26b71eac935a173e7269fb2cb4126bfdeea6b7cd202d870ee7afc0581b85e0ae055327158c62f003a3d5c3b8e7596a87b68c649ab9d2db7e2b407114cf9cd4a11c1c5b4c8a679c56b5468510600737d40971d3fa8fc7ce4419b3db34631a9c2e4d4522b3c25c33b0c2df18d8d5c25cfdb34b66675fa9e8514f2da146dae0024390bdda5b9a4a046d952983ad35fb1ede2e0b44d0badb1c9f76a9be0d5e7f0e98e0d3543cd9672b3d982e458a51908029ae10a01827add14d5504823cdea151eb98ad8d6b3ace5753bc6555a86f9c3c781626e9283a39bb7d0b5975dbf827532e86931a25c7aac4d772210f334306bf4dbab50a8e3c33bae733d06e5617abf1a5d97b092f68455389a460e8e6f140d665da9e6740e8c755580ae60c9c1aaed80d3711eb5a1ee5e7bfd240920cc640cde6ebaa41dba02a5b142aedbf835a8ed128692e99efbd3195d0d6d60a109653219058c73e64eb6ed6424a9664a4fa18ca9b5c0b1822af6c59ad700b82174ada7a6b78987f8867c3b0ff9a8d572120435cb0b466cbf28d1254d1e6048bde9af236d84cd29e14125671699d796014ec745b0b65a1e3905238cbf2ab40a59e2c79302c1f8cc057aafeaa9533f6ee0e431ccd0ff7b53d2b4b29bc297d143441076fb7c144a4fcfa5b8ba9e7d25190e7123893ea91c17de2fbd7bfc59d8d0d1a1c04f53fc6a5ed4f7902e7a965f21b51ae7343662f37725ed84c49d6e7931a71768499cb9dad205de11d31e9cf4186b78b089abc1250bf212a0d7d5233c95914113799e9e7c286932d7229fb8c7cabd6308186a6600d892fa2d51e747f61ecbe987ea92aea99c00bc23f4a16df9caae6cf3e8cca11b4f691fb5cb265ec2cef95e689fb5e145e4e81cfe93729c23bf3ce0cd69ffc1a9ece4758045f0ee569aaf76bd4934278ca81dea5147f8935cd7d3c90bfc2084ee341e6456c8a7592ceda342cba1772844750d305228fa1bedfed640f5dc210f227f94b56e0846eb4bb47104d9158958bfb33e6e7389454c424ba8aeca21b28742386f037001952ded0aa6dbca49eb4e208b64a8f466d4c80cf671d01ae7fe6b12368632f5e1981355aced0bb78e1aa39485b7917829921f7a2d1d0236992af67fe24d38c3cd67e08b53d88f5f444bf1074ee05bb416129d4c9d6590dbd892c5328f088184a12fbbd889231df703e2dce3ea63dacbcde1616a9b2e5bb24c5d93f772b1a7f513966c889df13e277506f64dca0b4b47e68c3136d26d24aecafd997f4abc913d9d8700e9e51dea94b89a76e1b50975cbba771d3d524c3602ab58e414b4a77f0f5dfd7eb0eec2cb9e9f7eef3e371c3280a321ed8d2bbe9623d87f825de6675a1880d4943aa85fc1b4fcbf763bc682a171977e80c842631421e4d577ce307c1a23483d7d06d86e394f45658efe50da9bcee551ed0d4c43cc1f4d74a981cc9dbf540e861d273550f9023bb9ef60cba0c985d45dd9bd22ba2d457710c67e11a09558a816969d8467e24c63c78d4c7162bceaa59589c0f921d0f2de5b009d4a90dcec632daba16b6cd33c36beafa7f6858bcf7f2a4de0d00af4472f5e15e07361cd4bf7d36824b78b728bf6824a75492a559fee80c6d369f6b065bdcba2fc11bf908dada50173275659f0d8500b05aa4cffc938bc23a7b1205fc1ba6ef224671591ca13cf9a2cc1c687a67c36a30a2104042c6019ddfb3e419710d1a0d63703c6209e42e5168ef9bbd9423ea685f7a82bb92181935b61d8d343a9111f6b26aedeb76aa5080d2ee08c8746ce08368bc986280083339a41cd54a302dc221024b11c881700702a173888a55077bc989939dc15f03e34a549c3d3966e3a05cb15625a55c297cb59476426f6d40f5959a8e827789b07852a977ee2e3de8b05d73151ed77ab7a844dc2d09698cdec44e17ff369f6e6220d9a0928a17599e8054e763129456380f6fec4b6be6ee895d078eeed371c649e84ad0262d9ea58cc7e77de5d5ae7db35f9bb55f5844befd2dd0460dee9954b7b71f34f688092cf97a503e1276a4052a59a7d1dcf3f430104f1e01e92567330a37dc02249959640b1232d7df3d4765477bf6260c9c2e501d315ca0a8a282e891635aadba9793a3a039970495fe7233e9b7a03e4b67488521b44357b885c227b8a9b8b535bba0dbd04095509f67aae0e870539a289188fa48be4ec6baf301cc011346ba7f60cba48cfec7be0224c23557d8a95c91f4def29ebc43d030fcad255dc3924050728ba9d61cae69d729a9afc47374ecd07fb04ec433b6d7ed53aa1219e5f6e2b94e43e26c8684aac0ebbbdb4cd19716da67b618a0e4eeb20796d91cde926266bab4a4a6fa2e33132cf3fe12d9488a192633cc971d2e2d933826643ccd22f0eb7f0e7975269a336105e83dc66a9551da47ed8378f7b5f72004d371a1c3bf5cc6722c19f43e9ddf1d36794e4292acaaaf2a7938d6b4fa3839cb6777cf2e6f2005dfd44f747e90c4b5dd335145cb294873fa48e40303f67ee1ae48e3e9818fa66bacff9aad9e8a92ffa9aac014a9e29141071b8db30dbb18de8db66feecd32b53dab562f2faedb847a87e7c5aeab48f2b7616fac33942f38635a98064e7a183b7965c62e1f55a9e92813f816611c6a061bbed6963a093ab13b176b3fec4b7d2d215b5a1b0bbdaeb1c9bc7abaf194ea8f61c095fbb0cf3ab618cf5237246f52a07cda2541463b0c086afea3b35e545af9037616dc9e6c33933e2d4fef7332b822aca6f9b78abcea1cfb8d27b07cf8ab4b506d795499e760e0d0d5ea4404afebe171f214feaf2c4c23aae3447fa024c1839117f8cdf062a51cf6528fd32c0308b577cf90526d205eef91d64d9bd01f1e356f56eab20175259a0249ca28ca97007487147ded1bae08432f95b9b4f415e8d36ba989a8f5476faa2964f75d3a9062b4b98bbf13e2f7059fc9df70db26ab41bd7c25490cec08889493bf16065762655c3be7668d3052b40dc557f5be719e46f3a0fd83be20dcc9fc876f648ca17c2616403ae5ffcea4fc4ffcd579b51ecba54fe8a9de1563e939a587452150f5f06284ff123761d7b65fa212015f5e8e21f2ea2458e14c27455f61dcdf2331a894b30c917e9feaa3068c476f09f5f3d01493820ff3665e3ff7f72befe49c86a80c54e411d632e38893ba3672d7c46bb9e5485f636ed6f26abd61fba720e6dcf79af8601fd957f90d1d397775e03f5d845c84655594cf8b2005b054bf3256acadb654e67cb1e1a47bdf4a0459110b739228cd038c4b73a5b971914ab0eb6fd2cf5dd410372bcef01b7a1cbc4df4fab9856bd2bff8215f79c7a2ba6628fba51b82dbdd25afc354affb65d972ce4d459add19e2155a58bc214aabcf04ab2e713b9ac52c82b203be3aa142cc3e565aff95b2b351c5c2c54ba8dbeb3f95391fae624e30ef897fb43150cce8e61e458bffacea1b0c5de9f72e84907e8ea9356079994c08accf2f7061dd3ba9f5f810ce3bdef6e1ee4ad95203cd3933ce565e0481be1f690310adceae096ae51a152e449f9617523fbd8adc3cbed5737d77372257333a78fd099db62e04e79cafa5da86e087cecb4fc65848c9f998f211d10f65dc468dae1061fd5d416f1e5edf862ddb42f5c19310e9c2287eb57567a64314bddd7a74c21264532ef73c6eee002f4d6f3522fe5c5734ef7ad3c160a098643260f6d4e079fba09be4dd57709205cf337699183dc4bcaa791826b87eccaf7cf2ec9bc238b6052c3d1ea503e5172f52fe74548e16030c772d642795bf7164134838b1e1c5a2757350426a39609659cb770a36154441c8c82512c89636e1ffc6eef0e8d6eb65107290de30ddfd2622a212b2193e628d250ae201344d44e87a39f953a22454cc171f61eb6fb1e0efbbee00ac05131a69c5b191b4586eb80f07dc6165192d358672af065570d3d8aaae65cf81c7fcc6c3d6fc565d2a3e9c3aada9c7358d5738227209167c2fd511ba6181d7da644d42fbb2b6f19c294947f28d24b29c7bd64ce795b7ccc97cc18a194ef524f40a3a366f24ce3aa6a8d0f04ee7a7e870b33f16b15ba9fb2f216f318678491badb2a211e36b08145970f0fa99b181d4afcca2d0d54371c210f1d5210fda63603bf4325230054b730acabaccf92f16cc4d279fdb06e4f53c9db90f359b974d6dcfc6a1446184c3c03a4fe6c0ea97e6a202e5b4516a433dbdfb4582b9671598febc4e3e58893acb97ae9c6e1d5c56514b32c3b597aedd77976bf85e30682b628ebda4c94247d18e1f9a8bfba9999d3d26d598fd3256db196b87472683a397cdc0039cef6f2f3c9dfbf1df7b3000f5c68141276cfd795cf944b782497982b3b8cade5e878a7e994ede96f030401b4c46646afa3b845c8c140350d789c0802f0b169c2b4d697f8ea75a88f93491ac4106acc893c1de1c22883f7ebfeaf2fad8278a760080290147e5509acabf98b5eb4711ab29ba9de4ce7bf4c26cf765373f56be5bf8413adf2362c3983b7316c3d9efd71ee9fbe5fdf86506a7f87335da14604d436f0067a6e726d0e6fd550082f7c92"
# # md5_str = hashlib.md5(vid.encode()).hexdigest().encode()
# # key, iv = md5_str[:16], md5_str[16:]
# key = ky[:16]
# iv = bytes(list(map(lambda x:int(x/2), [2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 14, 10, 6, 4, 2])))
# aes = AES.new(key, AES.MODE_CBC, iv)
# t = []
# text = aes.decrypt(bns.unhexlify(keys))
# print(base_text)
# asa = list(text)

import shlex, subprocess

command_line = input()
args = shlex.split(command_line)
p = subprocess.Popen(args)
print(p)
