#Runs on windows 10, Python 3.8.5

import os

import loader
import processor

def main():
    print(
        processor.cfg["a"]
    )
    os.system('pause')

if __name__ == '__main__':
    main()
