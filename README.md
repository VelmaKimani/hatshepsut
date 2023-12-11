# Commandline chat app in Python

## Intro

Hi Guys this repo consist of a source code for a simple CLI chatting app made using sockets in Python


To get started just clone the repository using  _git_  command or pressing download button option at the right side of the repository

**Cloning**

$ git clone 
$ cd Commandline-chatting-system-python
Commandline-chatting-system-python $ tree
.
├── client.py
├── README.md
└── server.py

0 directories, 3 files

This repo consist of two  **Python scripts**  named  _client.py_  and  _server.py_as I have explained on the tutorial, whereby  **server.py**  will serve as our server node and  **client.py**  will serve as our client node.

## Running our script

**Note**

You should start running the server script before running the client script because if you do otherwise, the client will exit immediately as result of not finding a server node to connect

**running server.py**

$ python server.py

**running client.py**

$ python client.py
Enter server_ip: 127.0.0.1
Finding connection
Connection successful made to the server

**Note**

If the server script is run on the different pc or laptop enter your server pubic IP on client  **enter ip**  prompt

## Explore it

Now your script should be running and able to communicate with each other, you try writing message to any of those script and then press enter to send the message to the another node whether it's server or client.