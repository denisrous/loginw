from PyQt5.QtWidgets import QWidget
from random import shuffle
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle("Реєстрація")
window.resize(400, 300)

username = QLabel("Ваш логін:")
password = QLabel("Пароль:")
olegUs = QLineEdit()
olegPas = QLineEdit()
Regestration = QPushButton("Login")

Hor1 = QHBoxLayout() 
Hor2 = QHBoxLayout()
Hor3 = QHBoxLayout()
Vert1 = QVBoxLayout()

Hor1.addWidget(username)
Hor1.addWidget(olegUs)

Hor2.addWidget(password)
Hor2.addWidget(olegPas)

Hor3.addWidget(Regestration)

Vert1.addLayout(Hor1)
Vert1.addLayout(Hor2)
Vert1.addLayout(Hor3)

pop = []
pos = []

def bam():
    if olegUs.text() in pop:
        lol = QMessageBox()
        lol.setWindowTitle("Nipobeda")
        lol.setText("Такий користувач вже є.")
        lol.show()
        lol.exec()
        if pos[pop.index(olegUs.text())] == olegPas.text():
            lol = QMessageBox()
            lol.setWindowTitle("Pobedo")
            lol.setText("Ви успісшно вішли в аккаунт!")
            lol.show()
            lol.exec()
        else:
            lol = QMessageBox()
            lol.setWindowTitle("zabyl porol")
            lol.setText("Некоректний пароль.")
            lol.show()
            lol.exec()
    else:
        pop.append(olegUs.text())
        pos.append(olegPas.text())
        lol = QMessageBox()
        lol.setWindowTitle("Pobeda")
        lol.setText("Ви успісшно зареєстровані!")
        lol.show()
        lol.exec()
Regestration.clicked.connect(bam)

window.setLayout(Vert1)

window.show()
app.exec()