import serial
import time
from Tkinter import *
import struct


locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3',  
    '/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']

for device in locations:    
        try:    
            print "Trying...",device  
            arduino = serial.Serial(device, 9600)   
            
            break  
        except:    
            print "Failed to connect on",device  

def print_value():
    try:
        print (w1.get())
        valx = w1.get()
        arduino.write('251')
        time.sleep(1.5)
        arduino.write(str(valx))
        time.sleep(1.5)
        arduino.flush()
        
        print (w2.get())
        valy = w2.get()
        arduino.write('252')
        time.sleep(1.5)
        arduino.write(str(valy))
        time.sleep(1.5)
        arduino.flush()
        
        print (w3.get())
        valz = w3.get()
        arduino.write('253')
        time.sleep(1.5)
        arduino.write(str(valz))
        arduino.flush()
        
        
        
        
    except:
        print "Failed to send"
              
master = Tk() 
w1 = Scale(master, from_=-100, to=100, length=600, tickinterval=8, orient=HORIZONTAL)
w1.set(5)
w1.pack()
w2 = Scale(master, from_=0, to=250, length=100, tickinterval=10,)
w2.set(100)
w2.pack(padx=5, pady=20, side=LEFT)
w3 = Scale(master, from_=0, to=250, length=100, tickinterval=10)
w3.set(100)
w3.pack(padx=5, pady=20, side=LEFT)
Button(master, text='Send', command= print_value).pack(padx=5, pady=20, side=LEFT)


mainloop()

