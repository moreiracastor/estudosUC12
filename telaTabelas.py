import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox, QTableWidget, QVBoxLayout, QTableWidgetItem

import hortaController


def carregarDados():
    dadosPlantas = hortaController.carregarColunas()[0]
    dadosSensores = hortaController.carregarColunas()[1]

    tabelaPlantas.setRowCount(len(dadosPlantas))
    tabelaSensor.setRowCount(len(dadosSensores))

    for linha, planta in enumerate(dadosPlantas):
        tabelaPlantas.setItem(linha, 0, QTableWidgetItem(str(planta[0])))
        tabelaPlantas.setItem(linha, 1, QTableWidgetItem(planta[1]))
        tabelaPlantas.setItem(linha, 2, QTableWidgetItem(planta[2]))

    for linha, sensor in enumerate(dadosSensores):
        tabelaSensor.setItem(linha, 0, QTableWidgetItem(str(sensor[0])))
        tabelaSensor.setItem(linha, 1, QTableWidgetItem(str(sensor[1])))
        tabelaSensor.setItem(linha, 2, QTableWidgetItem(str(sensor[2])))
        tabelaSensor.setItem(linha, 3, QTableWidgetItem(str(sensor[3])))

app = QApplication(sys.argv)

janelaTab = QWidget()
janelaTab.setWindowTitle("Tabelas")
janelaTab.setGeometry(500, 30, 480, 720)


layout = QVBoxLayout()
janelaTab.setLayout(layout)


tabelaPlantas = QTableWidget()
tabelaPlantas.setColumnCount(3)
tabelaPlantas.setHorizontalHeaderLabels(["ID", "Nome Cien", "Nome Pop"])


tabelaSensor = QTableWidget()
tabelaSensor.setColumnCount(4)
tabelaSensor.setHorizontalHeaderLabels(["ID", "Temperatura", "Humidade", "Luminosidade"])


btnAtualizar = QPushButton("Atualizar dados")
btnAtualizar.clicked.connect(carregarDados)

layout.addWidget(tabelaPlantas)
layout.addWidget(tabelaSensor)
layout.addWidget(btnAtualizar)


janelaTab.show()
sys.exit(app.exec_())