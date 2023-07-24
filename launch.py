import os
from threading import Thread

def start_server():
    os.system("python ./Codes/server.py")

def start_detection():
    os.system("python ./Codes/detect.py")

Thread(target=start_server).start()
Thread(target=start_detection).start()
