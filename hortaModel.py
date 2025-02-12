import mysql.connector


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


# ------------ Função de cadastro dos dados ------------ #
def regisSensores(temperatura, humidade, luminosidade):
    sql = "INSERT INTO sensores_tb (temperatura, humidade, luminosidade) VALUES (%s, %s, %s)"

    valores = (temperatura, humidade, luminosidade)

    cursor.execute(sql, valores)
    conexao.commit()

    return cursor.lastrowid


# ------------ Função para encerrar a coneção com o Bancos ------------ #
def fecharConexao():
    cursor.close()
    conexao.close()