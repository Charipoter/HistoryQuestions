import sys
from random import randint
from window import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication


class Init_Window(QWidget, Ui_Form):
    def __init__(self):
        super(Init_Window, self).__init__()
        self.setupUi(self)
        self.ans_dic = {}
        self.que_list = []
        self.ans = ''
        self.index = 0
        self.max = 100


class Main_Function(Init_Window):
    def __init__(self):
        super(Main_Function, self).__init__()

    def set_question(self, index):
        file = open(r'{}s.txt'.format(str(index)), 'r', encoding='utf-8')
        self.ans_dic = {}
        self.que_list = []
        n = 0
        question = ''
        while True:
            line = file.readline()
            if line == 'e':
                break
            if line == '\n':
                ans = file.readline()
                self.ans_dic[n] = ans[0]
                self.que_list.append(question)
                question = ''
                n += 1
            else:
                question += line
        self.max = n
        file.close()

    def select_question(self):
        index = self.select_box.currentIndex()
        if index == 0:
            pass
        else:
            self.index = 0
            self.set_question(index)
            self.set_page2()
            self.stackedWidget.setCurrentIndex(1)

    def set_page2(self):
        self.textEdit.setText(self.que_list[self.index])
        self.ans = self.ans_dic[self.index]
        self.label.setText('')

    def next_question(self):
        self.index = (self.index + 1) % self.max
        self.set_page2()

    def back_question(self):
        self.index -= 1
        if self.index == -1:
            self.index = self.max - 1
        self.set_page2()

    def random_question(self):
        self.index = randint(0, self.max - 1)
        self.set_page2()

    def judge_ans(self, ans):
        if ans == self.ans:
            self.label.setText('你答对了，ohohohohohoh!!')
        else:
            self.label.setText('你答错了，再试一次')

    def choice_A(self):
        self.judge_ans('A')

    def choice_B(self):
        self.judge_ans('B')

    def choice_C(self):
        self.judge_ans('C')

    def choice_D(self):
        self.judge_ans('D')

    def go_page0(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()
    my_pyqt_form = Main_Function()
    my_pyqt_form.show()
    sys.exit(app.exec_())