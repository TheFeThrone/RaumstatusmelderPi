# RaumstatusmelderPi

For now this is only a local website that shows if the room is occupied or not.  
The motion detector detects every 5 seconds if there is a movement
- if there is movement, edits the status.json and requests the server.
- if there was no movement for 60 seconds it edits the status.json and request the server

## Required Hardware

1. [Raspberry Pi ZeroW](https://www.berrybase.de/raspberry-pi-zero-w)
 - With or without GPIO header
   - If without then buy a [GPIO header](https://www.berrybase.de/40-pin-gpio-header-fuer-raspberry-pi-farbig-kodiert-simple-version) too (You will have to solder it)
3. Motion detector: [PIR HC-SR501](https://www.berrybase.de/hc-sr501-pir-sensor-infrarot-bewegungsmelder)
4. [F/F Jumper Wires](https://www.berrybase.de/40pin-jumper/dupont-kabel-female-female-trennbar)
5. MicroSD Card of any size

## Pi Installation

1. Connect the detector to the right Pin numbers

- The Out-Connection has to be connected to a GPIO pin
- You can find a perfect depiction of the numbering [here](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZero_1.pdf)
- I chose BOARD numberings: In 2, Out 7, Ground 6
- ![https://projects-static.raspberrypi.org/projects/physical-computing/248971027a596f3437da45bafd2bd8a8cc35cb95/en/images/pir_wiring.png](https://github.com/TheFeThrone/RaumstatusmelderPi/assets/117587855/fc99d7d4-f4c3-4f44-9346-b87cfa9e92f7)

2. Download [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to get started

- OS: Any Raspbian will do it. I used Raspbian 32Bit (Dont try Lite.. you will not be able to find whats missing as requirement)
- Storage: Choose your MicroSD Card
- Settings: Here you can set the hostname, username and password by witch you can ssh into your pi and also set your first wireless connection

3. Install pip and requirements

- `sudo apt-get install -y pip`
- `pip -r requirements.text -y`

## How to run

### Configuration

In `config/config.json` you can configure everythin you need. 
```json
{
  "host": "YOUR HOSTNAME", 
  "port": THE PORT YOU WANT TO RUN THE SERVER FROM,
  "sleep_interval": INTERVAL IN WHICH THE DETECTOR WILL LOOK FOR MOVEMENT,
  "detection_interval": INTERVAL IN WHICH ABSCENCE CAN BE DECIDED: if nothing has moved during this time, the room is empty,
  "get": "SUBDIRECTORY THAT THE DETECTOR IS GOING TO REQUEST",
  "status": "SUBDIRECTORY IN WHICH THE status.json WILL BE MIRRORED IN",
  "SENSOR_PIN": SENSOR PIN NUMBER DEPENDNG ON THE MODE YOU CHOSE (Default = BOARD)
}
```

### Start

~~The code to be run is in the `Codes` directory~~
~~You have to run (best with `screen`) both `detect.py` and `server.py` over python~~
> I will add an automation to this soon
- You just have to launch the `launch.py` file to have it all running

## Useful Tutorials

[How to solder header pins to the Raspberry Pi Zero (W)](https://www.youtube.com/watch?v=UDdbaMk39tM)  
[Detecting motion with a Raspberry Pi Zero W ](https://www.youtube.com/watch?v=pSSn4u3xGIg)
