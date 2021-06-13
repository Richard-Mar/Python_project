# 生物信息分析工具包

项目主页：https://github.com/Richard-Mar/Python_project

>学号：519111910095
>
>姓名：马睿锋

<CENTER><FONT SIZE = 5> 目录</FONT></CENTER>

-----------------------

[TOC]

-----------

## Intro

```markdown
生物信息学的dna序列蕴含着大量的遗传信息和丰富的分析位点，使用一款用户友好、操作简单的生信序列分析工具能为序列分析的工作提供巨大的帮助，因此，开发一款整合了序列翻译（自动查找编码区段）、序列比对、氨基酸性质信息查询的综合工具，来方便大家对dna序列翻译相关工作的研究。

该项目利用`Python`作为开发平台，开发出的生物数据分析工具，主要用于DNA序列的比对和最佳匹配输出、智能化翻译RNA并输出翻译结果。
特点是利用GUI编程和`tkinter`包，实现直观的可视化操作，用户友好。
利用PIL库导入图片使得程序更加美观
```

## Platform

```markdown
Platform:
	Python 3.8.5
Package:
	tkinter
	PIL
```



## features

- 注册与登录线上系统
- 根据`rna`序列输出翻译蛋白质
- 序列比对与结果输出
- 生信数据库



## how can I get it?

- 项目github主页:`https://github.com/Richard-Mar/Python_project/blob/main/README.md`	

- 默认账号：

>账户名：root
>
>密码：root



## Usage

### 1.运行Python文件，进入主界面

![image-20210613135023299](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135023299.png)

<CENTER>图1 登录主界面</CENTER>

#### 1.1.主界面信息简介

![image-20210613135255703](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135255703.png)

>菜单栏包含模式、版本、作者、关于四个部分，下面示例展示了其中模式菜单的子菜单
>
>![image-20210613135547759](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135547759.png)

#### 1.2.注册界面介绍

>账户信息验证区可以登录进入下一级页面，如果没有账户，需要注册才能登陆，点击登录注册进入下一级注册窗口
>
>![image-20210613135650550](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135650550.png)
>
>![image-20210613135719627](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135719627.png)
>
>注册完成后，提示可以登录
>
>![image-20210613135822799](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135822799.png)

#### 1.3.其他细节

>可以切换密码显示形式
>
>![image-20210613135847237](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613135847237.png)

### 2.工具选择功能界面

#### 2.1.界面主要信息介绍

![image-20210613140447669](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613140447669.png)

<CENTER>图2 功能选择界面</CENTER>

### 2.2.功能介绍举例

- 翻译功能

>![image-20210613142504707](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613142504707.png)
>
>进入后，按照提示输入序列，软件将自动寻找编码区段并进行翻译。
>
>![image-20210613142751279](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613142751279.png)

- 序列比对功能

>点击按钮B
>
>![image-20210613151144594](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613151144594.png)
>
>进入后，按照提示输入惩罚系数和两个序列
>
>![image-20210613151114104](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613151114104.png)
>
>给出最佳匹配效果

- 氨基酸信息查询功能

>点击按钮C
>
>![image-20210613153836179](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613153836179.png)
>
>进入后，按照提示输入
>
>![image-20210613153908831](D:\马睿锋\Onedrive\OneDrive - sjtu.edu.cn\大二下\md笔记\typora_pictures\image-20210613153908831.png)
>
>给出对应氨基酸的相关信息

## others

- 开发日志：


>```python
>在做工具接口的时候本来也想用tkinter做图形化的直观的界面，但是囿于个人能力有限，在调用次级窗口总会出现上一级窗口的构件进入次级窗口的问题，调试多次未果，加上时间紧迫，来不及继续改进。遂采用功能与窗口分离的选择，实际是无奈之举。
>```

- 建立远程库和上传至github

## Contributors

- Author：马睿锋

## Ref

[1]《tkinter初级教程 》----传智播客 ⼤猫

[2\][Python installer使用](http://c.biancheng.net/view/2690.html)

[3\][基于python的全局与局部序列比对的实现（DNA）](https://blog.csdn.net/mmqwqf/article/details/108922579)

[4\][氨基酸 百度百科](https://baike.baidu.com/item/%E6%B0%A8%E5%9F%BA%E9%85%B8/303574)

[5]Git教程 By 廖雪峰


## 鸣谢

- Thanks to the tutorial of Mr Lu Junchao

