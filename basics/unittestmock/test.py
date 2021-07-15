"""
==============================
    @author: bmz
    @contact: Bomz@dianzhong.com
    @software: PyCharm
    @File:  test.py
    @time: 2021/7/13 14:35
    @Site : 
    @Version:  2.0
==============================
"""
from unittest import mock
import unittest
import temple


class TestPayStatus(unittest.TestCase):
    """
    单元测试用例
    """

    @mock.patch("temple.pay")
    def test_01(self, mock_pay):
        '''测试支付成功场景'''
        # 方法一：mock一个支付成功的数据
        # temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})

        # 方法二：mock.path装饰器模拟返回结果
        mock_pay.return_value = {"result": "success", "reason": "null"}
        # 根据支付结果测试页面跳转
        statues = temple.pay_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    @mock.patch("temple.pay")
    def test_02(self, mock_pay):
        """
        支付失败用例
        :param mock_pay:
        :return:
        """

        mock_pay.return_value = {"result": "fail", "reason": "余额不足"}
        # 根据支付结果测试页面跳转
        statues = temple.pay_statues()
        self.assertEqual(statues, "支付失败")


if __name__ == "__main__":
    unittest.main()





