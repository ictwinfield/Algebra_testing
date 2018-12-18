import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from QuestionPage import Quests
from ResultsPage import Results_Page


class Tester(Gtk.Assistant):
    def __init__(self):
        Gtk.Assistant.__init__(self)

        # self.set_default_size(600, 500)

        self.intro = Gtk.TextView()
        self.quests = Quests(self)
        self.review = Results_Page(self)

        # Set up TextView
        self.intro.set_editable(False)
        self.intro.get_buffer().set_text("""The steps required:
        * Select what you want to be tested on
        * Select the level of the test
        * If you want a hint on the style of the answer select hint
        * If you want a video tutorial press the video button
        * Put your answer in the text Window
        * You can use python format or latex
        * When you have done a question press submit""")

        # Add the pages
        self.append_page(self.intro)
        self.append_page(self.quests)
        self.append_page(self.review)

        self.set_page_type(self.intro, Gtk.AssistantPageType(1))
        self.set_page_title(self.intro, "Introduction")
        self.set_page_complete(self.intro, True)

        self.set_page_type(self.quests, Gtk.AssistantPageType(4))
        self.set_page_title(self.quests, "Questions")

        self.set_page_type(self.review, Gtk.AssistantPageType(1))
        self.set_page_title(self.review, "Your Results")

        self.connect("cancel", Gtk.main_quit)
        self.connect("close", Gtk.main_quit)


        self.intro.show()
        self.quests.show()
        self.review.show()

ass = Tester()
ass.connect("destroy", Gtk.main_quit)
ass.show_all()
Gtk.main()
