#!/usr/bin/env python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
from OpenGL.GL import glClearColor, glClear, GL_COLOR_BUFFER_BIT
import os, sys

UI_FILE = "pygtk_gtkglarea.ui"

class GUI:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        gl_area = Gtk.GLArea()
        gl_area.connect('render', self.area_render)
        gl_area.connect('realize', self.area_realize)
        #gl_area.connect('create-context', self.area_context)
        box = self.builder.get_object('box1')
        box.pack_end(gl_area, True, True, 0)

        window = self.builder.get_object('window')
        window.show_all()

    def area_realize (self, gl_area):
        error = gl_area.get_error()
        if error != None:
            print "your graphics card is probably too old : ", error
        else:
            print gl_area, "realize... fine so far"

    def area_context(self, gl_area):
        # not needed except for special instances, read the docs
        c = gl_area.get_context()
        print c , "context"
        return c

    def area_render(self, area, context):
        #print gl_area
        #print gl_context
        glClearColor (0.5, 0.5, 0.5, 1.0)
        glClear (GL_COLOR_BUFFER_BIT)
        # glFlush()
        print "rendering... done"
        return True

    def on_window_destroy(self, window):
        Gtk.main_quit()

def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
