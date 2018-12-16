import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from PIL import Image
from questions import *
from sympy import *
from experiment_file import *

class Quests(Gtk.Grid):
    def __init__(self, parent):
        self.parent = parent
        Gtk.Grid.__init__(self)
        self.problems = Questions()
        self.solved = -1
        self.correct = 0

        blank_image = Image.new("RGB", (400, 200), '#ffffff')
        blank_image.save('blank.png')
        self.lbl = Gtk.Label("0/0")
        self.quest_image = Gtk.Image()
        self.quest_image.set_from_file("blank.png")
        self.ans = Gtk.Entry()
        self.hint_btn = Gtk.Button(label='Hint')
        self.video = Gtk.Label('Video Help')
        self.submit_btn = Gtk.Button(label='Start')

        self.attach(self.lbl, 0, 0, 2, 1)
        self.attach(self.quest_image, 0, 1, 2, 1)
        self.attach(self.ans, 0, 2, 2, 1)
        self.attach(self.hint_btn, 0, 3, 1, 1)
        self.attach(self.video, 1, 3, 1, 1)
        self.attach(self.submit_btn, 0, 4, 2, 1)

        self.submit_btn.connect("clicked", self.submit)

    def submit(self, widget):
        if self.solved >= 0:
            mal = str_to_list_of_factors(self.ans.get_text())
            mql = list_of_factors(factor_list(self.problems.ans[self.solved - 1]))
            if compare_factors(mal,mql ):
                print("Correct")
                self.correct += 1
            else:
                print(self.problems.ans[self.solved - 1])
            self.quest_image.set_from_file(self.problems.images[self.solved])
            self.ans.set_text("")
            self.solved += 1
            self.lbl.set_text(str(self.correct)+ "/" + str(self.solved))

        if self.solved < 0:
            self.submit_btn.set_label("Submit")
            self.solved += 1
            self.quest_image.set_from_file(self.problems.images[0])





        # print("Solved = " + str(self.solved))
