import discord
import random
import time 
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


port = os.environ['PORT']
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("I'm alive".encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self,message):
    # Check if the message is from the specified server and user
        if (message.guild and message.guild.id in [1236380949663711313,1246083692376625216]) and (message.author.id == 1150448986264698980):
            print(f'Message received user {message.author.name}: {message.content}')
            for i in range(1):
                print(type(message.components[0].children[i]))
                if message.components[0].children[i].label == "Enter":
                    time.sleep(random.randint(5,10))
                    await message.components[0].children[i].click()
            #await message.components[0].children[0].click()

client = MyClient()
client.run(os.environ['TOKEN'])
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
