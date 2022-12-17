import requests

ismojuopen = {'status' : "open"}
r= requests.post("http://127.0.0.1:5000/register",data = ismojuopen)
print(r.text)