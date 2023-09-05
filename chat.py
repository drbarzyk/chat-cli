'''
Created on Apr 28, 2020
@author: danbarzyk
'''
import requests
import matplotlib.pyplot as plt
url = 'https://posthere.io/hw13chatmsgs'
texts = 0
chat = {
    "sender": "",
    "recipient": "",
    "message": ""
    }
flags = {
    ":clear":"Clears all chats",
    ":update":"Updates the chat",
    ":quit":"Quits the chat"
    }
def start():
    chat["sender"] = input("Enter sender name: ")
    chat["recipient"] = input("Enter recipient name: ")
    print("\nSpecial flags:")
    for flag, desc in flags.items():
        print(flag + " -- " + desc)
    print("\n-----------------------\n")
    getMessages()
def isCommand(s):
    return(s in flags)
def sendMessage():
    chat["message"] = input("Enter message: ")
    chatPost = {
        "sender":chat["sender"],
        "recipient":chat["recipient"],
        "message":chat["message"]
        }
    requests.post(url, data=chatPost)
    #If the message is not one of the commands, display all the messages in the
chat after sending
    if (not isCommand(chat["message"])):
        print()
        getMessages()
def getMessages():
    r = requests.get(url, headers = {'accept': 'application/json'})
    messages = r.json()
#For each message, print it out if it is not a command and is part of this chat

    for i in range(len(messages) - 1, -1, -1):
        text = messages[i]['body']['message']
        tstamp = messages[i]['timestamp']
        if (not isCommand(text)):
            if (chat["sender"] == messages[i]['body']['sender'] and
chat["recipient"] == messages[i]['body']['recipient'] or
                chat["recipient"] == messages[i]['body']['sender'] and
chat["sender"] == messages[i]['body']['recipient']):
                sender = messages[i]['body']['sender']
                print(tstamp + " from user " + sender + ": " + text)
print()
def clearChat():
    requests.delete(url)
    print("All chats cleared.")
    print()
#Display the graph.
#Number of readable messages (not commands) sent per user
def displayGraphic():
    senderCount = 0
    recipientCount = 0
    r = requests.get(url, headers = {'accept': 'application/json'})
    messages = r.json()
    for message in messages:
        if (not isCommand(message['body']['message'])):
            if (chat["sender"] == message['body']['sender'] and chat["recipient"]
== message['body']['recipient']):
                senderCount += 1
            if (chat["recipient"] == message['body']['sender'] and chat["sender"]
== message['body']['recipient']):
                recipientCount += 1
    x = [chat["sender"], chat["recipient"]]
    y = [senderCount, recipientCount]
    plt.bar(x, y)
    plt.xlabel("Username")
    plt.ylabel("Number\nof\nreadable\nmessages\nsent", rotation=0, labelpad=40)
    plt.tight_layout()
    plt.show()
#Main
start()
while(True):
    sendMessage()
    if (chat["message"] == ":quit"):
        print()
        print("Quitting...")
        print("Chat ended.")
        displayGraphic()
        break
    elif (chat["message"] == ":clear"):
        print()
        clearChat()
    elif (chat["message"] == ":update"):
        print()
        getMessages()
