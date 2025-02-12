import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox

import hortaController

def cadDados():
    temperatura = dadoTemperatura.text().strip()
    humidade = dadoHumidade.text().strip()
    luminosidade = dadoLuminosi.text().strip()

    if not temperatura or not humidade or not luminosidade:
        QMessageBox.critical(None, "ERRO", "Dados não coletados")
        return
    
    idSens = hortaController.regisSensores(temperatura, humidade, luminosidade)

    if idSens:
        QMessageBox.information(None, "Sucesso", "Dados coletados")

        labelHumidade.clear()
        labelTemperatura.clear()
        labelLuminosi.clear()
    else:
        QMessageBox.warning(None, "ERRO", "Dados não cadastrados")



# ------------ Configurações básicas ------------ #
app = QApplication(sys.argv)

janelaSens = QWidget()
janelaSens.setWindowTitle("Tela de Sensores")
janelaSens.setGeometry(500, 30, 480, 720)

labelTitulo = QLabel("Dados de Sensores", janelaSens)
labelTitulo.setObjectName("titulo")
labelTitulo.setGeometry(0, 10, 200, 50)


# ------------ Sensor de Temperatura ------------ #
labelTemperatura = QLabel("Temperatura", janelaSens)
labelTemperatura.setObjectName("temperatura")
labelTemperatura.setGeometry(0, 40, 200, 40)

dadoTemperatura = QLineEdit(janelaSens)
dadoTemperatura.setObjectName("dadoTemp")
dadoTemperatura.setGeometry(0, 80, 200, 40)
dadoTemperatura.setPlaceholderText("Insira a Temperatura")


# ------------ Sensor de Humidade ------------ #
labelHumidade = QLabel("Humidade",janelaSens)
labelHumidade.setObjectName("humidade")
labelHumidade.setGeometry(0, 140, 200, 40)

dadoHumidade = QLineEdit(janelaSens)
dadoHumidade.setObjectName("dadoHumi")
dadoHumidade.setGeometry(0, 180, 200, 40)
dadoHumidade.setPlaceholderText("Insira a Humidade")


# ------------ Sensor de Luminosidade ------------ #
labelLuminosi = QLabel("Luminosidade", janelaSens)
labelLuminosi.setObjectName("luminosidade")
labelLuminosi.setGeometry(0, 230, 200, 40)

dadoLuminosi = QLineEdit(janelaSens)
dadoLuminosi.setObjectName("dadoLumi")
dadoLuminosi.setGeometry(0, 270, 200, 40)
dadoLuminosi.setPlaceholderText("Inisira a Luminosidade")


# ------------ Botão voltar ------------ #
btnVoltar = QPushButton("Voltar",janelaSens)
btnVoltar.setObjectName("btnVoltar")
btnVoltar.setGeometry(0, 350, 100, 30)


# ------------ Botão cadastrar ------------ #
btnCadastrar = QPushButton("Cadastrar", janelaSens)
btnCadastrar.setObjectName("btnCadastrar")
btnCadastrar.setGeometry(130, 350, 100, 30)
btnCadastrar.clicked.connect(cadDados)



janelaSens.show()

sys.exit(app.exec_())