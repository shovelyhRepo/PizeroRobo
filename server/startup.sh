#!/bin/bash
sudo pkill -9 -ef mjpg_streamer
sudo pkill -9 -ef app.py
sudo python3 /home/pi/PiRobo/app.py &
