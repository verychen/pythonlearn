#!/usr/bin/env python3
import requests
import demjson
import string
import re

result = requests.get("http://data.gtimg.cn/flashdata/hushen/latest/daily/sz300104.js", params='maxage=43201')

lines = str.splitlines(result.text)

for line in lines:
	print(line)
	matchObj = re.match('(\d*)\s+(.*)\s+(.*)\s+(.*)\s+(.*)\s+.*',line)
	if matchObj:
		print('日期',matchObj.group(1),'最高价格',matchObj.group(4),'最低价格', matchObj.group(5))