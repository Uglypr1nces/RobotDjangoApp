from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .client import client
from .views import *
import json

# Global variables
port = 8001
server = "0.0.0.0"

#pages
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def information(request):
    return render(request, 'information.html')

def settings(request):
    return render(request, 'settings.html')

#robot movement
def forward(request):
    client("forward", server, port)
    return HttpResponse("")
def backward(request):
    client("backward", server, port)
    return HttpResponse("")
def left(request):
    client("left", server, port)
    return HttpResponse("")
def right(request):
    client("right", server, port)
    return HttpResponse("")
def right(request):
    client("right", server, port)
    return HttpResponse("")

#camera movement
def camera_left(request):
    client("camera_left", server, port)
    return HttpResponse("")

def camera_right(request):
    client("camera_right", server, port)
    return HttpResponse("")

def camera_up(request):
    client("camera_up", server, port)
    return HttpResponse("")

def camera_down(request):
    client("camera_down", server, port)
    return HttpResponse("")

def camera(request):
    #start_video_server()   # I accidently broke the camera
    print("Opening camera..")
    return HttpResponse("")

#robot features

def sound(request):
    print("Playing sound..")
    client("alarm_sound", server, port)
    return HttpResponse("")

def shutdown(request):
    client("over_sound", server, port)
    return HttpResponse("")

def savesettings(request):
    global port
    global server

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        server = data.get('robotIP')
        port = int(data.get('port'))
        print("Saving settings... Robot IP:", server, "Port:", port)
        try:
            client("test", server, port)
        except Exception as e:
            print(f"Cause of error: {e}")

    return HttpResponse("")

def sendmessage(request):
    if request.method == 'POST':
        message = request.body.decode('utf-8')
        print("Received message:", message)
        client("word"+message, server, port)
        return HttpResponse("")
