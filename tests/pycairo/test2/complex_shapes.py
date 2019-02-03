#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This code example draws another
three shapes in PyCairo.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: April 2016
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import cairo


class cv(object):
    
    points = ( 
        ( 0, 85 ), 
        ( 75, 75 ), 
        ( 100, 10 ), 
        ( 125, 75 ), 
        ( 200, 85 ),
        ( 150, 125 ), 
        ( 160, 190 ),
        ( 100, 150 ), 
        ( 40, 190 ),
        ( 50, 125 ),
        ( 0, 85 )
    )


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Complex shapes")
        self.resize(460, 240)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, wid, cr):

        cr.set_source_rgb(0.6, 0.6, 0.6)
        cr.set_line_width(1)

        for i in range(10):
            cr.line_to(cv.points[i][0], cv.points[i][1])

        cr.fill()

        cr.move_to(240, 40)
        cr.line_to(240, 160)
        cr.line_to(350, 160)
        cr.fill()

        cr.move_to(380, 40)
        cr.line_to(380, 160)
        cr.line_to(450, 160)
        cr.curve_to(440, 155, 380, 145, 380, 40)
        cr.fill()
        
        #MOD
        
        cr.set_source_rgb(0.2, 0.23, 0.9)
        cr.rectangle(10, 15, 90, 60)
        cr.fill()
        
        cr.set_source_rgb(0.9, 0.1, 0.1)
        cr.rectangle(130, 15, 90, 60)
        cr.fill()

        cr.set_source_rgb(0.4, 0.9, 0.4)
        cr.rectangle(250, 15, 90, 60)
        cr.fill()
        
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
