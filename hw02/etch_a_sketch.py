#!/usr/bin/env python3
import gpiod
import sys

CHIP = '1'
CONSUMER = 'getset'
getoffsets = [12, 13, 14, 15] #P8_12,P8_11,P8_16,P8_15
setoffsets =[30, 18, 16, 19] #P9_12,P9_14,P9_15,P9_16
L=12 
R=13
U=14
D=15
def printpic(board,size):
    
    for i in range(size):
        print(str(i)+":" , end = "")

    for i in range(size):
        print()
        print(str(i)+":", end= " ")
        for j in range(size):
            print(board[i][j], end=" ")
    print()

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

print("Hit ^C to stop")


print('etch-a-sketc')
print('size of pic')
size = int(input())

board = [['.' for _ in range(size)] for _ in range(size)]
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
                
            board[current_y][current_x] = 'x'
            printpic(board,size)
        # Button pressed
        


    # while True:
    #     printpic(board,size)

    #     # Get user input
    #     move = input("Move cursor (W/A/S/D), 'Q' to quit, 'R' to erase: ").upper()

    #     if move == 'Q':
    #         break
    #     elif move == 'W' and current_y > 0:
    #         current_y -= 1
    #     elif move == 'S' and current_y < size - 1:
    #         current_y += 1
    #     elif move == 'A' and current_x > 0:
    #         current_x -= 1
    #     elif move == 'D' and current_x < size - 1:
    #         current_x += 1

    #     # Mark the current position
    #     board[current_y][current_x] = 'x'
    #     if move =='R':
    #         board = [['.' for _ in range(size)] for _ in range(size)]
            
