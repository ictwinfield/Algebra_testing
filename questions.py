from sympy import *
from random import *
from PIL import Image

x, y = symbols("x,y")

class Factorise():
    def __init__(self, level, filename):
        self.level = level
        self.fn = filename
        self.quest = ""
        self.ans   = ""


        if self.level == 1:
            alpha1 = str(randint(1, 10))
            s1 = '-' if randint(1,2) == 1 else '+'
            alpha2 = str(randint(1, 10))
            s2 = '-' if randint(1,2) == 1 else '+'
            expr = "(x " + s1 + alpha1 + ")*(x " +s2 + alpha2 + ")"
            self.quest = expand(expr)
            self.ans   = factor(self.quest)
        else:
            alpha1 = str(randint(1, 5))
            s1 = '-' if randint(1,2) == 1 else '+'
            alpha2 = str(randint(1, 5))
            s2 = '-' if randint(1,2) == 1 else '+'
            beta1 = str(randint(2, 5))
            beta2 = str(randint(2, 5))
            expr = "(" + beta1 + "* x " + s1 + alpha1 + ")*(" + beta2 + "* x " +s2 + alpha2 + ")"
            self.quest = expand(expr)
            self.ans   = factor(self.quest)

        preview(self.quest, viewer='file', filename=self.fn, euler=False)

        old_im = Image.open(self.fn)
        old_size = old_im.size
        # new_size = (old_size[0] + 40, old_size[1] + 40)
        new_size = (400, 200)

        new_im = Image.new("RGB", new_size, '#ffffff')
        new_im.paste(old_im, (int((new_size[0]-old_size[0])/2), int((new_size[1]-old_size[1])/2)))

        new_im.save(self.fn)

    def get_question(self):
        return self.quest

    def get_answer(self):
        return self.ans

class Questions():
    questions = []
    ans = []
    images = []
    for i in range(5):
        fn = "quest" + str(i) + ".png"
        images.append(fn)
        problem = Factorise(1, fn)
        questions.append(problem.get_question())
        ans.append(problem.get_answer())
        print("Problem " + str(i))
        print(problem.get_question())
        print(problem.get_answer())
        # questions.append(Factorise(2, fn).get_question())
    # for i in range(5):
    #     print(questions[i].get_question())
    #     print(questions[i].get_answer())
    # print(questions[3])
    # print(ans[3])
