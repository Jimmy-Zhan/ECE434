#!/usr/bin/env python3
import gpiod
import sys
import smbus
import time

bus = smbus.SMBus(2)
matrix = 0x70
size = 8
bus.write_byte_data(matrix, 0x21,0)
bus.write_byte_data(matrix, 0x81,0)
bus.write_byte_data(matrix, 0xe7,0)

CHIP = '1'
CONSUMER = 'getset'

eQEP1 = '1'
eQEP2 = '2'
COUNTPATH1 = '/dev/bone/counter/'+eQEP1+'/count0'
COUNTPATH2 = '/dev/bone/counter/'+eQEP2+'/count0'
ms = 100
maxCount = 1000000
getoffsets = [12, 13, 14, 15] #P8_12,P8_11,P8_16,P8_15
setoffsets =[30, 18, 16, 19] #P9_12,P9_14,P9_15,P9_16
L=12 
R=13
U=14
D=15

LEDMatrix=[0x00 for _ in range(16)]
def printpic(board,size):
    
    for i in range(size):
        print(str(i)+":" , end = "")

    for i in range(size):
        print()
        print(str(i)+":", end= " ")
        for j in range(size):
            print(board[i][j], end=" ")
    print()
    
    for i in range(size): 
        num = 0x0
        for j in range(size):
            num+=board[i][j] * pow(2, j)
        LEDMatrix[2*i] = num 
    bus.write_i2c_block_data(matrix,0,LEDMatrix)
    

def checkButton(event):
    if event.type == gpiod.LineEvent.RISING_EDGE:
        button = event.source.offset()

        
        if button ==D and current_y > 0:
            current_y -= 1
        elif button == U  and current_y < size - 1:
            current_y += 1
        elif button ==L and current_x > 0:
            current_x -= 1
        elif button ==R and current_x < size - 1:
            current_x += 1
            
        board[current_y][current_x] = 'x'
        printpic(board,size)




chip = gpiod.Chip(CHIP)

getlines = chip.get_lines(getoffsets)
getlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_EV_BOTH_EDGES)

setlines = chip.get_lines(setoffsets)
setlines.request(consumer=CONSUMER, type=gpiod.LINE_REQ_DIR_OUT)

f1 = open(COUNTPATH1+'/count','r')
f2 = open(COUNTPATH2+'/count','r')
olddata1 = -1
olddata2 = -1
#print('size of pic')
#size = int(input())

#board = [['.' for _ in range(size)] for _ in range(size)]
board = [[0 for _ in range(size)] for _ in range(size)]
print("Hit ^C to stop")
print('etch-a-sketc')
printpic(board,size)
print()

current_x,current_y=int(size/2),int(size/2)
    
    
while True:
    ev_lines = getlines.event_wait(sec=1)
    
    if ev_lines:
        vals = getlines.get_values()
        setlines.set_values(vals)
        for line in ev_lines:
            event = line.event_read()
            if event.type == gpiod.LineEvent.RISING_EDGE:
                button = event.source.offset()

            
            if button ==D and current_y > 0:
                current_y -= 1
            elif button == U  and current_y < size - 1:
                current_y += 1
            elif button ==L and current_x > 0:
                current_x -= 1
            elif button ==R and current_x < size - 1:
                current_x += 1
                
            board[current_y][current_x] = 1
            printpic(board,size)
    # data1 = f1.read()[:1]
    # data2 = f2.read()[:1]
    # if data1 != olddata1 or data2 != olddata2
    #     if data1 > olddata1 and current_y > 0:
    #         current_y -= 1
    #     elif data1 < olddata1   and current_y < size - 1:
    #         current_y += 1
    #     elif data2>olddata2  and current_x > 0:
    #         current_x -= 1
    #     elif data2<olddata2  and current_x < size - 1:
    #         current_x += 1
    
    # olddata1 = data1
    # olddata2 = data2
        
    board[current_y][current_x] = 1
    printpic(board,size)
     
