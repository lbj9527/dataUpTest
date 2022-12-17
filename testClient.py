import requests
import time


while True:
    ismojuopen = {'status' : "open"}
    r = requests.post("https://lbj9527.pythonanywhere.com/register", data=ismojuopen)
    print(r)
    time.sleep(0.5)