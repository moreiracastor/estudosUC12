import mysql.connector
import telaCad, telaTabelas, telaSensores


# ------------ Conexão com o banco de dados ------------ #
conexao = mysql.connector.connect(
    host="localhost", # Endereço do servidor (Mysql)

    user="root", # Usuário do Banco de Dados
    
    password="", # Senha do Banco de Dados
    
    database="horta_db" # Nome do Banco 
)

# ------------ Editor do Banco ------------ #
cursor = conexao.cursor()


# ------------ Função de cadastro das plantas ------------ #
def cadPlantas(nomePop, nomeCien, imagemPath):
    sql = "INSERT INTO plantas_tb (nomePop, nomeCie, imagePath) VALUES (%s, %s, %s)"

    valores = (nomePop, nomeCien, imagemPath)

    cursor.execute(sql, valores)
    conexao.commit()

    return cursor.lastrowid


# ------------ Função de cadastro dos Sensores ------------ #
def regisSensores(temperatura, humidade, luminosidade):
    sql = "INSERT INTO sensores_tb (temperatura, humidade, luminosidade) VALUES (%s, %s, %s)"

    valores = (temperatura, humidade, luminosidade)

    cursor.execute(sql, valores)
    conexao.commit()

    return cursor.lastrowid


# ------------ Função de ver Tabelas ------------ #
def carregarTabelas():
    sqlPlantas = "SELECT * FROM plantas_tb"
    sqlSensores = "SELECT * FROM sensores_tb"

    cursor.execute(sqlPlantas)
    c1 = cursor.fetchall()

    cursor.execute(sqlSensores)
    c2 = cursor.fetchall()

    return (c1, c2)

# ------------ Funções de abertura de janela ------------ #
def cadPlantas():
    telaCad.janelaCad.show()

def cadSensores():
    telaSensores.janelaSens.show()

def verTabelas():
     telaTabelas.janelaTab.show()

# ------------ Função para encerrar a coneção com o Banco ------------ #
def fecharConexao():
    cursor.close()
    conexao.close()