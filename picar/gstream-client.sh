#!/bin/bash

sudo pkill -9 gst
gst-launch-1.0 -e -v udpsrc port=5000 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false &
ssh -X pi@$1 /home/pi/rccar.py
sudo pkill -9 gst
