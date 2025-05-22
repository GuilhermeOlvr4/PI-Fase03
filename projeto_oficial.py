import mysql.connector

def criptografia(texto):
    """"""
def descriptografia(texto):
    """"""
# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_projetoti"
)
cursor = conn.cursor() # Para manipular o banco de dados com Python 

def classif_agua(litros: int) -> str: # parte juan # Funções para classificar o comportamento sustentável
    if litros < 150:
        return "Alta Sustentabilidade"
    elif 150 <= litros <= 200:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"

def classif_energia(energia: float) -> str:
    if energia < 5:
        return "Alta Sustentabilidade"
    elif 5 <= energia <= 10:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"

def classif_residuos(residuos: float) -> str:
    if residuos < 5:
        return "Alta Sustentabilidade"
    elif 5 <= residuos <= 10:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"    

def classif_reciclados(reciclados: int) -> str:
    if reciclados > 50:
        return "Alta Sustentabilidade"
    elif 20 <= reciclados <= 50:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"
def classif_transporte(opc1,opc2,opc3,opc4,opc5,opc6: int) -> str:
    if (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and opc4 == "N" and opc6 == "N":
            return "Alta Sustentabilidade"      
    elif (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and (opc4 == "S" or opc6 == "S"):
            return "Moderada Sustentabilidade"
    elif opc1 == "N" and opc2 == "N" and opc3 == "N" and opc5 == "N" and (opc4 == "S" or opc6 == "S"):
            return "Baixa Sustentabilidade"
    transportes_str = ""
    if opc1 == 'S': transportes_str += "| Transporte Público |"
    if opc2 == 'S': transportes_str += "| Bicicleta |"
    if opc3 == 'S': transportes_str += "| Caminhada |"
    if opc4 == 'S': transportes_str += "| Carro (combustível fósseis) |"
    if opc5 == 'S': transportes_str += "| Carro Elétrico |"
    if opc6 == 'S': transportes_str += "| Carona compartilhada (Fósseis) |"
    
def cadastrardados(): 
# Coleta dos dados (cadastrar os dados)
    data = input("Qual é a data (yyyy-MM-dd): ")
    litros = int(input("\nQuantos litros de água você consumiu hoje? (Aprox. em litros): "))
    energia = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
    residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
    reciclados = int(input("Qual a porcentagem de resíduos reciclados no total (em %)?: "))
    print("\nResponda com 'S' e 'N' qual meio de transporte você usou hoje?:")
    opc1 = input('1. Transporte público (ônibus, metrô, trem): ')
    opc2 = input('2. Bicicleta: ')
    opc3 = input('3. Caminhada: ')
    opc4 = input('4. Carro (combustível fósseis): ')
    opc5 = input('5. Carro elétrico: ')
    opc6 = input('6. Carona compartilhada (Fósseis): ')
    # Parte de criptografia
    agua = criptografia(classif_agua(litros))
    ...
    ...
    # precisa do comando SQL para inserir os dados
# Classificações usando funções
consumo_agua = """"""
consumo_energia = """"""
geracao_residuos = """"""
residuos_reciclaveis = """"""
uso_transporte = """"""

# Pra pessoa que for fazer a inserção no banco aqui precisa incluir a inserção dos dados na nova tabela com os valores
insert_query = """
    INSERT INTO resultados_sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
values = (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte)

cursor.execute(insert_query, values)
conn.commit()

print("\nDados inseridos com sucesso!")
# Parte do vinicius
# def alterar_dados():
# def excluir_dados():
# def listar_dados():
# QUERY  PARA GERAR AS MÉDIAS DAS CLASSIFICAÇÕES
select_query = """
SELECT
    -- Consumo de água
    CASE 
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_agua,

    -- Consumo de energia
    CASE 
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_energia,

    -- Geração de resíduos não recicláveis
    CASE 
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_geracao_residuos,

-- Porcentagem de resíduos recicláveis
    CASE 
        WHEN COUNT(DISTINCT residuos_reciclaveis) = 1 AND MAX(residuos_reciclaveis) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT residuos_reciclaveis) = 1 AND MAX(residuos_reciclaveis) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_residuos_reciclaveis,

    -- Uso de transporte
    CASE 
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_uso_transporte
FROM sustentabilidade;
"""

cursor.execute(select_query)
results = cursor.fetchall()

print("\nMédia de todos os dados presentes no banco:")

for row in results:
    print(f"Média de Consumo de Água: {row[0]}")
    print(f"Média de Consumo de Energia: {row[1]}")
    print(f"Média de Geração de Resíduos: {row[2]}")
    print(f"Média de Porcentagem Resíduos Recicláveis: {row[3]}")
    print(f"Média de Uso de Transporte: {row[4]}")

cursor.close()
conn.close()
def menu(): #Parte guilherme
    cadastrardados()
    # por os prints para mostrar oque pode fazer, e quando atribuir um numero a uma função: usar ela 
    # Exemplo:
    # print(f'Menu')
    # if variavelaleatoria == 1:
    #    funcaoaleatoria()

menu()
