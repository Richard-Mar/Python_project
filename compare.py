import numpy as np
#定义全局变量列表finalList存储最后回溯的路径  finalOrder1,finalOrder2存储最后的序列 finalRoad用于存储方向路径用于最后画图
def createList():
    global finalList
    global finalOrder1
    global finalOrder2
    global finalRoad
    finalList = []
    finalOrder1 = []
    finalOrder2 = []
    finalRoad = []
#创建A G C T 对应的键值对，方便查找计分矩阵中对应的得分
def createDic():
    dic = {'A':0,'G':1,'C':2,'T':3}
    return dic
#构建计分矩阵
# A G C T
def createGrade():
    grade = np.matrix([[10,-1,-3,-4],
                       [-1,7,-5,-3],
                       [-3,-5,9,0],
                       [-4,-3,0,8]])
    return grade

#计算两个字符的相似度得分函数
def getGrade(a,b):
    dic = createDic()  # 碱基字典 方便查找计分矩阵
    grade = createGrade()  # 打分矩阵grade
    return grade[dic[a],dic[b]]

#构建得分矩阵函数 参数为要比较序列、自定义的gap值
def createMark(s,t,gap):
    a = len(s)                         #获取序列长度a,b
    b = len(t)
    mark = np.zeros((a+1,b+1))         #初始化全零得分矩阵
    direction = np.zeros((a+1,b+1,3))  #direction矩阵用来存储得分矩阵中得分来自的方向   第一个表示左方 第二个表示左上 第三个表示上方 1表示能往哪个方向去
                                       #由于得分可能会来自多个方向，所以使用三维矩阵存储

    direction[0][0] = -1               #确定回溯时的结束条件 即能够走到方向矩阵的值为-1
    mark[0,:] = np.fromfunction(lambda x, y: gap * (x + y), (1, b + 1), dtype=int)     #根据gap值将得分矩阵第一行计算出
    mark[:,0] = np.fromfunction(lambda x, y: gap * (x + y), (1, a + 1), dtype=int)     #根据gap值将得分矩阵第一列计算出
    for i in range(1,b+1):
        direction[0,i,0] = 1
    for i in range(1, a + 1):
        direction[i, 0, 2] = 1

    for i in range(1,a+1):
        for j in range(1,b+1):
            threeMark = [mark[i][j-1],mark[i-1][j-1],mark[i-1][j]]         #threeMark表示现在所要计算得分的位置的左边 左上 上边的得分
            threeGrade = [gap,getGrade(s[i-1],t[j-1]),gap]                 #threeGrade表示经过需要计算得左边 左上 上边的空位以及相似度得分
            finalGrade = np.add(threeMark,threeGrade)                      #finalGrade表示最终来自三个方向上的得分
            mark[i][j] = max(finalGrade)                                   #选取三个方向上的最大得分存入得分矩阵
            #可能该位置的得分可以由多个方向得来，所以进行判断并循环赋值
            for k in range(0,len([y for y,x in enumerate(finalGrade) if x == max(finalGrade)])):
                directionList = [y for y,x in enumerate(finalGrade) if x == max(finalGrade)]
                direction[i][j][directionList[k]]  = 1
    return mark,direction

#回溯函数 参数分别为 得分矩阵 方向矩阵 现在所处得分矩阵的位置 以及两个序列
def remount(mark,direction,i,j,s,t):
    if direction[i][j][0] == 1 :
        if direction[i][j-1][0] == -1:            #如果该位置指向左边 先判断其左边是否是零点
            finalList.append(0)                   #如果是 将该路径存入路径列表
            finalList.reverse()                   #将列表反过来得到从零点开始的路径
            index1 = 0                            #记录现在所匹配序列s的位置 因为两个字符串可能是不一样长的
            index2 = 0                            #记录现在所匹配序列t的位置
            for k in finalList:
                if k == 0 :
                    finalOrder1.append("-")
                    finalOrder2.append(t[index2])
                    index2 += 1
                if k == 1 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append(t[index2])
                    index1 += 1
                    index2 += 1
                if k == 2 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append("-")
                    index1 += 1
            finalList.reverse()  # 将原来反转的路径再返回来
            finalRoad.append(np.array(finalList))  # 将此次的路径添加到最终路径记录用于最后画图
            finalList.pop()                       #输出后将当前方向弹出 并回溯
            return
        else :
            finalList.append(0)                   #如果不是零点 则将该路径加入路径矩阵，继续往下走
            remount(mark,direction,i,j-1,s,t)
            finalList.pop()                       #该方向走完后将这个方向弹出  继续下一轮判断 下面两个大的判断同理
    if direction[i][j][1] == 1 :
        if direction[i-1][j-1][0] == -1:

            finalList.append(1)
            finalList.reverse()                   # 将列表反过来得到从零点开始的路径
            index1 = 0                            # 记录现在所匹配序列s的位置 因为两个字符串可能是不一样长的
            index2 = 0                            # 记录现在所匹配序列t的位置
            for k in finalList:
                if k == 0 :
                    finalOrder1.append("-")
                    finalOrder2.append(t[index2])
                    index2 += 1
                if k == 1 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append(t[index2])
                    index1 += 1
                    index2 += 1
                if k == 2 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append("-")
                    index1 += 1
            finalList.reverse()  # 将原来反转的路径再返回来
            finalRoad.append(np.array(finalList))  # 将此次的路径添加到最终路径记录用于最后画图
            finalList.pop()
            return
        else :
            finalList.append(1)
            remount(mark,direction,i-1,j-1,s,t)
            finalList.pop()
    if direction[i][j][2] == 1 :
        if direction[i-1][j][0] == -1:
            finalList.append(2)
            finalList.reverse()                      # 将列表反过来得到从零点开始的路径
            index1 = 0                               # 记录现在所匹配序列s的位置 因为两个字符串可能是不一样长的
            index2 = 0                               # 记录现在所匹配序列t的位置
            for k in finalList:
                if k == 0 :
                    finalOrder1.append("-")
                    finalOrder2.append(t[index2])
                    index2 += 1
                if k == 1 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append(t[index2])
                    index1 += 1
                    index2 += 1
                if k == 2 :
                    finalOrder1.append(s[index1])
                    finalOrder2.append("-")
                    index1 += 1
            finalList.reverse()                    # 将原来反转的路径再返回来
            finalRoad.append(np.array(finalList))  # 将此次的路径添加到最终路径记录用于最后画图
            finalList.pop()
            return
        else :
            finalList.append(2)
            remount(mark,direction,i-1,j,s,t)
            finalList.pop()
def compare(gap,s,t):
    createList()
    a = len(s)                      #获取s的长度
    b = len(t)                      #获取t的长度
    mark,direction = createMark(s,t,gap)
    remount(mark,direction,a,b,s,t) #调用回溯函数
    c = a if a > b else b          #判断有多少种比对结果得到最终比对序列的长度
    total = int(len(finalOrder1)/c)
    for i in range(1,total+1):     #循环输出比对结果
        k = str(i)
        print("序列比对结果 "+k+" 是：")
        print(finalOrder1[(i-1)*c:i*c])
        print(finalOrder2[(i-1)*c:i*c])

# 测试代码
if __name__ == '__main__':
    compare()

