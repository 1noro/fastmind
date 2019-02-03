#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This program shows how to work
with patterns in PyCairo.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: April 2016
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import cairo


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        self.create_surpat()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Patterns")
        self.resize(300, 290)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        

    def create_surpat(self):
        
        sr1 = cairo.ImageSurface.create_from_png("blueweb.png")
        sr2 = cairo.ImageSurface.create_from_png("maple.png")
        sr3 = cairo.ImageSurface.create_from_png("crack.png")
        sr4 = cairo.ImageSurface.create_from_png("chocolate.png")
        
        self.pt1 = cairo.SurfacePattern(sr1)
        self.pt1.set_extend(cairo.EXTEND_REPEAT)
        self.pt2 = cairo.SurfacePattern(sr2)
        self.pt2.set_extend(cairo.EXTEND_REPEAT)
        self.pt3 = cairo.SurfacePattern(sr3)
        self.pt3.set_extend(cairo.EXTEND_REPEAT)
        self.pt4 = cairo.SurfacePattern(sr4)
        self.pt4.set_extend(cairo.EXTEND_REPEAT)        
        
        
    def on_draw(self, wid, cr):

        cr.set_source(self.pt1)
        cr.rectangle(20, 20, 100, 100)
        cr.fill()

        cr.set_source(self.pt2) 
        cr.rectangle(150, 20, 100, 100)
        cr.fill()

        cr.set_source(self.pt3)
        cr.rectangle(20, 140, 100, 100)
        cr.fill()

        cr.set_source(self.pt4)
        cr.rectangle(150, 140, 100, 100)
        cr.fill()
        
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
