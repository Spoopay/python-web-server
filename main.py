import socket
import threading
import json
from wsgiref.simple_server import server_version

PORT = 25568
FORMAT = 'utf-8'
SERVER = 'play.spoopaydev.com'

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def getUserMessage():
    connected = True
    while connected:
        user_message = encodeToJson(input(), username)
        send(user_message)

def encodeToJson(message, username):
    json_data = {}
    json_data["username"] = username
    json_data["message"] = message
    return json.dumps(json_data)

def decodeFromJson(data):
    if (data == "DISCONNECTED"):
        return False
    return json.loads(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    username = input("Input an username: ")
    client.connect((SERVER, PORT))
    print(f"Welcome to the server {username}!")
    connected = True
    thread = threading.Thread(target=getUserMessage, args=())
    thread.start()
    while connected:
        server_msg = decodeFromJson(client.recv(1024).decode())
        if (server_msg == False):
            break
        if (server_msg['username'] != username):
            print(f"[{server_msg['username']}] {server_msg['message']}")