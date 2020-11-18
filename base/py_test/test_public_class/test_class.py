"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: test_class.py
@time: 2020/10/26 16:31
@desc:
==============================
"""
import requests


class SendRequests(object):
	def rts(self, url, data, headers, method):
		try:
			if method.upper() == "POST":
				return requests.post(url, json=data, headers=headers)
			elif method.upper() == "GET":
				return requests.get(url, json=data, headers=headers)
			else:
				print("请求方法错误，请重试！")
		except Exception as e:
			raise e


if __name__ == '__main__':
	r = SendRequests().rts(
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
