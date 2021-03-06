import base64
import sys
import requests as r
import random

url_01 = "http://127.0.0.1:5000/"
url_02 = "https://iot.pxl-co.ml/"
url_03 = "https://xxiot.herokuapp.com/"

extra_url_01 = "api/temps"
extra_url_02 = "api/temps/1"

data_01 = {"value":str(random.random()*10),"place":"pxl"}
data_02 = {"value":str(random.random()*10),"place":"ks51"}

urls = [url_01, url_02, url_03]

def init(res):
    global extra_url_02
    q=r.get(res)
    if q.status_code==200:
        rs = q.json()
        print(len(rs['temps']))
        if len(rs['temps'])>0:
            extra_url_02 = extra_url_02[:-1]+str(rs['temps'][-1]['id'])
            print(extra_url_02)


def get_test(res):
    q=r.get(res)
    print(q.json())

def post_test(res):
    q = r.post(res,json=data_01)
    print(q.json())

def put_test(res):
    q = r.put(res,json=data_02)
    print(q.json())

def delete_test(res):
    q = r.delete(res)
    print(q.json())


if __name__ == '__main__':
    n = input("Input number for url : ")
    url = urls[int(n)];print(url)

    # post_test(url+extra_url_01)
    # get_test(url+extra_url_01)

    # get_test(url+extra_url_02)
    # put_test(url+extra_url_02)
    # get_test(url+extra_url_02)
    # delete_test(url+extra_url_02)

    # get_test(url+extra_url_01)

    functionList_01 = [post_test,init, get_test]
    functionList_02 = [get_test, put_test,get_test,delete_test]

    for foo in functionList_01:
        foo(url+extra_url_01)

    for foo in functionList_02:
        foo(url+extra_url_02)

    get_test(url+extra_url_01)
