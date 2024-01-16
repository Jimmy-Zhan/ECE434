#!/usr/bin/env python3
import gpiod
import sys
import smbus
import time
from flask import Flask, render_template, request


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
    


app = Flask(__name__)
@app.route("/")
def index():
        # Read Sensors Status
        global board
        global current_x,current_y
        current_x,current_y=int(size/2),int(size/2)
        board = [[0 for _ in range(size)] for _ in range(size)]
        print('etch-a-sketc')
        printpic(board,size)
        print() 
        templateData = {
            #   'title' : 'Control etch-a-sketch'
              
        }
        return render_template('etch_a_sketch.html', **templateData)

@app.route("/<action>")
def action(action):
        global board
        global current_x,current_y
        
        if action =="up" and current_y > 0:
            current_y -= 1
        elif action == "down"  and current_y < size - 1:
            current_y += 1
        elif action =="left" and current_x > 0:
            current_x -= 1
        elif action =="right" and current_x < size - 1:
            current_x += 1
            
        board[current_y][current_x] = 1
        printpic(board,size)

        templateData = {
        # 'title' : 'Control etch-a-sketch'
        }
        return render_template('etch_a_sketch.html', **templateData)


bus = smbus.SMBus(2)
matrix = 0x70
size = 8
bus.write_byte_data(matrix, 0x21,0)
bus.write_byte_data(matrix, 0x81,0)
bus.write_byte_data(matrix, 0xe7,0)








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
    
    

    

     
