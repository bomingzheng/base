"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: encryption.py
@time: 2020/9/4 16:56
@desc:
==============================
"""

import hashlib


def sha1_encryption(*args):
    list1 = []
    for i in args:
        list1.append(i)
    s = "".join(list1)
    y = hashlib.sha1(s.encode("utf-8"))
    w = y.hexdigest()
    return w


def md5_encryption(*args):
    list2 = []
    for i in args:
        list2.append(i)
    qa = "".join(list2)
    ysq = hashlib.md5(qa.encode("utf-8"))
    w = ysq.hexdigest()
    return w


def md5_encryption_salt(*args, salt='qaz'):      # md5加盐，盐的默认值是空
    list3 = []
    for i in args:
        list3.append(i)
    sqw = "".join(list3)
    ysz = sqw + salt
    m = hashlib.md5(str(ysz).encode())     # 先变成bytes类型才能加密创建md5对象
    return m.hexdigest()                    # 获取加密后的字符串


if __name__ == '__main__':
    nonce = "123456"
    timestamp = "1583868236"
    client_id = "100074085"
    token = "i9h3cblxzKjaQgdlbK"

    print(sha1_encryption(token, timestamp, client_id, nonce))
    print(md5_encryption(token, timestamp, client_id, nonce))
    print(md5_encryption_salt(token, timestamp, client_id, nonce))

