import requests
import urllib
import json
def encode(message,pw):
    return "".join([chr(ord(char)+ord(pw[i%len(pw)])) for i,char in enumerate(message)])
def decode(message,pw):
    return "".join([chr(ord(char)-ord(pw[i%len(pw)])) for i,char in enumerate(message)])
print("welcome to mnet")
name = input("please enter name : ")
room = input("enter room id : ")
pw = input("enter room pw : ")
while True:
    mess = input("=>")
    if mess[0] == "/":
        spl = mess.split()
        if spl[0]=="/help":
            print("/name [name]=> change your name\n/room [room_id]=> swith to room (try public room 1)")
        elif spl[0]=="/show":
            roomd = json.loads(urllib.request.urlopen('http://mtzgnp.pythonanywhere.com/get?room=%s' % room).read())
            for message in roomd:
                try:
                    print("%s\n     %s" % (message["name"],decode(message["message"],pw)) )
                except:
                    print("invalid")
        elif spl[0]=="/name":
            name = mess.replace("/name","")
        elif spl[0] == "/room":
            room = mess.replace("/room","")
            pw = input("enter pw for room %s" % room)
        else:
            print("command not found , for a list of commands type /help")
    else:
        print(requests.get(url = "http://mtzgnp.pythonanywhere.com/post?room=%s&message=%s&name=%s" % (room,encode(mess,pw),name)))
    
