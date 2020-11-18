"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: locustfile.py
@time: 2020/9/14 19:03
@desc:
==============================
"""
import unittest
import requests
import pytest
from py_test.test_public_class.test_class import SendRequests
from py_test.test_tools.read_jaon import read_json
from parameterized import parameterized


def read_json_file():
    ad = read_json()
    arr = []
    for i in ad.values():
        arr.append((i.get("url"), i.get("data"), i.get("headers"), i.get("method")))
    return arr


class TestCase:

    # @parameterized.expand(read_json_file())
    @pytest.mark.parametrize("url, data, headers, method", read_json_file())
    def test_1(self, url, data, headers, method):
        r = requests.post(url, data, headers)
        print(r.json())


if __name__ == '__main__':
    # unittest.main()
    pytest.main(["--html=rest.html --self-contained-html"])
