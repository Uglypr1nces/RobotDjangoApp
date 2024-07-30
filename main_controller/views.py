from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .python_robotcontroller.server.client import RobotClient
from time import sleep
import threading
import json

# Global variables
port = 8001
server = "0.0.0.0"

RobotClient = RobotClient(server, port)

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
    RobotClient.send_message("forward")
    return HttpResponse("")

def backward(request):
    RobotClient.send_message("backward")
    return HttpResponse("")

def left(request):
    RobotClient.send_message("left")
    return HttpResponse("")

def right(request):
    RobotClient.send_message("right")
    return HttpResponse("")

# Camera movement
def camera_left(request):
    RobotClient.send_message("camera_left")
    sleep(1)
    return HttpResponse("")

def camera_right(request):
    RobotClient.send_message("camera_right")
    sleep(1)
    return HttpResponse("")

def camera_up(request):
    RobotClient.send_message("camera_up")
    sleep(1)
    return HttpResponse("")

def camera_down(request):
    RobotClient.send_message("camera_down")
    sleep(1)
    return HttpResponse("")

def camera(request):
    # start_video_server()   # I accidentally broke the camera
    print("Opening camera..")
    return HttpResponse("")

# Robot features
def sound(request):
    print("Playing sound..")
    RobotClient.send_message("alarm_sound")
    return HttpResponse("")

def shutdown(request):
    RobotClient.send_message("over_sound")
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
            RobotClient.set_server(server, port)
            RobotClient.connect()
            RobotClient.listen()
            RobotClient.send_message("test")
            context = {
                'Status': 'Connected to the robot!',
            }
        except Exception as e:
            print(f"Error: {e}")

    return render(request, 'settings.html', context)

@csrf_exempt
def send_command(request):
    if request.method == 'POST':
        message = request.body.decode('utf-8')
        print("Received message:", message)
        RobotClient.send_message("word" + message)
        return HttpResponse("")


