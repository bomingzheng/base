"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: load_test.py
@time: 2020/11/5 11:15
@desc:
==============================
"""
import random
from locust import TaskSet, HttpUser, task, SequentialTaskSet, between, constant
import os
# 定义一个任务类，类继承TaskSet或者SequentialTaskSet
# 当类里面的任务请求有先后顺序时，继承SequentialTaskSet类， 没有先后顺序，可以使用继承TaskSet类


class MyTaskCase(TaskSet):
    # 初始化方法，相当于 setup
    def on_start(self):
        pass
    # @task python中的装饰器，告诉下面的方法是一个任务，任务就可以是一个接口请求，
    # 这个装饰器和下面的方法被复制多次，改动一下，就能写出多个接口
    # 装饰器后面带上(数字)代表在所有任务中，执行比例权重
    # 要用这个装饰器，需要头部引入 从locust中，引入task

    @task
    def get_vip_time(self):   # 一个方法,方法名称可以自己改
        url = '/cpsconsume/portal/1203'   # 接口请求的URL地址
        # 定义请求头为类变量，这样其他任务也可以调用该变量
        self.headers = {"Content-Type": "application/json"}
        data = {"user_id": 110000123}  # post请求的 请求体
        # 使用self.client发起请求，catch_response 值为True 允许为失败 ， name（可选参数）设置任务标签名称
        rsp = self.client.post(url, json=data, headers=self.headers)
        try:
            assert "万古书屋" == rsp.json()["data"][0]["chapter_name"]
        except AssertionError as e:
            print(e)
            raise

    # @task  # 装饰器，说明下面是一个任务
    # def login_(self):
    #     url = '/erp/loginIn'  # 接口请求的URL地址
    #     data = {"name": self.user, "pwd": self.pwd}
    #     rsp = self.client.post(url, json=data, headers=self.headers,
    #                            catch_response=True)  # 使用self.client发起请求，请求的方法 选择post
    #     self.token = rsp.json()['token']    # 提取响应json 中的信息，定义为 类变量
    #     if rsp.status_code == 200 and rsp.json()['code'] == "200":
    #         rsp.success()
    #     else:
    #         rsp.failure('login_ 接口失败！')
    #
    # @task  # 装饰器，说明下面是一个任务
    # def getuser_(self):
    #     url = '/erp/user'  # 接口请求的URL地址
    #     headers = {"Token": self.token}  # 引用上一个任务的 类变量值   实现参数关联
    #     rsp = self.client.get(url, headers=headers, catch_response=True)  # 使用self.client发起请求，请求的方法 选择 get
    #     if rsp.status_code == 200:
    #         rsp.success()
    #     else:
    #         rsp.failure('getuser_ 接口失败！')

    # 结束方法， 相当于teardown
    def on_stop(self):
        pass

# 定义一个运行类 继承HttUser类， 所以要从locust中引入 HttpUser类


class UserRun(HttpUser):
    tasks = [MyTaskCase]  # 定义固定的 task_set  指定前面的任务类名称
    wait_time = between(0, 5)  # 设置运行过程中间隔时间 需要从locust中 引入 between
    stop_timeout = 0.05


if __name__ == '__main__':
    os.system(

        "locust -f load_test.py --host=http://192.168.0.251:8188 --headless -u 100 -r 10  -t 5m"
    )

