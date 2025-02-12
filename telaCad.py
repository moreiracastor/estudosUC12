import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

import hortaController


# ------------ Área de Funções ------------ #
def abrir_arquivo():
        options = QFileDialog.Options()  # Configurações do seletor de arquivos
        # Abre a janela para selecionar a imagem, permitindo vários formatos
        global file_name
        file_name, _ = QFileDialog.getOpenFileName(
        None, "Abrir Arquivo", "", "Imagens (*.png *.jpg *.jpeg *.bmp *.gif); Todos os Arquivos (*)", options=options
        )
        if file_name:  # Se um arquivo for selecionado
            global imagemPath
            imagemPath = file_name  # Armazena o caminho da imagem escolhida
            pixmap = QPixmap(file_name)  # Carrega a imagem
            labelImagem.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))  # Exibe a imagem redimensionada

def cadastrarPlantas():
    nomeCien = placeNomeCie.text().strip()
    nomePop = placeNome.text().strip()


    if not nomeCien or not nomePop:
        QMessageBox.critical(None, "ERRO", "Preencha todos os campos")
        return
    
    idPlanta = hortaController.salvarPlantas(nomePop, nomeCien, imagemPath)

    if idPlanta:
        QMessageBox.information(None, "Sucesso", "Planta cadastrada com sucesso")

        placeNomeCie.clear()
        placeNome.clear()
        file_name = ""
    else:
        QMessageBox.critical(None, "ERRO", "Erro ao cadastrar a planta")

# ------------ Criação da tela e da Aplicação ------------ #
app = QApplication(sys.argv) #Criação da Aplicação

janelaCad = QWidget() # Criação da tela
janelaCad.setWindowTitle("Tela de Cadastro") # Título da Tela
janelaCad.setGeometry(500, 20, 480, 720) # Dimensionamento da tela

labelTitulo = QLabel("Faça o Cadastro", janelaCad)
labelTitulo.setObjectName("labelTitulo")
labelTitulo.setGeometry(200, 10, 200, 40)

# ------------ PlaceHolder para o nome Popular da planta ------------ #
placeNome = QLineEdit(janelaCad)
placeNome.setObjectName("placeNome") 
placeNome.setPlaceholderText("Insira o Nome comum")
placeNome.setGeometry(150, 60, 200, 50)

placeNomeCie = QLineEdit(janelaCad)
placeNomeCie.setObjectName("placeNomeCie")
placeNomeCie.setPlaceholderText("Insira o Nome Cientifico")
placeNomeCie.setGeometry(150, 100, 200, 50)

# ------------ Botão para buscar a imagem ------------ #
btnImagem = QPushButton("Buscar Imagem", janelaCad) 
btnImagem.setObjectName("btnImagem")
btnImagem.setGeometry(150, 160, 200, 50)

# ------------ Local da Imagem ------------ #
labelImagem = QLabel(janelaCad)
labelImagem.setObjectName("labelImage")
labelImagem.setGeometry(100, 220, 300, 200)

# ------------ Botão para cadastrar a planta ------------ #
btnCad = QPushButton("Cadastrar", janelaCad)
btnCad.setObjectName("btnCad")
btnCad.setGeometry(150, 430, 200, 50)
btnCad.clicked.connect(cadastrarPlantas)

# ------------ Botão de Cancelar ------------ #
btnCan = QPushButton("Cancelar", janelaCad)
btnCan.setObjectName("btnCan")
btnCan.setGeometry(150, 485, 200, 50)

# ------------ Link do botão com a função ------------ #
btnImagem.clicked.connect(abrir_arquivo)

janelaCad.show() # Função que irá exibir a tela

# ------------ Atribui uma página .qss este arquivo ------------ #
with open("estilo.qss", "r") as arq:
    estilo = arq.read()
    app.setStyleSheet(estilo)

sys.exit(app.exec_()) # Função que para fechar o aplicativo