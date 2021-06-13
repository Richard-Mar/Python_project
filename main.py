from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as Mb
import translate
import compare
import search_aa


root = Tk()
root.geometry('500x250')
root.title("生信之友--工具包")

img = Image.open("./pic/dna.png")
photo = ImageTk.PhotoImage(img)
Lab = Label(root, compound='center', image = photo)
Lab.pack()
class Login():
    #flag=False
# 初始化
    acList=["root   ",]
    passwdList=["root   ",]

# 初始化登录界面：工具名信息、账户、密码输入框、密码输入格式
    def __init__(self):

        self.lb_intro = Label(root, text = "生信助手工具包", font = ("黑体", 25, "bold"),fg = "green")
        self.lb_prompt = Label(root, text = "登录",font = ("黑体", 15, "bold"))
        self.lb_ac = Label(root, text = '账户:')
        self.lb_passwd = Label(root, text='密码:')

        self.en_ac_input = Entry(root,width=40)
        self.en_passwd_input = Entry(root, show='-', width=40)

        self.bn_switch_show = Button(root,text = '显示密码',width = 8,command=self.switch_show)
        self.bn_sign_in = Button(root, text="登录", width=10, command = self.sign_in)
        self.bn_sign_up = Button(root, text="注册新账户", width=10, command = self.sign_up)
        self.bn_quit = Button(root, text="退出程序", command = root.quit)
        # 创建菜单
        self.mu_bar = Menu(root)
        self.mu_f_bar = Menu(self.mu_bar)
        for item in ["简洁","美观","经典"]:
            self.mu_f_bar.add_command(label = item)
        self.mu_e_bar = Menu(self.mu_bar)
        self.mu_e_bar.add_command(label = "version --1.0")
        self.mu_a_bar = Menu(self.mu_bar)
        self.mu_a_bar.add_command(label = "马睿锋")
        self.mu_h_bar = Menu(self.mu_bar)
        for item in ["版权信息","帮助文档"]:
            self.mu_h_bar.add_command(label = item)
        self.mu_bar.add_cascade( label = "模式", menu = self.mu_f_bar)
        self.mu_bar.add_cascade( label = "版本", menu = self.mu_e_bar)
        self.mu_bar.add_cascade( label = "作者", menu = self.mu_a_bar)
        self.mu_bar.add_cascade( label = "关于", menu = self.mu_h_bar)
        root["menu"] = self.mu_bar



    def sign_in(self):
        account = self.en_ac_input.get().ljust(10, " ")
        passwd = self.en_passwd_input.get().ljust(10, " ")
        if self.check(account,passwd)==True:
            self.clear_window()
            showTool()
            del self
            return
        else:
            Mb.showinfo(title='登录错误！', message='原因：账号或密码不正确，请检查')
            return

######## for sign_in to use
    def check(self,account,passwd):
        i=0
        while i<len(self.acList):
            if account == self.acList[i] and passwd==self.passwdList[i]:
                return True
            i=i+1
        return False
######## for sign_in to use


    def sign_up(self):

        # 创建子窗口
        self.top = Toplevel()
        self.top.geometry('450x220')
        lb_sign_up =  Label(self.top,text="注册新账户")
        lb_sign_up_ac = Label(self.top, text='账户：')

        passwd = Label(self.top, text='密码：')
        repasswd = Label(self.top, text='重新输入密码：')

        self.top.ac_input = Entry(self.top, width = 30)
        self.top.passwd_input = Entry(self.top, show='-', width = 30)
        self.top.passwd_input_repasswd = Entry(self.top, show = '-', width = 30)
        bn_ok = Button(self.top, command=self.ok_click, text="确认", width=10)
        bn_bcak = Button (self.top, command=self.back_click, text="回到上一级", width = 10)

        lb_sign_up.place(x = 130,y = 30)
        lb_sign_up_ac.place(x = 98, y = 70)
        passwd.place(x = 98, y = 95)
        repasswd.place(x = 50,y = 120)
        self.top.ac_input.place(x = 135, y = 70)
        self.top.passwd_input.place(x = 135, y = 95)
        self.top.passwd_input_repasswd.place(x = 135,y = 120)
        bn_ok.place(x = 140, y = 140)
        bn_bcak.place(x = 240, y = 140)

######## for sign_up to use
    def back_click(self):
        self.top.destroy()
    def ok_click(self):
        get_account = self.top.ac_input.get().ljust(10, " ")
        get_passwd = self.top.passwd_input.get().ljust(10, " ")
        get_repasswd = self.top.passwd_input_repasswd.get().ljust(10, " ")
        if get_repasswd != get_passwd:
            Mb.showinfo(title='注册失败', message='原因：两次密码不一致，请重新输入')
            return
        if self.checkAccount_repeat(get_account) == True:
            Mb.showinfo(title='注册失败', message='原因：账号已存在')
            return
        elif self.checkAccount_repeat(get_account) == False:
            Mb.showinfo(title='注册成功！', message='注册成功,请登录')
            self.acList.append(get_account)
            self.passwdList.append(get_passwd)
            self.top.destroy()
    def checkAccount_repeat(self,get_account):
        i=0
        while i<len(self.acList):
            if get_account==self.acList[i]:
                return True
            i=i+1
        return False
######## for sign_up to use





######### 布局与清理、显示模块
    def place_items(self):
        self.lb_intro.place(x = 145,y = 15)
        self.lb_ac.place(x = 75, y = 90)
        self.lb_passwd.place(x = 75, y = 115)
        self.lb_prompt.place(x = 230,y = 60)

        self.en_ac_input.place(x = 125, y = 90)
        self.en_passwd_input.place(x = 125, y = 115)

        self.bn_switch_show.place(x = 420, y=113)
        self.bn_sign_in.place(x = 135, y = 155)
        self.bn_sign_up.place(x = 240, y = 155)
        self.bn_quit.place(x = 345, y = 155)
    def switch_show(self):
        if(self.en_passwd_input['show'] == '-'):
            self.en_passwd_input['show'] = ''
            self.bn_switch_show['text'] = '隐藏密码'
        else:
            self.en_passwd_input['show'] = '-'
            self.bn_switch_show['text'] = '显示密码'
    def clear_window(self):
        self.lb_ac.destroy()
        self.lb_passwd.destroy()
        self.lb_intro.destroy()
        self.lb_prompt.destroy()

        self.en_ac_input.destroy()
        self.en_passwd_input.destroy()

        self.bn_sign_in.destroy()
        self.bn_sign_up.destroy()
        self.bn_quit.destroy()
        self.bn_switch_show.destroy()
######### 布局与清理、显示模块

class Tool_window():
    def __init__(self):
        self.lb_guide = Label(text="点击需要使用的工具对应的按钮进入工具页面", fg='green')
        self.lb_intro = Label(text="工具选择", font=("黑体", 25, "bold"))
        self.lb_translate = Label(text=" 序列翻译  ")
        self.lb_compare = Label(text=" 序列比对  ")
        self.lb_aa = Label(text='氨基酸查询')

        self.bn_translate = Button(text='A',command = self.translate_window)
        self.bn_compare = Button(text='B', command = self.compare_window)
        self.bn_aa = Button(text='C', command = self.aa_window)

        self.bn_back = Button(text="返回主菜单", command = self.back_to_home)

    def place_items(self):
        self.lb_intro.place(x = 120,y = 15)
        self.lb_translate.place(x = 165, y = 90)
        self.lb_compare.place(x = 165, y = 120)
        self.lb_aa.place(x = 165,y = 150)
        self.lb_guide.place(x = 100,y=180)

        self.bn_translate.place(x = 270, y = 87)
        self.bn_compare.place(x = 270, y = 118)
        self.bn_aa.place(x = 270,y = 148)
        self.bn_back.place(x = 300, y = 200)
    def clear_items(self):
        self.lb_intro.destroy()
        self.lb_translate.destroy()
        self.lb_compare.destroy()
        self.lb_aa.destroy()
        self.lb_guide.destroy()

        self.bn_translate.destroy()
        self.bn_aa.destroy()
        self.bn_compare.destroy()
        self.bn_back.destroy()
    def back_to_home(self):
        self.clear_items()
        logIn()
    def translate_window(self):

        Translate()
        del self
        return
    def compare_window(self):

        Compare()
        del self
        return

    def aa_window(self):

        ShowAA()
        del self
        return


########

#####



def logIn():
    root.geometry('500x300')
    L = Login()
    L.place_items()

def showTool():
    root.geometry('400x250')
    L = Tool_window()
    L.place_items()

def Translate():
    Mb.showinfo(title='翻译', message='请在shell中进行操作,输入Q/q退出')
    print("-" * 10, 'dna翻译', '-' * 10)
    dna=""
    while True:
        dna = input("请输入dna序列:")
        aa,seq = translate.translate_raw(dna);
        if(dna == 'q' or dna =='Q'):
            print("程序退出")
            break
        if(len(aa) == 0 or len(seq) == 0):
            print("没有找到编码区段！")
        else:
            print("aa = {},coding seq = {}".format(aa,seq))
        symbol = input("是否进行下一轮？q/Q退出")
        if (symbol == 'q' or symbol == 'Q'):
            break
def ShowAA():
    Mb.showinfo(title='查询氨基酸信息', message='请在shell中进行操作,输入Q/q退出')
    print("-" * 8, '氨基酸信息查询', '-' * 8)
    while True:
        letter = input("请输入要查询氨基酸的英文字母简写：").upper()
        while(len(letter)!=1):
            letter = input("英文简写字母长度应该为1！请重新输入")
        search_aa.search_aa(letter)
        symbol = input("是否进行下一轮？q/Q退出")
        if (symbol == 'q' or symbol == 'Q'):
            break
def Compare():
    Mb.showinfo(title='序列比对', message='请在shell中进行操作,输入Q/q退出')
    print("-" * 10, '序列比对', '-' * 10)
    while True:
        try:
            gap = int(input("输入惩罚系数：（必须是整数）"))  # 获取gap值
        except:
            gap = int(input("输入有误！重新输入")) # 获取gap值
        if (gap == 'q' or gap == 'Q'):
            break
        s = input("序列1:").upper()  # 获取用户输入的第一条序列
        if (s == 'q' or s =='Q'):
            break
        t = input("序列2:").upper()  # 获取用户输入的第二条序列
        if (t == 'q' or t == 'Q'):
            break
        compare.compare(gap, s, t)
        symbol = input("是否进行下一轮？q/Q退出")
        if(symbol == 'q' or symbol == 'Q'):
            break


logIn()
root.mainloop()