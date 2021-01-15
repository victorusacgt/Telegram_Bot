# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 00:07:13 2021

@author: victorusacgt
"""

import sys
import subprocess
import time
import telepot
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

#function DHT11
def dht():
    return subprocess.check_output('python DHT11.py', shell=True)

#text function
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command =='/temp':
       bot.sendMessage(chat_id, dht()) 


bot = telepot.Bot('bot_code') #telegram token
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()