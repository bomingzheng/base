import locust.stats
from locust import TaskSet, HttpUser, task, between, tag
import os
locust.stats.CSV_STATS_INTERVAL_SEC = 3


class MyTaskCase(TaskSet):

    def on_start(self):
        pass

    @tag('任务')
    @task(12)
    def get_vip_time(self):
        url = '/channeldata/data/user/list'
        headers = {"Content-Type": "application/json"}
        data = {
                "channel_id": 1823,
                "vip_id": "1819",
                "start_time": "2021-04-19 22:38:34",
                "end_time": "2021-04-17 22:38:34",
                "client_id": 10002814,
                "nonce": "123456",
                "timestamp": 1583868236,
                "signaure": "ccdb633eca57bf4bd8c63c1060c3747f4212b53a"
            }
         with self.client.post(url, json=data, headers=headers, catch_response=True) as res:
            try:
                if (res.json()["error_code"] == 0 and isinstance(res.json()['data'], dict)) or\
                        (res.json()["error_code"] == 10007 and isinstance(res.json()['data'], list)):
                    res.success()

                else:
                    res.failure("code码获取错误")
            except AssertionError as e:
                print(res.text)
                res.failure("获取数据失败", e)


class UserRun(HttpUser):
    tasks = MyTaskCase  
    wait_time = between(1, 5) 
    host = 'http://testapi.cps24.dzods.cn'


if __name__ == '__main__':
    os.system("locust -f Locustfile.py")

