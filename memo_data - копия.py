from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex
from random import randint, shuffle

class Question():
    def __init__(self, question='New question', answer='new answer', wrong_answer1='', wrong_answer2='', wrong_answer3=''):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0
        self.correct = 0
        self.is_active = True 

    def got_right(self):
        self.correct += 1
        self.attempts += 1

    def got_wrong(self):
        self.attempts += 1

    def set_active(self, value):
        self.is_active = value

class QuestionView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        
    def change(self, frm_model):
        self.frm_model = frm_model

    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

class AnswerCheck(QuestionView):
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if answer.isChecked():
            self.result.setText('Correct')
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_right()
        else:
            self.result.setText('Incorrect')
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_wrong()

class QuestionListModel(QAbstractListModel):
    def __init__(self, perent=None):
        super().__init__(parent)
        self.form_list = []
    
    def rowCount(self):
        return len(self.form_list)
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list(index.row())
            return form.question
    def insertRows(self, parent=QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position)
        self.form_list_append(Question())
        self.endInsertRows()
        QModelIndex()
        return True

    def romoveRows(self, position, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total = len(self.form_list)
        current = randint(0, total-1)
        return self.form_list[current]

def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card

























































