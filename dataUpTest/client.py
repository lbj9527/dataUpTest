import requests
import time
while True:
    #r = requests.get('https://lbj9527.pythonanywhere.com:80/register?status=open')
    r = requests.get('http://127.0.0.1:5000/register?index=8&status=open')
    print(r.text)
    time.sleep(0.5)
