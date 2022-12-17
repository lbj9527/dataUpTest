import requests
import time


while True:
    ismojuopen = {'status' : "open"}
    r = requests.post("https://lbj9527.pythonanywhere.com/register", data=ismojuopen)
    #r = requests.post("http://127.0.0.1:5000//register", data=ismojuopen)
    print(r)
    time.sleep(0.5)