#!/usr/bin/env bash
COUNTPATHO='/sys/bus/counter/devices/counter2/count0'
COUNTPATHT='/sys/bus/counter/devices/counter1/count0'
echo "100000" >${COUNTPATHO}/ceiling
echo  "1" >${COUNTPATHO}/enable
echo  "100000" >${COUNTPATHT}/ceiling
echo  "1" >${COUNTPATHT}/enable
