// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio1_addr;
    volatile void *gpio0_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    unsigned int reg;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio0_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);

    gpio_oe_addr           = gpio0_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio0_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio0_addr + GPIO_CLEARDATAOUT;

    if(gpio0_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio0_addr);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);

    // Set GPIO1_13  to be an output pin
    reg = *gpio_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~GPIO_13;       // Set USR3 bit to 0
    *gpio_oe_addr = reg;
    printf("GPIO1 configuration: %X\n", reg);

    // Set GPIO0_10 to be an output pin
    reg = *gpio_oe_addr;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~GPIO_10;       // Set USR3 bit to 0
    *gpio_oe_addr = reg;


 


    while(keepgoing) {
        // printf("ON\n");
        *gpio_setdataout_addr = GPIO_10;
//        usleep(250000);
        // printf("OFF\n");
        *gpio_cleardataout_addr = GPIO_10;
  //      usleep(250000);
    }

    munmap((void *)gpio0_addr, GPIO1_SIZE);
    close(fd);
    return 0;
}
