#!/usr/bin/env bash

mplayer -vo fbdev2 -nolirc -framedrop -vf-add scale=320:240 ~/ECE434/test.mov
