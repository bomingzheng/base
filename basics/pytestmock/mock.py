"""
==============================
    @author: bmz
    @contact: bomz@dianzhong.com
    @software: PyCharm
    @file: Public.py
    @time: 2021/5/21 20:15
    @desc:
    @Site : 
    @Version:  2.0
==============================
"""


class Mock():
    def weather(self):
        """
        天气接口
        返回数据：{'result': "雪", 'status': '下雪了！'}
        """
        pass

    def weather_result(self):
        """
        根据返回打印结果
        :return:
        """
        result = self.weather()

        if result['result'] == '雪':
            print('下雪了！！！')
        elif result['result'] == '雨':
            print('下雨了！！！')
        elif result['result'] == '晴天':
            print('晴天！！！！')
        else:
            print('返回值错误！')
        return result['status']