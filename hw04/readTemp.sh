#!/usr/bin/env bash
I2CPATH='/sys/class/i2c-adapter/i2c-2'
TEMP1INPUT='2-0048/hwmon/hwmon0'
cat ${I2CPATH}/${TEMP1INPUT}/temp1_input
