from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

class ADD(QWidget):
    def __init__(self):
        super().__init__()

        self.hBtnEditLay = QHBoxLayout()
        self.vEditLay = QVBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engEdit = QLineEdit()
        self.engEdit.setPlaceholderText("Eng...")

        self.uzEdit = QLineEdit()
        self.uzEdit.setPlaceholderText("Uzb...")

        self.okBtn = QPushButton("OK")
        self.okBtn.clicked.connect(self.ok)

        self.natijaLbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.vEditLay.addWidget(self.engEdit)
        self.vEditLay.addWidget(self.uzEdit)

        self.hBtnEditLay.addLayout(self.vEditLay)
        self.hBtnEditLay.addWidget(self.okBtn)

        self.vMainLay.addLayout(self.hBtnEditLay)
        self.vMainLay.addWidget(self.natijaLbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def ok(self):
        if len(self.engEdit.text())>0 and len(self.uzEdit.text())>0:
            with open("hello.txt", "a+") as f:
                f.write(f"{self.engEdit.text()} {self.uzEdit.text()}\n")
            self.engEdit.clear()
            self.uzEdit.clear()
            self.natijaLbl.setText("Yangi so'z qo'shildi!")
        else:
            self.natijaLbl.setText("Kiritilmadi!")
            

    def menu(self):
        self.engEdit.clear()
        self.uzEdit.clear()
        self.natijaLbl.clear()
        self.close()

class SEARCH(QWidget):
    def __init__(self):
        super().__init__()

        self.hRadioLay = QHBoxLayout()
        self.hEditBtnLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.EngRadio = QRadioButton("Englsih")
        self.UzRadio = QRadioButton('Uzbek')

        self.Edit = QLineEdit()

        self.searchBtn = QPushButton("search")
        self.searchBtn.clicked.connect(self.search)

        self.lbl = QLabel("")

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hRadioLay.addWidget(self.EngRadio)
        self.hRadioLay.addWidget(self.UzRadio)

        self.hEditBtnLay.addWidget(self.Edit)
        self.hEditBtnLay.addWidget(self.searchBtn)

        self.vMainLay.addLayout(self.hRadioLay)
        self.vMainLay.addLayout(self.hEditBtnLay)
        self.vMainLay.addWidget(self.lbl)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)

    def search(self):
        p = True
        with open("hello.txt", "r") as f:
            if self.EngRadio.isChecked():
                for i in f.read().split("\n"):
                    i = i.split(" ")
                    if i[0] == self.Edit.text():
                        self.lbl.setText(i[-1])
                        p = False
                        f.seek(0)

            elif self.UzRadio.isChecked():
                for i in f.read().split("\n"):
                    i = i.split(" ")
                    if i[-1] == self.Edit.text():
                        self.lbl.setText(i[0])
                        p = False
                        f.seek(0)
        if p:
            self.lbl.setText("Not Found")            

    def menu(self):
        self.Edit.clear()
        self.close()

class LIST(QWidget):
    def __init__(self):
        super().__init__()
        self.navbat = 1

        self.hLblLay = QHBoxLayout()
        self.hListWidgLay = QHBoxLayout()
        self.vMainLay = QVBoxLayout()

        self.engLbl = QLabel("English")
        self.uzLbl = QLabel("Uzbek")

        self.engListWdg = QListWidget()
        self.uzListWdg = QListWidget()
        
        with open("hello.txt", "r") as f:
            for i in f.read().split("\n"):
                i = i.split(" ")
                self.engListWdg.addItem(f"{self.navbat}.{i[0]}")
                self.uzListWdg.addItem(f"{self.navbat}.{i[-1]}")
                self.navbat += 1

        self.menuBtn = QPushButton("MENU")
        self.menuBtn.clicked.connect(self.menu)

        self.hLblLay.addWidget(self.engLbl)
        self.hLblLay.addWidget(self.uzLbl)

        self.hListWidgLay.addWidget(self.engListWdg)
        self.hListWidgLay.addWidget(self.uzListWdg)

        self.vMainLay.addLayout(self.hLblLay)
        self.vMainLay.addLayout(self.hListWidgLay)
        self.vMainLay.addWidget(self.menuBtn)

        self.setLayout(self.vMainLay)
    
    def menu(self):
        self.engListWdg.clear()
        self.uzListWdg.clear()
        self.close()

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.addWindow = ADD()
        self.searchWindow = SEARCH()
        self.listWindow = LIST()

        self.vBtnLay = QVBoxLayout()
        self.hMainLay = QHBoxLayout()

        self.addBtn = QPushButton("ADD")
        self.addBtn.clicked.connect(lambda: self.addWindow.show())

        self.searchBtn = QPushButton("SEARCH")
        self.searchBtn.clicked.connect(self.searchWindow.show)
        
        self.listBtn = QPushButton("LIST")
        self.listBtn.clicked.connect(self.listWindow.show)

        self.exitBtn = QPushButton("EXIT")
        self.exitBtn.clicked.connect(self.close)

        self.vBtnLay.addWidget(self.addBtn)
        self.vBtnLay.addWidget(self.searchBtn)
        self.vBtnLay.addWidget(self.listBtn)
        self.vBtnLay.addWidget(self.exitBtn)

        self.hMainLay.addStretch()
        self.hMainLay.addLayout(self.vBtnLay)
        self.hMainLay.addStretch()

        self.setLayout(self.hMainLay)

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()