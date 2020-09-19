"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: pytest.py
@time: 2020/9/14 19:03
@desc:
==============================
"""
import requests
import json


class Communal(object):
	def request(self, url, data, headers, method):
		try:
			if method.upper() == "POST":
				return requests.post(url, json=data, headers=headers)
			elif method.upper() == "GET":
				return requests.get(url, params=data, headers=headers)
			else:
				print("请求方法错误，请重试！")
		except Exception as e:
			raise e


if __name__ == '__main__':
	r = Communal().request(
		"http://api.bcex.cloud/api_market/placeOrder",
		{
			"market": "USDT", "token": "ETH", "market_type": "1", "type": "1", "price": "0.01", "amount": "2",
			"api_key": "c8863ec11ee3d908ae40fc98a98f4804", "sign": "qa"
		},
		{
			"Content-Type": "application/json"
		},
		"POST"
	)
	print(r.json())