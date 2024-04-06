import os

import scratchattach as scratch3

from chatgpt import chatgpt
from server import server

server()


session = scratch3.Session(os.environ['E'], username=os.environ['U'])
conn = session.connect_cloud(os.environ['P'])
client = scratch3.CloudRequests(conn)



@client.request
def chat(argument1):
    print("!")
    return scratch3.Encoding.encode(chatgpt(argument1, "A friendly assistant"))
    

@client.event
def on_ready():
    print("Request handler is ready")


client.run()
