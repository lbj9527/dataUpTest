from flask import Flask, request
from flask import render_template, url_for

app = Flask(__name__)

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


@app.route('/register',methods=['post'])
def register():
    global moshu
    localstatus = (request.form['status'])
    if localstatus == "open":
        moshu  = moshu + 1
    txt = "reiceve moju data: {}"
    return txt.format(moshu)

if __name__ == '__main__':
    app.run(debug = True)