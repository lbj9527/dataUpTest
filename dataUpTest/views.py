from flask import Flask, request
from flask import render_template, url_for

from dataUpTest import app

name = '顺润'
moshu = 0

@app.route('/')
def index():
    print(request.args.get('count','hi'))  #获取URL参数
    return render_template('index.html', name  = name, moshu = moshu)

@app.route('/query')
def query():
    global moshu
    return str(moshu)


@app.route('/register',methods=['get'])
def register():
    global moshu
    localstatus = request.args.get('status')
    num = request.args.get('index')
    if localstatus == "open":
        moshu  = moshu + 1
    txt = "reiceve #{0} moju data: {1}"
    return txt.format(num, moshu)