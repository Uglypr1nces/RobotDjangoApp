import pygame
import sys
import tkinter as tk
from tkinter import messagebox
from .server.client import *
import time

def tkintermessage(message):
    root = tk.Tk()
    tk.messagebox.showinfo("Message", message)
    root.destroy()
    exit()

def send(message, server, port):
    try:
        client(message, server, port)
    except Exception as e:
        print(f"Cause of error: {e}")
        tkintermessage("Server is not running")

def start_robot(server, port):
    pygame.init()

    # Initialize the joystick
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        tkintermessage("No joystick/controller found.")
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    screen = pygame.display.set_mode([500, 500])

    FPS = 60
    fpsClock = pygame.time.Clock()
    running = True

    player_image = pygame.image.load('main_controller/python_robotcontroller/content/player1.png')
    player_rect = player_image.get_rect()

    player_1_x = 100
    player_1_y = 100

    player_speed = 2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    send("alarm_sound",server, port)
                

        # Get joystick input
        left_thumbstick_x = joystick.get_axis(0)
        left_thumbstick_y = joystick.get_axis(1)

        right_thumbstick_x = joystick.get_axis(2)
        right_thumbstick_y = joystick.get_axis(3)

        # Adjust player position based on joystick input
        player_1_x += int(left_thumbstick_x * player_speed)
        player_1_y += int(left_thumbstick_y * player_speed)

        if right_thumbstick_x < -0.5:
            send("camera_left", server, port)
            
        elif right_thumbstick_x > 0.5:
            send("camera_right", server, port)
            
        if right_thumbstick_y < -0.5:
            send("camera_up", server, port)
            
        elif right_thumbstick_y > 0.5:
            send("camera_down", server, port)
            

        if left_thumbstick_y < -0.5:
            player_image = pygame.image.load('main_controller/static/rbot_up.png')
            send("forward", server, port)
            
        elif left_thumbstick_y > 0.5:
            player_image = pygame.image.load('main_controller/static/rbot_down.png')
            send("backward", server, port)
            

        if left_thumbstick_x < -0.5:
            player_image = pygame.image.load('main_controller/static/rbot_left.png')
            send("left", server, port)
            
        elif left_thumbstick_x > 0.5:
            player_image = pygame.image.load('main_controller/static/rbot_right.png')
            send("right", server, port)
            

        player_rect.topleft = (player_1_x, player_1_y)

        screen.fill((255, 255, 255))

        screen.blit(player_image, player_rect)

        pygame.display.update()
        fpsClock.tick(FPS)

    pygame.quit()
    client("over_sound", server, port)
    exit()