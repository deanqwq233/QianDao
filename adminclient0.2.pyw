# coding:utf-8
import requests
import json
import datetime
import socket
from tkinter import *
from tkinter import messagebox
import re

IP = socket.gethostbyname(socket.gethostname())

def get_test():
    global ifsignin
    url = 'http://192.168.3.224:8182/QDadmin/' #填写你服务端的IP地址+后缀
    name = name_entry.get()
    pwd = pwd_entry.get()
    data_json = {
    "name": "V0.2" + pwd +" DATE: "+ name,
    }
    res = requests.post(url, params=data_json)
    result_text.delete(1.0, END)
    result_text.insert(INSERT, "等待服务器响应……")
    # 如果服务器返回"Success"，则将用户标记为已签到
    if "VerFailed" in res.text:
        result_text.delete(1.0, END)
        result_text.insert(INSERT, "版本过低，请联系管理员。")
    if "Failed" in res.text:
        result_text.delete(1.0, END)
        result_text.insert(INSERT, "出现错误，请联系管理员。")
    else: 
        result_text.delete(1.0, END)
        result_text.insert(INSERT, res.text)
                


root = Tk()
root.title("欢迎QDadmin0.2：" + IP)

frame = Frame(root)
frame.pack(padx=10, pady=10)

#ip_label = Label(frame, text="欢迎你，" + IP)
#ip_label.grid(row=0, column=0)

pwd_label = Label(frame, text="密码：")
pwd_label.grid(row=0, column=0)
pwd_entry = Entry(frame)
pwd_entry.grid(row=0, column=1)

name_label = Label(frame, text="时间：yy-MM-DD-HH")
name_label.grid(row=1, column=0)
name_entry = Entry(frame)
name_entry.grid(row=1, column=1)
submit_button = Button(frame, text="查询", command=get_test)
submit_button.grid(row=1, column=2)

result_label = Label(frame, text="服务器返回：")
result_label.grid(row=2, column=0)
result_text = Text(frame, wrap=WORD)
result_text.grid(row=2, column=1, columnspan=2)

auth_label = Label(frame, text="2022-2023@SamTech, All Rights Reserved.")
auth_label.grid(row=3, column=1)

root.mainloop()
