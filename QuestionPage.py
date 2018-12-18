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
        self.problem = 0
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
        res = widget.get_property("label")
        if res == "Start":
            self.submit_btn.set_label("Submit")
            self.quest_image.set_from_file(self.problems.images[self.problem])
        else:
            mal = str_to_list_of_factors(self.ans.get_text())
            mql = list_of_factors(factor_list(self.problems.ans[self.problem]))
            if compare_factors(mal, mql):
                print("Correct")
                self.correct += 1
            else:
                print(self.problems.ans[self.problem])
            if self.problem < 4:
                self.problem += 1
                self.ans.set_text("")
                self.quest_image.set_from_file(self.problems.images[self.problem])
                self.lbl.set_text(str(self.correct)+ "/" + str(self.problem))
            else:
                self.problem += 1
                self.submit_btn.set_sensitive(False)
                self.parent.set_page_complete(self.parent.quests, True)
                self.parent.review.lbl2.set_text(str(self.correct)+ "/" + str(self.problem))
        
