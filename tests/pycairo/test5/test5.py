# import gtk
import gi
gi.require_version('Gtk', '2.0')
from gi.repository import Gtk as gtk
import math

class PyApp(gtk.Window):

    def __init__(self):
        super(PyApp, self).__init__()

        self.set_title("Basic shapes using Cairo")
        self.set_size_request(400, 250)
        # self.set_position(gtk.WIN_POS_CENTER)

        self.connect("destroy", gtk.main_quit)

        darea = gtk.DrawingArea()
        darea.connect("expose-event", self.expose)

        self.add(darea)
        self.show_all()

    def expose(self, widget, event):
        cr = widget.window.cairo_create()

        cr.set_line_width(2)
        cr.set_source_rgb(0,0,1)
        cr.rectangle(10,10,100,100)
        cr.stroke()

        cr.set_source_rgb(1,0,0)
        cr.rectangle(10,125,100,100)
        cr.stroke()

        cr.set_source_rgb(0,1,0)
        cr.rectangle(125,10,100,100)
        cr.fill()

        cr.set_source_rgb(0.5,0.6,0.7)
        cr.rectangle(125,125,100,100)
        cr.fill()

        cr.arc(300, 50, 50,0, 2*math.pi)
        cr.set_source_rgb(0.2,0.2,0.2)
        cr.fill()

        cr.arc(300, 200, 50, math.pi,0)
        cr.set_source_rgb(0.1,0.1,0.1)
        cr.stroke()

        cr.move_to(50,240)
        cr.show_text("Hello PyGTK")
        cr.move_to(150,240)
        cr.line_to(400,240)
        cr.stroke()

PyApp()
gtk.main()
