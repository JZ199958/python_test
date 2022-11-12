from tkinter import *
import pymysql
from tkinter.messagebox import *
from tkinter import ttk


def get_connect():
    conn = pymysql.connect(host='localhost', user="root", passwd='GAO147258369', database='stu')
    return conn


window = Tk()
window.geometry('500x300')
window.title('登录账号！')


def create():
    root = Toplevel()
    root.geometry('700x800')
    root.title('学生管理系统')

    Label(root, text="学号：").place(relx=0, rely=0.05, relwidth=0.1)
    Label(root, text="姓名：").place(relx=0.5, rely=0.05, relwidth=0.1)
    Label(root, text="性别：").place(relx=0, rely=0.1, relwidth=0.1)
    Label(root, text="电话：").place(relx=0.5, rely=0.1, relwidth=0.1)

    sid1 = StringVar()
    name1 = StringVar()
    sex1 = StringVar()
    phone = StringVar()
    Entry(root, textvariable=sid1).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
    Entry(root, textvariable=name1).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)

    Entry(root, textvariable=sex1).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
    Entry(root, textvariable=phone).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)

    def add():
        list1 = []
        list1.append(sid1.get())
        list1.append(name1.get())
        list1.append(sex1.get())
        list1.append(phone.get())
        # print(list1)
        connection = get_connect()
        cur = connection.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'insert into student(学号,姓名,性别,电话) values("%s","%s","%s", "%s")'
        sid = int(list1[0])
        name = list1[1]
        sex = list1[2]
        iphone = int(list1[3])
        try:
            cur.execute(sql % (sid, name, sex, iphone))
            connection.commit()
        except Exception as e:
            connection.rollback()
            raise e
        finally:
            connection.close()
        showinfo('提示', '添加成功！')

    def search():
        showinfo('提示', '请输入学号！')
        into = int(sid1.get())
        conn = pymysql.connect(host='localhost', user="root", passwd="", database='stu')
        cur = conn.cursor()
        sql = 'select * from student ;'
        cur.execute(sql)
        all = cur.fetchall()
        for i in range(len(all)):
            for j in all:
                if into == j[0]:
                    treeview.insert('', i, value=(j[0], j[1], j[2], j[3]))
                    break
            break

    def search_all():
        conn = pymysql.connect(host='localhost', user="root", passwd="", database='stu')
        cur = conn.cursor()
        sql = 'select * from student ;'
        cur.execute(sql)
        f = cur.fetchall()
        for i in range(len(f)):
            # for j in range(len(i)):
            treeview.insert('', i, value=(f[i][0], f[i][1], f[i][2], f[i][3]))

    Button(root, text="添加信息", command=add).place(relx=0.1, rely=0.2, width=100)
    Button(root, text="查询个人信息", command=search).place(relx=0.3, rely=0.2, width=100)
    Button(root, text="查询所有信息", command=search_all).place(relx=0.6, rely=0.2, width=100)
    Button(root, text="退出程序", command=root.quit).place(relx=0.8, rely=0.2, width=100)

    columns = ('学号', '姓名', '性别', '电话')
    treeview = ttk.Treeview(root, show='headings', columns=columns)
    treeview.column('学号', width=150, anchor='center')
    treeview.column('姓名', width=150, anchor='center')
    treeview.column('性别', width=150, anchor='center')
    treeview.column('电话', width=150, anchor='center')

    treeview.heading('学号', text='学号')
    treeview.heading('姓名', text='姓名')
    treeview.heading('性别', text='性别')
    treeview.heading('电话', text='电话')

    treeview.place(rely=0.3, relwidth=0.97)


Label(window, text='账号:').place(relx=0, rely=0.05, relwidth=0.3)
Label(window, text='密码：').place(relx=0, rely=0.15, relwidth=0.3)

# 鼠标定位
zh = StringVar()
mm = StringVar()
# 输入框
Entry(window, textvariable=zh, show=None).place(relx=0.3, rely=0.05, relwidth=0.3)
Entry(window, textvariable=mm, show='*').place(relx=0.3, rely=0.15, relwidth=0.3)


# 登陆函数
def dl():
    if zh.get() == '20' and mm.get() == '':
        # showinfo('提示！','登录成功！')
        # window.quit()
        return create()
    else:
        showerror('错误！', '账号或密码错误！')


Button(window, text='登录', command=dl).place(relx=0.2, rely=0.3, relwidth=0.5)

window.mainloop()
