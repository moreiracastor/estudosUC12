from hortaModel import *


def salvarPlantas(nomePop, nomeCien, imagemPath):

    if nomePop and nomeCien:
        return cadPlantas(nomePop=nomePop, nomeCien=nomeCien, imagemPath=imagemPath)
    
    return None

def salvarDados(temperatura, humidade, luminosidade):

    if temperatura and humidade and luminosidade:
        return regisSensores(temperatura=temperatura, humidade=humidade, luminosidade=luminosidade)
    
    return None

def carregarColunas():
    return carregarTabelas()

def verPlantas():
    return cadPlantas()

def verSensores():
    return cadSensores()

def verTab():
    return verTabelas()