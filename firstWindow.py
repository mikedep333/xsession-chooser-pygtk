#!/usr/bin/env python
import os
import xsessionLauncher

from gi.repository import Gtk

gladefile = os.path.join(os.path.dirname(__file__), "xsession-chooser.glade")


class firstWindow(object):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladefile)
        self.firstWin = self.builder.get_object("firstWindow")
        self.filechooser = self.builder.get_object("filechooserwidget")
       # self.filechooser.set_current_folder("/usr/share/xsessions")
        self.mainhandlers = {
            "on_cancel_clicked": Gtk.main_quit,
            "on_cancelBtn_clicked": Gtk.main_quit,
            "on_firstWindow_delete_event": Gtk.main_quit,
            "on_execute": self.launch,
        }
        self.builder.connect_signals(self.mainhandlers)
        self.firstWin.show_all()
        Gtk.main()

    def launch(self, filechooser):
        print(filechooser.get_filename())
        xsessionLauncher.launch(filechooser.get_filename())
