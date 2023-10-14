#1.0.1为大版本更新，更换POST，将保存的文件单独放到一个文件夹里
# coding:utf-8
import requests
import json
import datetime
import socket
from tkinter import *
from tkinter import messagebox
import re

IP = socket.gethostbyname(socket.gethostname())

# 添加一个字典来跟踪用户的签到状态
sign_in_status = {}
ifsignin = False


# 检查输入的字符串是否为中文
def is_chinese(text):
    if re.match(r'^[\u4e00-\u9fa5]+$', text):
        return True
    else:
        return False

def get_test():
    global ifsignin
    url = 'http://192.168.3.224:8080/QianDao/' #填写你服务端的IP地址+后缀
    name = name_entry.get()
    # 检查用户是否已经签到
    if not is_chinese(name):
        messagebox.showerror("错误", "请输入中文姓名")
        name_entry.delete(0, END)
        result_text.delete(1.0, END)
        result_text.insert(INSERT, "请输入中文姓名")
    else:
        if ifsignin == True:
            messagebox.showerror("错误", "不能重复签到")
            name_entry.delete(0, END)
            result_text.delete(1.0, END)
            result_text.insert(INSERT, "不能重复签到")
        else:
            data_json = {
                "name": datetime.datetime.now().strftime('%H:%M:%S') + " " + name + " " + IP + " V1.0.1",
            }
            res = requests.post(url, params=data_json)
            result_text.delete(1.0, END)
            result_text.insert(INSERT, "等待服务器响应……")
            # 如果服务器返回"Success"，则将用户标记为已签到
            if "Success." in res.text:
                result_text.delete(1.0, END)
                result_text.insert(INSERT, "签到成功，时间：" + datetime.datetime.now().strftime('%H:%M:%S') + "，" + name + "同学，位于" + IP)
                messagebox.showinfo(name, "你好！" + name + "位于" + IP)
                sign_in_status[name] = True
                ifsignin = True
            else: 
                if "Failed." in res.text:
                    result_text.delete(1.0, END)
                    result_text.insert(INSERT, "请使用最新版客户端")
                    messagebox.showinfo(name, "请使用最新版客户端")
                


root = Tk()
root.title("QianDao1.0.1：" + IP)

frame = Frame(root)
frame.pack(padx=10, pady=10)

#ip_label = Label(frame, text="欢迎你，" + IP)
#ip_label.grid(row=0, column=0)

name_label = Label(frame, text="请输入你的姓名：")
name_label.grid(row=1, column=0)
name_entry = Entry(frame)
name_entry.grid(row=1, column=1)

submit_button = Button(frame, text="签到", command=get_test)
submit_button.grid(row=1, column=2)

result_label = Label(frame, text="服务器返回结果：")
result_label.grid(row=2, column=0)
result_text = Text(frame, wrap=WORD)
result_text.grid(row=2, column=1, columnspan=2)

auth_label = Label(frame, text="2022-2023@SamTech, All Rights Reserved.")
auth_label.grid(row=3, column=1)

root.mainloop()
