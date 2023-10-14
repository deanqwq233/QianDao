#1.0.1为大版本更新，更换POST，将保存的文件单独放到一个文件夹里
# coding:utf-8
import json
from flask import Flask, request
import datetime
import os

app = Flask(__name__)

BASE_URL = '/'

date = datetime.date.today()

# 接收get请求
@app.route(BASE_URL + '/QianDao/', methods=['POST'])
def test_get():
    # 解析请求参数
    param = request.args.to_dict()
    name = param['name']
    filename = datetime.datetime.now().strftime('%y-%m-%d-%H') + ".txt"
    #写入文件
    if "V1.0.1" in name:
        QDFILE = os.getcwd() +'\\QDFiles\\'+ filename
        f = open(QDFILE, 'a' ,encoding = 'utf-8')
        print(name, file = f)
        f.close()
        # 返回json
        result_json = json.dumps("Success.")
        return result_json
        
    else:
        # 返回json
        result_json = json.dumps("Failed.")
        return result_json
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
