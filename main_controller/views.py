from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .client import client
from time import sleep
import json

# Global variables
port = 8001
server = "0.0.0.0"

# Pages
def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def information(request):
    return render(request, 'information.html')

def settings(request):
    return render(request, 'settings.html')

# Robot movement
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

# Camera movement
def camera_left(request):
    client("camera_left", server, port)
    sleep(1)
    return HttpResponse("")

def camera_right(request):
    client("camera_right", server, port)
    sleep(1)
    return HttpResponse("")

def camera_up(request):
    client("camera_up", server, port)
    sleep(1)
    return HttpResponse("")

def camera_down(request):
    client("camera_down", server, port)
    sleep(1)
    return HttpResponse("")

def camera(request):
    # start_video_server()   # I accidentally broke the camera
    print("Opening camera..")
    return HttpResponse("")

# Robot features
def sound(request):
    print("Playing sound..")
    client("alarm_sound", server, port)
    return HttpResponse("")

def shutdown(request):
    client("over_sound", server, port)
    return HttpResponse("")

@csrf_exempt
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
            print(f"Error: {e}")

    return HttpResponse("")

@csrf_exempt
def sendmessage(request):
    if request.method == 'POST':
        message = request.body.decode('utf-8')
        print("Received message:", message)
        client("word" + message, server, port)
        return HttpResponse("")

# Ensure the server is listening when the Django app starts
if __name__ == "__main__":
    socket_thread.start()
