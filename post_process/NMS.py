import numpy as np
#定义一个数据
boxes = np.array([[100,100,210,210,0.72],
                  [250, 250, 420, 420, 0.8],
                  [220, 220, 320, 330, 0.92],
                  [100, 100, 210, 210, 0.72],
                  [230, 240, 325, 330, 0.81],
                  [220, 230, 315, 340, 0.9]])

def py_cpu_nms(dets, thresh):
    #计算数据赋值和计算对应矩形框的面积
    #dets的数据格式是dets[[xmin,ymin,xmax,ymax,scores],...]
    x1 =dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (y2-y1+1) * (x2-x1+1)
    scores = dets[:, 4]
    print('areas', areas)
    print('scores', scores)

    keep = [] #用于存放NMS后剩余的方框
    #取出分数从到到小排列的索引。.argsort()是从小到大排列，[::-1]是列表头尾颠倒一下
    index = scores.argsort()[::-1]
    print(index)
    # 上面这两句比如分数[0.72 0.8  0.92 0.72 0.81 0.9 ]
    #  对应的索引index[  2   5    4     1    3   0  ]记住是取出索引，scores列表没变。

    while index.size > 0:
        print(index)
        #取出第一个方框进行和其他方框比对，看有没有可以合并的
        i = index[0]
        # 因为我们这边分数已经按从大到小排列了。
        # 所以如果有合并存在，也是保留分数最高的这个，也就是我们现在那个这个
        # keep保留的是索引值，不是具体的分数。
        keep.append(i)
        print(keep)
        print('x1', x1[i])
        print(x1[index[1:]])

        # 计算交集的左上角和右下角
        # 这里要注意，比如x1[i]这个方框的左上角x和所有其他的方框的左上角x的



import matplotlib.pyplot as plt

def plot_bbox(dets, c='k'):


plt.figure(1)
ax1 = plt.subplot(1,2,1)
ax2 = plt.subplot(1,2,2)

plt.sca(ax1)
plt_bbox(boxes, 'k')

