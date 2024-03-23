from django.shortcuts import render,redirect
from emailsending import views
from django.http import HttpResponse
from .python_robotcontroller.game import *
from django.views.decorators.csrf import csrf_exempt
from .python_robotcontroller.server.client import *
import json
import pygame
import socket

port = 8001
server = "0.0.0.0"

def playsound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(f'{sound}.wav')
    pygame.mixer.music.play()

def index(request):
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')
def information(request):
    return render(request, 'information.html')
def settings(request):
    return render(request, 'settings.html')

def start(request):
    print(f"starting robot at {server}:{port}...")
    if server == "0.0.0.0":
        tkintermessage("please enter a server address in the settings page")
    else:
        start_robot(server,port)
        return HttpResponse("")

def camera(request):
    if server == "0.0.0.0":
        tkintermessage("please enter a server address in the settings page")
    else:
        print("opening camera..")
        return HttpResponse("")

def sound(request):
    if server == "0.0.0.0":
        tkintermessage("please enter a server address in the settings page")
    else:
        print("playing sound..")
        client("alarm_sound", server, port)
        return HttpResponse("")

def shutdown(request):
    if server == "0.0.0.0":
        tkintermessage("please enter a server address in the settings page")
    else:
        print("shutting down robot..")
        client("over_sound",server,port)
        return HttpResponse("")

def savesettings(request):
    global port
    global server

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        server = data.get('robotIP')
        port = int(data.get('port'))
        print("Saving settings... Robot IP:", server, "Port:", port)
        client("test",server,port)

    return HttpResponse("")

def Contact(request):
    return redirect("/Contact")

def sendmessage(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message')
        print("sending message: " + message)
        client("word"+message,server,port)
    return HttpResponse("")