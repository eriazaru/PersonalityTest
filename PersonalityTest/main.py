import random
import sys
import typing
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def connectdb(sqlquery):
        connection = sqlite3.connect("./data/db.db")
        cur = connection.cursor()
        
        cur.execute(sqlquery)

        rows = cur.fetchall()

        list_from_db = [list(row) for row in rows]

        return list_from_db

class StartWindow(QDialog):
    def __init__(self):
        super(StartWindow, self).__init__()
        loadUi("start.ui", self)
        self.pushButton.clicked.connect(self.gotoTest)

    def gotoTest(self):
        testwindow = TestWindow()
        widget.addWidget(testwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.show()

class TestWindow(QDialog):
    def __init__(self):
        super(TestWindow, self).__init__()
        loadUi("test.ui", self)
        self.populate()
        self.pushButton.clicked.connect(self.nextQuestion)
        self.a = 0
        self.b = 0
        self.c = 0

    def populate(self):
        sqlquery = "SELECT * FROM questions"

        result_list = connectdb(sqlquery)

        shuffled = random.sample(result_list, len(result_list))

        self.shuffled_questions = shuffled

        self.current_question_index = 0

        self.label_3.setText("Question " + str(self.current_question_index+1))
        self.label_4.setText(str(shuffled[self.current_question_index][1]))
        self.radioButton.setText(str(shuffled[self.current_question_index][2]))
        self.radioButton_2.setText(str(shuffled[self.current_question_index][3]))
        self.radioButton_3.setText(str(shuffled[self.current_question_index][4]))

    def nextQuestion(self):
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked() and not self.radioButton_3.isChecked():
            QMessageBox.warning(self, "Selection Error", "Please select an option!")
            return
        
        if self.radioButton.isChecked():
            self.a +=1
        elif self.radioButton_2.isChecked():
            self.b +=1
        elif self.radioButton_3.isChecked():
            self.c +=1

        print("a: " + str(self.a) + " b:" + str(self.b) + " c: " + str(self.c))

        self.current_question_index += 1

        if self.current_question_index < len(self.shuffled_questions):
            question = self.shuffled_questions[self.current_question_index]

            self.label_3.setText("Question " + str(self.current_question_index + 1))
            self.label_4.setText(question[1])
            self.radioButton.setText(question[2])
            self.radioButton_2.setText(question[3])
            self.radioButton_3.setText(question[4])
            if self.current_question_index == len(self.shuffled_questions) - 1:
                self.pushButton.setText("FINISH")
        else:
            # All questions have been answered, show the result window
            self.pushButton.setText("NEXT")
            resultwindow = ResultWindow(self.a, self.b, self.c)
            widget.addWidget(resultwindow)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.current_question_index = 0
            self.label_3.setText("Question " + str(self.current_question_index+1))
            self.a = 0
            self.b = 0
            self.c = 0

class ResultWindow(QDialog):
    def __init__(self, a, b, c):
        super(ResultWindow, self).__init__()
        loadUi("result.ui", self)

        self.showresult(a, b, c)
        self.pushButton.clicked.connect(self.retakeTest)

    def retakeTest(self):
        testwindow = TestWindow()
        widget.addWidget(testwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.show()

    def showresult(self, a, b, c):
        sqlquery = "SELECT * FROM results"

        result_list = connectdb(sqlquery)

        counts = [a, b, c]
        max_count = max(counts)
        print("a: " + str(a) + " b:" + str(b) + " c: " + str(c))
        print("max count: " + str(max_count))
        if a == max_count:
            if a == b:
                index = 2
            elif a == c:
                index = 0
            else:
                index = 1
        elif b == max_count:
            if b == c:
                index = 0
            else:
                index = 2
        elif c == max_count:
            index = 0

        self.label_2.setText(result_list[index][0])
        self.label_3.setText(result_list[index][1])

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
startwindow = StartWindow()
widget.addWidget(startwindow)
widget.setFixedSize(600, 500)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")