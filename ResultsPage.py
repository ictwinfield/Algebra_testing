import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Results_Page(Gtk.Box):
    def __init__(self, parent):
        self.parent = parent
        Gtk.Box.__init__(self, orientation="vertical")

        self.lbl1 = Gtk.Label("Your Score Was")
        self.lbl2 = Gtk.Label(str(self.parent.quests.correct) + ' out of 5')
        self.btn = Gtk.Button(label="New Set")

        self.pack_start(self.lbl1, True, True, 0)
        self.pack_start(self.lbl2, True, True, 0)
        self.pack_start(self.btn, True, True, 0)
