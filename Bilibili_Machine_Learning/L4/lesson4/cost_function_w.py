import matplotlib.pyplot as plt
import dataset
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#从数据中获取随机豆豆
m=100
xs,ys = dataset.get_beans(m)


#配置图像
plt.title("Size-Toxicity Function", fontsize=12)
plt.xlabel('Bean Size')
plt.ylabel('Toxicity')

# 豆豆毒性散点图
plt.scatter(xs, ys) 

#预测函数
w=0.1
b=0.1
y_pre = w*xs+b