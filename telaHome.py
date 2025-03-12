import sys

import hortaController
import telaCad

from PyQt5.Qt import Qt # Organização dos elementos

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

btnSen = QPushButton("Ver Sensores", janelaHome)
btnSen.setGeometry(0, 30, 200, 30)

janelaHome.show()

sys.exit(app.exec_())