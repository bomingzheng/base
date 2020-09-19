"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: 进程_线程_协程.py
@time: 2020/9/19 10:54
@desc:
==============================
"""

# 10000请求，使用2个进程，进程开启3个线程，线程开启5个协程
import time
import requests
from threading import Thread
from multiprocessing import Process, Queue
import gevent



