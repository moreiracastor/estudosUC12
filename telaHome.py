import sys

import hortaController

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication(sys.argv)

janelaHome = QWidget()
janelaHome.setWindowTitle("Home")

# ------------------------ #
janelaHome.setFixedHeight(720)
janelaHome.setFixedWidth(480)
# ------------------------ #

btnCad = QPushButton("Cadastrar Plantas", janelaHome)
btnCad.setGeometry(0, 0, 200, 30)
btnCad.clicked.connect(hortaController.verPlantas)

btnSen = QPushButton("Ver Sensores", janelaHome)
btnSen.setGeometry(0, 30, 200, 30)
btnSen.clicked.connect(hortaController.verSensores)

btnTab = QPushButton("Ver Tabelas", janelaHome)
btnTab.setGeometry(0, 60, 200, 30)
btnTab.clicked.connect(hortaController.verTabelas)

janelaHome.show()

sys.exit(app.exec_())