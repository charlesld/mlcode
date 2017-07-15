#coding:utf-8
#!/usr/bin/env python
#Created by root on 17-7-15.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

import time


def addLayer(inputs, in_zise, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_zise, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)  # 1行，out_size列，推荐不为0 所以加上0.1
    Wx_plus_b = tf.matmul(inputs, Weights) + biases

    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)

    return outputs


import numpy as np
from matplotlib import pyplot as plt

Xdata = np.linspace(-1, 1, 300)[:, np.newaxis]

noise = np.random.normal(0, 0.05, Xdata.shape)  # 生成噪声
Ydata = np.square(Xdata) - 0.5 + noise

xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# plt.plot(Xdata, Ydata)
# plt.show()

L1 = addLayer(xs, 1, 10, activation_function=tf.nn.relu)  # 定义中间层10个神经元.relu 激励函数
predition = addLayer(L1, 10, 1, activation_function=None)  # 生成输出结果
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - predition), reduction_indices=[1]))
# （（（ys-输出结果）的平方）求和）求平均
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(Xdata, Ydata)
# plt.ion()  # plt之后不暂停
plt.show(block=False)
time.sleep(5)

with tf.Session() as sess:
    sess.run(init)
# sess = tf.Session()
# sess.run(init)
    for i in range(2001):
        sess.run(train_step, feed_dict={xs: Xdata, ys: Ydata})

        if i % 20 == 0:
            # print (sess.run(loss,feed_dict={xs:Xdata,ys:Ydata}))  #获取损失函数
            try:
                ax.lines.remove(lines[0])  # 对lines的进行清除，之后重新生成
            except Exception:
                pass

            predition_value = sess.run(predition, feed_dict={xs: Xdata, ys: Ydata})
            lines = ax.plot(Xdata, predition_value, 'r-', lw=5)

            plt.pause(0.1)
# plt.waitforbuttonpress(timeout=-1) #加上这行后图形不会自动退出，手动关闭后会报错，不影响使用
