from PyQt5.QtWidgets import *

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color: #DED3A6;
        color : #759242;
        font-size: 15px;
    }

    QPushButton {
        background-color: #759242;
        color : #374709;
        border-radius: 1px ;
        border-color: #374709;
        border-style: hidden;
        border-width: 5px;
        min-height: 20px;
        font-size: 15px;
        font-family: none;

    }
    
    QLabel {
        background-color: #DED3A6;
        color : #374709;
        font-size: 15px;
    }

""")

window = QWidget()
window.resize(800 , 500)
mainline = QHBoxLayout()

baton1 = QPushButton('створити замітку')
baton2 = QPushButton('видалити замітку')
baton3 = QPushButton('зберегти замітку')
baton4 = QPushButton('додати до замітки')
baton5 = QPushButton('відкріпити від замітки')
baton6 = QPushButton('Шукати по тегу')
text1 = QLabel('список заміток')
text2 = QLabel('список тегів')
pole1 = QTextEdit()
pole2 = QListWidget()
pole3 = QListWidget()
pole4 = QLineEdit()

linepole = QVBoxLayout()
linemenu = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

mainline.addLayout(linepole)
mainline.addLayout(linemenu)
linepole.addWidget(pole1)
linemenu.addWidget(text1)
linemenu.addWidget(pole2)
line1.addWidget(baton1)
line1.addWidget(baton2)
linemenu.addLayout(line1)
linemenu.addWidget(baton3)
linemenu.addWidget(text2)
linemenu.addWidget(pole3)
linemenu.addWidget(pole4)
line2.addWidget(baton4)
line2.addWidget(baton5)
linemenu.addLayout(line2)
linemenu.addWidget(baton6)

window.setLayout(mainline)
window.show()
app.exec()