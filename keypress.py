import keyboard as k
import time as t

i = 0
while not k.is_pressed ('q'):
    print ('check')
    if k.is_pressed ('down arrow'):
        print ('Hello!')
        i+=1
