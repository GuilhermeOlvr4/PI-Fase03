import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_projetoti"
)

cursor = conn.cursor() # Para manipular o banco de dados com Python 

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

consumo_agua = ""
consumo_energia = ""
geracao_residuos = ""
residuos_reciclaveis = ""
uso_transporte = ""

print("\nSustentabilidade:")

if litros < 150:
    consumo_agua = "Alta Sustentabilidade"
    print(f'Consumo de água: {consumo_agua}')
elif litros >= 150 and litros <= 200:
    consumo_agua = "Moderada Sustentabilidade"
    print(f'Consumo de água: {consumo_agua}')
else:
    consumo_agua = "Baixa Sustentabilidade"
    print(f'Consumo de água: {consumo_agua}')

if energia < 5:
    consumo_energia = "Alta Sustentabilidade"
    print(f'Consumo de energia: {consumo_energia}')
elif energia >= 5 and energia <= 10:
    consumo_energia = "Moderada Sustentabilidade"
    print(f'Consumo de energia: {consumo_energia}')
else:
    consumo_energia = "Baixa Sustentabilidade"
    print(f'Consumo de energia: {consumo_energia}')

if residuos < 5:
    geracao_residuos = "Alta Sustentabilidade"
    print(f'Geração de Resíduos Não Recicláveis: {geracao_residuos}')
elif litros >= 5 and litros <= 10:
    geracao_residuos = "Moderada Sustentabilidade"
    print(f'Geração de Resíduos Não Recicláveis: {geracao_residuos}')
else:
    geracao_residuos = "Baixa Sustentabilidade"
    print(f'Geração de Resíduos Não Recicláveis: {geracao_residuos}')

if reciclados > 50:
    residuos_reciclaveis = "Alta Sustentabilidade"
    print(f'Resíduos Reciclados: {residuos_reciclaveis}')
elif litros >= 20 and litros <= 50:
    residuos_reciclaveis = "Moderada Sustentabilidade"
    print(f'Resíduos Reciclados: {residuos_reciclaveis}')
else:
    residuos_reciclaveis = "Baixa Sustentabilidade"
    print(f'Resíduos Reciclados: {residuos_reciclaveis}')

if (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and opc4 == "N" and opc6 == "N":
    uso_transporte = "Alta Sustentabilidade"
    print(f'Uso de Transporte: {uso_transporte}')
elif (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and (opc4 == "S" or opc6 == "S"):
    uso_transporte = "Moderada Sustentabilidade"
    print(f'Uso de Transporte: {uso_transporte}')
elif opc1 == "N" and opc2 == "N" and opc3 == "N" and opc5 == "N" and (opc4 == "S" or opc6 == "S"):
    uso_transporte = "Baixa Sustentabilidade"
    print(f'Uso de Transporte: {uso_transporte}')

# Pra pessoa que for fazer a inserção no banco aqui precisa incluir a inserção dos dados na nova tabela com os valores
insert_query = """
    INSERT INTO sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
values = (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte)

cursor.execute(insert_query, values)
conn.commit()

print("\nDados inseridos com sucesso!")


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
