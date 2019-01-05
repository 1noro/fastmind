#!/usr/bin/python3
#GTK test 1
#by boot1110001

### IMPORTS ####################################################################
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

### EXEC #######################################################################
win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
