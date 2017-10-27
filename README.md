# mlcode

### 【算法】机器学习相关
#### 动态梯度学习，计算loss
[dyplotLine.py](https://github.com/charlesld/mlcode/blob/master/dyplotLine.py)

> 图片描述的是，对于给定的数据，通过梯度下降不断进行学习，求解最小loss，最后使得通过w b计算的值逼近原数据

![tensor学习动态](https://github.com/charlesld/mlcode/blob/master/tensordygraphic.gif)

#
### 【辅助插件，外挂相关】
#### python2 多线程锁功能单一，不引入三方组件进行修饰，支持超时任务
[代码这里](https://github.com/charlesld/mlcode/blob/master/mutiprocess/lock_wait_expire_for_py2.py)

> 运行实例

```python
start the mission for port 301 
start the mission for port 302 
port is 301
can't get file lock 302 , pass this step
port 301 is running over  

```
#

### 【实战】数据分析相关
#### 杭州车牌摇号分析

[rollingcarnum.py](https://github.com/charlesld/mlcode/blob/master/rollingcarnum.py)
> rollingcarnum.py 是杭州摇车牌的简略分析，目前只做了重名分析。本地数据可以看出，大概可以看出短名字更容易摇中

```python
dda = text.replace(r"↑", "")

# 这个中间有个大写加粗的↑箭头，从pdf而来。可以print text 查看后替换，这里网页被屏蔽。。
```

##### 简析摇号完整数据

昨天数据炸一看，感觉政府偏心，感觉车牌总是给那些短名字的人准备的，今天从摇号的官网爬了完整的数据，再看了一下。

[代码链接](https://github.com/charlesld/mlcode/blob/master/rollingcarcard/crawlrolldata.py)

> 程序运行结果如下

```shell
摇号总数命中： dict_items([('3名字中次数', 130816), ('2名字中次数', 20316), ('4名字中次数', 500)])
高频命中： dict_items([('3名字中次数', 1039), ('2名字中次数', 1961)])
```

> 生产了2张图提高可视化

###### 第一张图是全部数据分析，3字名命中要远高于2字名命中

![全数据分析](https://github.com/charlesld/mlcode/blob/master/pics/hzyh1.png)

###### 第二张图是高频命中，反复容易摇中的名字中，2字名要占大数

![车牌摇号分析](https://github.com/charlesld/mlcode/blob/master/pics/hzyh2.png)

###### 第三张图，应是彩蛋，这里可以用来作为改名指南，数据里，命中最高的名字居然被反复抽中101次。我觉得这里是重点【敲黑板】不打针，不吃药助你轻轻松摇到号，就是按图进行改名，分分钟就成为拥有浙A的人生赢家！

![改名指南](https://github.com/charlesld/mlcode/blob/master/pics/image2.png)
