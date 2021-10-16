from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QHBoxLayout, QVBoxLayout,QGroupBox, QButtonGroup, QRadioButton, QPushButton, QButtonGroup, QLabel)
from random import *

def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1        
            self.wrong2 = wrong2
            self.wrong3 = wrong3


def show_answer():
    questgroup.hide()
    answergroup.show()
    but_ok.setText('Следующий ответ')

def show_question():
    RadioGroup.setExclusive(False)
    but1.setChecked(False)
    but2.setChecked(False)
    but3.setChecked(False)
    but4.setChecked(False)
    RadioGroup.setExclusive(True)
    answergroup.hide()
    questgroup.show()
    but_ok.setText('Ответить')


def start():
    if but_ok.text()=='Ответить':
        check_answer()
    else:
        next_question()


def ask(q:Question):
    question_label.setText(q.question)
    shuffle(answer)

    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)


    # установить в виджет rightanswerlabel текст правильного ответа
    rightanswerlabel.setText(q.right_answer)
    show_question()

def check_answer():
# если выбран кнопка answers[0], то установить в виджет resultlabel текст 'Правильно!'
    if answer[0].isChecked():
        resultlabel.setText('Правильно')
    # иначе, установить 'Неверно!'
    else:
        resultlabel.setText('Неправильно')
    show_answer()
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''

    



app = QApplication([])

window = QWidget()
window.resize(600,400)

question_label = QLabel('Зимой и летом одним цветом')
but_ok = QPushButton('Ответить')

questgroup = QGroupBox('Выберите правильный ответ')


but1 = QRadioButton('Энцы')
but2 = QRadioButton('Смурфы')
but3 = QRadioButton('Чулымцы')
but4 = QRadioButton('Алеуты')

answer=[but1, but2, but3, but4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(but1)
RadioGroup.addButton(but2)
RadioGroup.addButton(but3)
RadioGroup.addButton(but4)


questlayout = QVBoxLayout()
questlayout.addWidget(but1)
questlayout.addWidget(but2)
questlayout.addWidget(but3)
questlayout.addWidget(but4)
questgroup.setLayout(questlayout)

answergroup = QGroupBox('Результат')
answerlayout = QVBoxLayout()

#csgo love

resultlabel = QLabel('Правильно Неправильно')
rightanswerlabel = QLabel('Тут будет правильный ответ')
answerlayout.addWidget(resultlabel)
answerlayout.addWidget(rightanswerlabel)
answergroup.setLayout(answerlayout)

 

main_layout = QVBoxLayout()
main_layout.addWidget(question_label)
main_layout.addWidget(questgroup)
main_layout.addWidget(answergroup)
main_layout.addWidget(but_ok)



answergroup.hide()
but_ok.clicked.connect(start)
window.setLayout(main_layout)

q = Question('Какого цвета нет на флаге России','Зеленый','Красный','Синий','Белый')
question_list=[]
question_list.append(q)
question_list.append(Question('2+2', '4', '3', '6', '2'))
question_list.append(Question('2+3', '5', '4', '6', '2'))
window.cur_question = -1





next_question()
window.show()
# вызываем функцию show_question
show_question()
app.exec()
