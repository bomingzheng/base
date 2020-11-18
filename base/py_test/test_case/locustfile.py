"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: one.py
@time: 2020/9/14 19:03
@desc:
==============================
"""
import pytest
import requests
import time
from locust import HttpUser, task, between, TaskSet



class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


if __name__ == '__main__':
    import os
    os.system("locust -f D:/git_hub/base/base/py_test/test_case/locustfile.py --host= http://www.baidu.com")