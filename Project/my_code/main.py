#Runs on windows 10, Python 3.8.5

from os import system as command

import loader
import processor
import actuator

from actuator.proceed import begin


def main():
    begin()
    command('pause')


if __name__ == '__main__':
    main()
