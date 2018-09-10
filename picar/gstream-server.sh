#!/bin/bash
HOST="192.168.2.59"

raspivid -n -t 0 -rot 180 -w 1280 -h 720 -fps 30 -b 2000000 -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! rtph264pay pt=96 config-interval=5 ! udpsink host=$HOST port=5000 &
