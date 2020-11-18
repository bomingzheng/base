"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: read_jaon.py
@time: 2020/10/26 17:23
@desc:
==============================
"""
import json


def read_json():
	json_path = r"D:\git_hub\base\base\py_test\test_data\data_params.json"
	with open(json_path, "r") as f:
		json_data = json.load(f)
		return json_data


print(type(read_json()))