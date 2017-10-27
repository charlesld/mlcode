# coding:utf-8
# !/usr/bin/env python

import threading
import time
from functools import wraps


class InstanceConfigLock():
    lock = threading.Lock()


def catch_lock_expire(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        for _ in range(5):
            try:
                # print("sssssss in getting")
                ca = func(*args, **kwargs)
                if not ca:
                    continue
                return ca
            finally:
                time.sleep(1)

    return wapper


@catch_lock_expire
def lock_with_timeout(block):
    return InstanceConfigLock.lock.acquire(block)


def release_with_unlock():
    try:
        InstanceConfigLock.lock.release()
    except Exception as e:
        print e


def build_instance_config(port, block=1):
    print ("start the mission for port %s " % port)
    if not lock_with_timeout(block):
        print ("can't get file lock %s , pass this step" % port)
        return

    print("port is %s" % port)
    time.sleep(10)
    print ("port %s is running over  " % port)
    release_with_unlock()


if __name__ == '__main__':
    t = threading.Thread(target=build_instance_config, args=(301,), name="231")
    t.start()
    t1 = threading.Thread(target=build_instance_config, args=(302, 0,))
    t1.start()


"""
输出结果:

start the mission for port 301 
start the mission for port 302 
port is 301
can't get file lock 302 , pass this step
port 301 is running over  

"""
