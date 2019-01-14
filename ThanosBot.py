import fbchat 
from fbchat import Client
from fbchat.models import *
from getpass import getpass 
import random

#THANOS BOT THANOS BOT

def getParticipants(client, group_id):
    return list(client.fetchGroupInfo(group_id)[group_id].participants)

def msgGrp(sender,txt,receiver):
    sender.send(Message(text=txt),thread_id=receiver.uid,thread_type=ThreadType.GROUP)

username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of groups: ")) 
for i in range(no_of_friends): 
    name = str(input("Name: ")) 
    friends = client.searchForGroups(name)  
    friend = friends[0] 
    idl=getParticipants(client, friend.uid)
    members=len(idl)
    half=int(members/2)
    assigned=1
    for e in idl:
        if e==client.uid:
            idl.remove(e)
    print(idl)
    print(half)
    #intro=msgGrp(client,"Thanos Bot Activated",friend)
    #snap=msgGrp(client,"*snap*",friend)
    #sent=msgGrp(client,"Perfectly Balanced",friend)
    intro=client.send(Message(text="Thanos Bot Activated"), thread_id=friend.uid, thread_type=ThreadType.GROUP)
    snap=client.send(Message(text="*snap*"), thread_id=friend.uid, thread_type=ThreadType.GROUP)
    if snap:
        print("Snapped!")
    for s in range(0,half):
        dead=random.choice(idl)
        client.removeUserFromGroup(user_id=dead,thread_id=friend.uid)
        idl.remove(dead)
    #msg = str(input("Message: ")) 
    #for i in range(0,1):
    sent=client.send(Message(text="Perfectly balanced."), thread_id=friend.uid, thread_type=ThreadType.GROUP)
    if sent: 
        print("The group is now balanced.") 
client.logout()
