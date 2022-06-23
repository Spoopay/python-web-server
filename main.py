import socket
import json

PORT = 25568
FORMAT = 'utf-8'
SERVER = 'play.spoopaydev.com'

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

def encodeToJson(message, username):
    json_data = {}
    json_data["username"] = username
    json_data["message"] = message
    return json.dumps(json_data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    username = input("Input an username: ")
    client.connect((SERVER, PORT))
    print(f"Welcome to the server {username}!")
    connected = True
    while connected:
        user_message = encodeToJson(input(), username)
        send(user_message)