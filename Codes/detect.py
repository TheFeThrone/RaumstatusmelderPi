import RPi.GPIO as GPIO
import time
import requests
from helpers.file_utils import load_json_file, write_status_to_file


class MotionDetector:
    def __init__(self, config):
        self.config = config
        self.WEB_URL = f"http://{config['host']}:{config['port']}/{config['get']}"
        self.status_file_path = "../config/status.json"
        self.last_detection_time = 0

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(config['SENSOR_PIN'], GPIO.IN)

    def printTime(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        print("Movement detected at", current_time)

    def sendHTTPRequest(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("HTTP request sent successfully")
        except requests.exceptions.RequestException as e:
            print("Error sending HTTP request:", e)

    def motionDetected(self, iSensorPin):
        self.printTime()
        self.last_detection_time = time.time()
        self.sendHTTPRequest(self.WEB_URL)
        write_status_to_file(self.status_file_path, True, "Room is Open")
        time.sleep(self.config['sleep_interval'])

    def setupMotionDetection(self):
        try:
            GPIO.add_event_detect(self.config['SENSOR_PIN'], GPIO.RISING, callback=self.motionDetected)
            while True:
                current_time = time.time()
                if current_time - self.last_detection_time > self.config['detection_interval']:
                    write_status_to_file(self.status_file_path, False, "Room is Closed")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Quit")
            GPIO.cleanup()

if __name__ == "__main__":
    config = load_json_file("../config/config.json")
    detector = MotionDetector(config)
    detector.setupMotionDetection()
