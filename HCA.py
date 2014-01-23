#-*- coding: utf-8 -*-
# HCAlos.py
from gi.repository import Gtk
import serial
import numpy


class HCA(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("HCA.xml")
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('movement')
        self.locations=['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2','/dev/ttyACM3',  
                   '/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']
                
    def obj(self, name):
        
        return self.builder.get_object(name)    
    
    def run(self):
        
        try:
            self.window.show_all()
            Gtk.main()
        except KeyboardInterrupt:
            pass 
            
    def quit(self):
        Gtk.main_quit()



    def on_movement_delete_event(self, *args):
        self.quit()

# Verbindung yum Arduino herstellen
    def on_savetoard_clicked(self, send, *args): 
            print ("click") 
            for device in self.locations:    
                try:    
                    print "Trying...",device  
                    arduino = serial.Serial(device, 9600)   
                    print arduino
                    break  
                except:    
                    print "Failed to connect on",device
            
                    return device
            arduino.write(self.mempos)
         
# Positionsslider

    def on_hscalex_value_changed(self, *args):
        posx = self.builder.get_object('hscalex').get_value()
        
        return posx

    def on_hscaley_value_changed(self, *args):
        posy = self.builder.get_object('hscaley').get_value()
        
        return posy
        
    def on_hscalez_value_changed(self, *args):
        posz = self.builder.get_object('hscalez').get_value()
        
        return posz

    def on_savetopos_clicked(self,button, *args):
        posx = self.on_hscalex_value_changed()
        posy = self.on_hscaley_value_changed()
        posz = self.on_hscalez_value_changed()
        self.mempos = [posx, posy, posz]
        array = self.mempos
        return array
       
    def on_Position1_toggled(self,button, *args):
            
            if button.get_active():
                posarray = "pos1"
                return posarray    
                            
    def on_Position2_toggled(self,button, *args):
            
            if button.get_active():
                posarray = "pos2"
                return posarray
            
    def posArray(self, posarray, array):
         
            if posarray == "pos1":
                memarray = [array] 
                print "mem1", memarray 
            
            if posarray == "pos2":
                print "mem2"
                memarray = [1, array] 
                
                print memarray    
    
if __name__ == '__main__':
    app = HCA()
    app.run()
    
