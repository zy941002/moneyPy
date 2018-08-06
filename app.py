#!/usr/bin/env python
#coding=utf-8

import json
import urllib2

VALUATION = "https://danjuanapp.com/djapi/fund/estimate-nav/%s"
FUND_LIST = [
    ("040008", "华安策略混合优选"),
    ("160222", "国泰国证食品饮料"),
    ("161229", "国投瑞银中国价值发现股票"),
    ("005520", "国投瑞银创新医疗"),
    ("003243", "摩根灵活配置")
]


def get(url):
    # 模拟浏览器用户标识
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(url = url,headers = headers)
    return urllib2.urlopen(req).read()

def beauty_print(data):
    if data[1] > 0:
        print('%s\t| +%.2f%%' % data)
    else:
        print('%s\t| %.2f%%' % data)

valuation_url = VALUATION
for fund in FUND_LIST:
    res = json.loads(get(valuation_url % (fund[0])))
    if res['result_code'] == 600001:
        print fund[1], res['message']
        break;
    if len(res['data']['items']) == 0:
        print fund[1], u'暂无更新'
    elif len(res['data']['items']) > 0 :
        percent = res['data']['items'][-1]['percentage']
        beauty_print((fund[1], percent))