"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: coded.py
@time: 2020/9/4 16:56
@desc:
==============================
"""

import hashlib
import base64
import hmac


def sha1_encrypt(*args):
    list1 = []
    for i in args:
        list1.append(i)
    s = "".join(list1)
    y = hashlib.sha1(s.encode("utf-8"))
    w = y.hexdigest()
    return w


def md5_encrypt(*args):
    list2 = []
    for i in args:
        list2.append(i)
    qa = "".join(list2)
    ysq = hashlib.md5(qa.encode("utf-8"))
    w = ysq.hexdigest()
    return w


def md5_encrypt_dual(*args):     # 双重MD5加密
    list2 = []
    for i in args:
        list2.append(i)
    qa = "".join(list2)
    md5_obj = hashlib.md5(qa.encode("utf-8"))
    str1 = md5_obj.hexdigest()                      # 加密1次
    obj2 = hashlib.md5(str1.encode("utf-8"))
    str2 = obj2.hexdigest()                         # 加密2次
    return str2                                     # 双重加密后，同样解密开


def md5_encrypt_salt(*args, salt='qaz'):      # md5加盐，盐的默认值是空
    list3 = []
    for i in args:
        list3.append(i)
    sqw = "".join(list3)
    ysz = sqw + salt
    m = hashlib.md5(str(ysz).encode())     # 先变成bytes类型才能加密创建md5对象
    return m.hexdigest()                    # 获取加密后的字符串


def hmc_encrypt_salt(*args):        # hamc加密是以一个密钥和一个消息作为输入生成一个消息摘要输出用于身份验证
    list3 = []
    for i in args:
        list3.append(i)
    ysz = "".join(list3)
    h = hmac.new(key=ysz, msg='hello')
    h.update('world!')
    ret = h.hexdigest()
    return ret


def sha256_encrypt(*args):
    list4 = []
    for i in args:
        list4.append(i)
    qa = "".join(list4)
    ysq = hashlib.sha256(qa.encode("utf-8")).hexdigest()
    return ysq


def bs64_encrypt(*args):
    list4 = []
    for i in args:
        list4.append(i)
    qa = "".join(list4)
    ysq = qa.encode('utf-8')
    bs64 = base64.b64encode(ysq)     # 加密
    s32 = base64.b32encode(ysq)
    bs16 = base64.b16encode(ysq)
    # bs64 = base64.b64decode(args)  # 使用decode进行解密
    # bs32 = base64.b32decode(args)
    # bs16 = base64.b16decode(args)
    return bs64, s32, bs16


if __name__ == '__main__':
    nonce = "123456"
    timestamp = "1583868236"
    client_id = "10005589"
    token = "aNcovnMGkNuklvuP6P122"

    print(sha1_encrypt(token, timestamp, client_id, nonce))
    print(md5_encrypt(token, timestamp, client_id, nonce))
    print(md5_encrypt_dual(token, timestamp, client_id, nonce))
    print(md5_encrypt_salt(token, timestamp, client_id, nonce))
    print(sha256_encrypt(token, timestamp, client_id, nonce))
    print(bs64_encrypt(token, timestamp, client_id, nonce))
