#!/usr/bin/python3

import sys
import firstWindow

try:
    from gi.repository import Gtk
except RuntimeError as e:
    print("xsession-chooser-pygtk requires a currently running X server.")
    print(("%s: %r" % (e.__class__.__name__, str(e))))
    sys.exit(1)

firstWindow.firstWindow()
