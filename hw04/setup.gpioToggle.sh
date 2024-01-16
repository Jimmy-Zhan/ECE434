#!/bin/bash
# Set up gpio 7 to read and gpio 3 to write
cd /sys/class/gpio
echo 3 > export
echo 7 > export
echo 10 > export
echo 11 > export
echo 45 > export
echo 44 > export
sudo chmod 777 gpio11/direction
sudo chmod 777 gpio10/direction
sudo chmod 777 gpio44/direction
sudo chmod 777 gpio45/direction

echo in  > gpio11/direction
echo out > gpio10/direction
echo out  > gpio44/direction
echo in > gpio45/direction
