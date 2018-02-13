#!/usr/bin/python
# -*- coding: utf-8 -*-
  
from Quartz.CoreGraphics import *
from time import sleep
from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import pyautogui
import sys
import _thread

flag = False

# Keyboard Events
class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        print ('flaf flag')
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def suprisesys():
    value = int(input("How many times?"))
    #i = 0
    print (value)
    #pyautogui.click()
    #for num in range(1,10):
    counter = 0
    while counter <= 100:
        print ("hi")
        counter += 1
        #i += 1
        #pyautogui.click()
        
        # ourEvent = CGEventCreate(None)
        # currentpos = CGEventGetLocation(ourEvent) # Save current mouse position
        # mouseclick(int(currentpos.x),int(currentpos.y))
        #sleep(0.01);
        

# Where the magic begins
def handler(event):
    global flag
    #print ('clicker flag')
    try:
        #print ('clicker flag')
        #NSLog(u"%@", event)
        #print 'keycode: ' + str(event.keyCode())
        if (int(event.keyCode()) == 6): # 6 - Z Key
            flag = not(flag)
            #suprisesys()
            status = 'activated' if flag else 'deactivated'
            print ('clicker ' + status)
            #clicker()
        elif (int(event.keyCode()) == 53): # 53 - ESC Key 
            AppHelper.stopEventLoop()
    except KeyboardInterrupt:
        print ('clicker what?')
        AppHelper.stopEventLoop()
    
# Mouse Events
def mouseEvent(type, posx, posy):  
    theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
    result = CGEventPost(kCGHIDEventTap, theEvent)
    return result
    
def mouseclick(posx,posy):  
    up = mouseEvent(kCGEventLeftMouseDown, posx,posy)  
    down = mouseEvent(kCGEventLeftMouseUp, posx,posy)
    return str(up) + ' ' + str(down)

# the clicker
def clicker():
    global flag
    print ('clicker started')
    while(True):
        if(flag):
            pyautogui.click(clicks=25, interval=0.001)
            sleep(0.001);
            # ourEvent = CGEventCreate(None)
            # currentpos = CGEventGetLocation(ourEvent) # Save current mouse position
            # mouseclick(int(currentpos.x),int(currentpos.y))
            
        
    
#main function
def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()
    
if __name__ == '__main__':
    _thread.start_new_thread(clicker,())
    main()