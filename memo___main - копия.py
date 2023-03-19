from memo___card_layout import *
from memo_main_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса

card_width, card_height = 600, 500 # начальные размеры окна "карточка"

text_wrong = 'Wrong'
text_correct = 'Correct'

frm_question = 'Яблуко'
frm_right = 'Apple'
frm_wrong1 = 'Aple'
frm_wrong2 = 'Applle'
frm_wrong3 = 'applє'

radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(radio_list)

answer = radio_list[0]
wrong_ans1, wrong_ans2, wrong_ans3 = radio_list[1], radio_list[2], radio_list[3]





def show_data():
    question.setText(frm_question)
    ans.setText(frm_right)
    answer.setText(frm_right)
    wrong_ans1.setText(frm_wrong1)
    wrong_ans2.setText(frm_wrong2)
    wrong_ans3.setText(frm_wrong3)

def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    pass

win_card = QWidget()
win_main = QWidget()
win_main.resize(650, 650)
win_main.setWindowTitle('main menu')
win_main.setLayout(layout_main)


def back_to_menu():
    win_card.hide()
    win_main.showNormal()

btn_menu.clicked.connect(back_to_menu)






win_card.resize(card_width,card_height)
win_card.move(300,300)
win_card.setWindowTitle('Memory Card')
#здесь должны быть параметры окна




win_card.setLayout(layout_card)
win_card.show()
app.exec_()