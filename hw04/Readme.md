etch-a-sketchb5.py sets a server that controls the etch-a-sketch

readTemp.sh is the shell script for reading the temp via kernal

gpioThru toggle reads p8-11 and writ to p8-12, P8-31 to P8-32

The mmap can toggle gpio around 50-70MHz, the frequency is not very stable

playmovie.sh is a shell script that play a test movie on lcd display



# hw04 grading

| Points      | Description | |
| ----------- | ----------- | - |
|  1/2 | Memory map | ReadMe didn't tell me where to find it.
|  4/4 | mmap() | 70MHz seems too fast.
|  4/4 | i2c via Kernel
|  5/5 | Etch-a-Sketch via flask
|  5/5 | LCD display
|      | Extras
| 19/20 | **Total**

*My comments are in italics. --may*
