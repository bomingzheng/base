"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: locustfile.py
@time: 2020/11/4 16:45
@desc:
==============================
"""

import requests

headers = {"Content-Type": "application/json"}
def post_vip():
    url = "http://192.168.0.251:8190/cpsconsume/portal/1300"
    data = {
        "user_id": 110000002,
        "book_id": 123,
        "day": 1,
        "hour": 0,
        "vip_starttime": 1604568837,
        "channel_vip_starttime": 1604567737,
        "dd": 0,
        "type": 4,
        "way_type": 0}

    res = requests.post(url=url, json=data, headers=headers)
    print(res.json())


def get_vip_time():
    url = "http://192.168.0.251:8190/cpsconsume/portal/1305"
    data = {"user_id": 110000002, "dd": 0, "book_id": 123}
    res = requests.post(url, json=data, headers=headers)
    print(res.json())


post_vip()
get_vip_time()



