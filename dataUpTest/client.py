import requests
import time
while True:
    # jdata={
    #     "status" : "open"
    # }
    # r = requests.post('http://lbj9527.pythonanywhere.com/register',data=jdata)
    r = requests.get('http://127.0.0.1:5000/register?status=open')
    print(r.text)
    time.sleep(0.5)
