import requests
import json

def main():
    # url = 'http://127.0.0.1:8000/item/'
    # body = {
    #     "name": "shirt",
    #     "description": "this is shirt",
    #     "price": 1990,
    #     "tax": 1.1
    # }
    # res = requests.post(url, json.dumps(body))
    # print(res.json())

    with open("./sample.json", mode="r") as f:
        url = 'http://127.0.0.1:8000'
        res = requests.post(url, json=json.load(f))
        print(res.json())


if __name__=="__main__":
    main()