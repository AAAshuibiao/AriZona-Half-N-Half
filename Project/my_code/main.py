#Runs on windows 10, Python 3.8.5

from os import system as command

import loader
import processor
import actuator

import time


def main():
    if actuator.ready:
        actuator.begin()
    time.sleep(2)
    #command('pause')


if __name__ == '__main__':
    main()
