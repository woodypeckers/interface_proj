#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import unittest
import requests
import json
import logging

from config import *

class WeatherTest(unittest.TestCase):
	u"""根据城市名获取天气预报"""
	base_url = r'http://v.juhe.cn/weather/index'

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_with_error_key(self):
		u'''使用错误的key值发送get请求'''
		r = requests.get(self.base_url)
		json_data = r.json()
		self.assertEqual(json_data['resultcode'], '101')
		self.assertEqual(json_data['error_code'], 10001)
		self.assertEqual(json_data['reason'], u'错误的请求KEY!')
		if json_data['error_code'] == 10001:
			logging.error("错误的请求KEY")

	def test_get_weather_by_cityname(self):
		u'''根据城市名获取天气预报的信息'''
		params={'key': KEY, 'cityname': '深圳'}
		print params
		r = requests.get(self.base_url, params=params)
		json_data = r.json()
		print json_data
		if json_data['error_code'] != 10001:
			logging.info("不是错误的请求KEY")
		


if __name__ == '__main__':
	unittest.main()