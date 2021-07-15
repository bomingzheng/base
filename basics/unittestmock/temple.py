"""
==============================
    @author: bmz
    @contact: Bomz@dianzhong.com
    @software: PyCharm
    @File:  temple.py
    @time: 2021/7/13 14:33
    @Site : 
    @Version:  2.0
==============================
"""


def pay():
    """
        假设这里是一个支付的功能,未开发完
        支付成功返回：{"result": "success", "reason":"null"}
        支付失败返回：{"result": "fail", "reason":"余额不足"}
        reason返回失败原因
    :return:
    """

    pass


def pay_statues():
    """
        根据支付的结果判断跳转到对应页面
        :return:
    """
    result = pay()
    print(result)
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            print("失败原因：%s" % result["reason"])
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"
