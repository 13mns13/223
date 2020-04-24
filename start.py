import requests, time
from threading import Thread

def method(method, p):
    param = {
        #196378cf8361e922f72e5cca7356939ef0774c7720936ea6a9192fdb701a4b3f34c195d7b9382a7b08318
        #3d9bdf9b7e9e468c118daba5a92829dd723c554c9a81fd2906ba03b7fe59dc03d17165d2ac1bd84aca833
        "access_token":"3d9bdf9b7e9e468c118daba5a92829dd723c554c9a81fd2906ba03b7fe59dc03d17165d2ac1bd84aca833",
        "v": 5.103
    }
    for i in p:
        param[i]=p[i]
    return requests.get(f"https://api.vk.com/method/{method}", params= param).json()

def voice(id):
    while True:
        try:
            method("messages.setActivity", {"peer_id":id,"type":"audiomessage"})
        except: pass

def main():
    response = method("messages.getConversations", {"offset":0,"count":200,"filter":"all"})["response"]
    count = response["count"]
    ids = []
    c_count = 0
    for i in range(0,count, 200):
        items = method("messages.getConversations", {"offset":i,"count":200,"filter":"all"})["response"]["items"]
        for j in range(len(items)):
            id = items[j]["conversation"]["peer"]["id"]

            if id not in ids and id>0:
                ids.append(id)
                c_count+=1
        if c_count>400:
            break

    #ids.remove(153656747)
    print("start")
    for id in ids:
        t = Thread(target=voice, args=(id,))
        t.name = id
        t.start()

    while True:
        pass

if __name__ == "__main__":
    main()