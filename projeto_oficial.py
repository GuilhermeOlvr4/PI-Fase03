import mysql.connector

# Funções de criptografia simples
def criptografia(texto):
    if texto == 'Alta Sustentabilidade':
        return 'A1'
    elif texto == 'Moderada Sustentabilidade':
        return 'B2'
    elif texto == 'Baixa Sustentabilidade':
        return 'C3'
    else:
        return texto

def descriptografia(texto):
    if texto == 'A1':
        return 'Alta Sustentabilidade'
    elif texto == 'B2':
        return 'Moderada Sustentabilidade'
    elif texto == 'C3':
        return 'Baixa Sustentabilidade'
    else:
        return texto

# Conexão com o banco de dados 
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="MuriloMoraes",
    password="Buck2005#",
    database="bd_projetoti"
)
cursor = conn.cursor()

# Funções de classificação: avaliam o nível de sustentabilidade
def classif_agua(litros: int) -> str:
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

def classif_reciclados(reciclados: float) -> str:
    if reciclados > 50:
        return "Alta Sustentabilidade"
    elif 20 <= reciclados <= 50:
        return "Moderada Sustentabilidade"
    else:
        return "Baixa Sustentabilidade"
    
def classif_transporte(opc1, opc2, opc3, opc4, opc5, opc6: int) -> str:
    if (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and opc4 == "N" and opc6 == "N":
        return "Alta Sustentabilidade"      
    elif (opc1 == "S" or opc2 == "S" or opc3 == "S" or opc5 == "S") and (opc4 == "S" or opc6 == "S"):
        return "Moderada Sustentabilidade"
    elif opc1 == "N" and opc2 == "N" and opc3 == "N" and opc5 == "N" and (opc4 == "S" or opc6 == "S"):
        return "Baixa Sustentabilidade"
    else:
        return 'Moderada Sustentabilidade'
# Função para inserir novos dados
def cadastrardados():

    data = input("Qual é a data (yyyy-MM-dd): ")

    cursor.execute("SELECT * FROM valores_sustentabilidade WHERE data = %s", (data,))
    if cursor.fetchone():
        print ("\nJá existe um registro para essa data.\n")
        return
    
    litros = int(input("\nQuantos litros de água você consumiu hoje? (Aprox. em litros): "))
    energia = float(input("Quantos kWh de energia elétrica você consumiu hoje?: "))
    residuos = float(input("Quantos kg de resíduos não recicláveis você gerou hoje?: "))
    reciclados = int(input("Qual a porcentagem de resíduos reciclados no total (em %)?: "))
    print("\nResponda com 'S' e 'N' qual meio de transporte você usou hoje?:")
    opc1 = input('1. Transporte público (ônibus, metrô, trem): ').upper()
    opc2 = input('2. Bicicleta: ').upper()
    opc3 = input('3. Caminhada: ').upper()
    opc4 = input('4. Carro (combustível fósseis): ').upper()
    opc5 = input('5. Carro elétrico: ').upper()
    opc6 = input('6. Carona compartilhada (Fósseis): ').upper()

    # Criptografa as classificações antes de inserir
    consumo_agua = criptografia(classif_agua(litros))
    consumo_energia = criptografia(classif_energia(energia))
    geracao_residuos = criptografia(classif_reciclados(reciclados))
    uso_transporte = criptografia(classif_transporte(opc1, opc2, opc3, opc4, opc5, opc6))
    
    # string com transportes usados para armazenamento
    transportes_str = ""
    if opc1 == 'S': transportes_str += "| Transporte Público |"
    if opc2 == 'S': transportes_str += "| Bicicleta |"
    if opc3 == 'S': transportes_str += "| Caminhada |"
    if opc4 == 'S': transportes_str += "| Carro (combustível fósseis) |"
    if opc5 == 'S': transportes_str += "| Carro Elétrico |"
    if opc6 == 'S': transportes_str += "| Carona compartilhada (Fósseis) |"

    # Comandos para inserir em duas tabelas
    insert_resultados = """
    INSERT INTO resultados_sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, uso_transporte)
    VALUES (%s, %s, %s, %s, %s)
    """
    insert_valores = """
        INSERT INTO valores_sustentabilidade (data, valor_agua, valor_energia, valor_residuos, valor_reciclaveis, valor_transporte)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores_resultados = (data, consumo_agua, consumo_energia, geracao_residuos, uso_transporte)
    valores_valores = (data, litros, energia, residuos, reciclados, transportes_str)

    cursor.execute(insert_resultados, valores_resultados)
    cursor.execute(insert_valores, valores_valores)
    conn.commit()

    print(f"\nDados inseridos com sucesso.")

# Outras funções: alterar, excluir, listar e calcular média seguem lógica similar

def alterar_dados():
    data = input("Digite a data do registro que deseja alterar (YYYY-MM-DD): ")
    cursor.execute("SELECT id FROM valores_sustentabilidade WHERE data = %s", (data,))
    resultado = cursor.fetchone()
    if not resultado:
        print("\nNenhum registro encontrado para essa data.\n")
        return
    id_valor = resultado[0]

    litros = int(input("\nNovo valor - Quantos litros de água foram consumidos?: "))
    energia = float(input("Novo valor - Quantos kWh de energia foram consumidos?: "))
    residuos = float(input("Novo valor - Quantos kg de resíduos não recicláveis foram gerados?: "))
    reciclados = int(input("Novo valor - Qual a porcentagem de resíduos reciclados (em %)? : "))
    print("\nResponda com 'S' ou 'N' sobre os meios de transporte usados no dia:")
    opc1 = input('1. Transporte público (ônibus, metrô, trem): ').upper()
    opc2 = input('2. Bicicleta: ').upper()
    opc3 = input('3. Caminhada: ').upper()
    opc4 = input('4. Carro (combustível fósseis): ').upper()
    opc5 = input('5. Carro elétrico: ').upper()
    opc6 = input('6. Carona compartilhada (Fósseis): ').upper()

    consumo_agua = criptografia(classif_agua(litros))
    consumo_energia = criptografia(classif_energia(energia))
    geracao_residuos = criptografia(classif_reciclados(reciclados))
    uso_transporte = criptografia(classif_transporte(opc1, opc2, opc3, opc4, opc5, opc6))

    transportes_str = ""
    if opc1 == 'S': transportes_str += "| Transporte Público |"
    if opc2 == 'S': transportes_str += "| Bicicleta |"
    if opc3 == 'S': transportes_str += "| Caminhada |"
    if opc4 == 'S': transportes_str += "| Carro (combustível fósseis) |"
    if opc5 == 'S': transportes_str += "| Carro Elétrico |"
    if opc6 == 'S': transportes_str += "| Carona compartilhada (Fósseis) |"

    update_valores = """
    UPDATE valores_sustentabilidade 
    SET valor_agua = %s, valor_energia = %s, valor_residuos = %s, 
        valor_reciclaveis = %s, valor_transporte = %s
    WHERE data = %s
    """
    cursor.execute(update_valores, (litros, energia, residuos, reciclados, transportes_str, data))

    update_resultados = """
    UPDATE resultados_sustentabilidade 
    SET consumo_agua = %s, consumo_energia = %s, 
        geracao_residuos = %s, uso_transporte = %s 
    WHERE data = %s
    """
    cursor.execute(update_resultados, (consumo_agua, consumo_energia, geracao_residuos, uso_transporte, data))

    conn.commit()
    print("\nDados atualizados com sucesso!")


def excluir_dados():
    data = input("\nDigite a data do registro que deseja excluir (YYYY-MM-DD): ")
    cursor.execute("DELETE FROM resultados_sustentabilidade WHERE data = %s", (data,))
    cursor.execute("DELETE FROM valores_sustentabilidade WHERE data = %s", (data,))
    conn.commit()
    print("\nRegistro excluído com sucesso!")


def listar_dados():
    select_query = """
    SELECT 
        v.data, 
        v.valor_agua,    r.consumo_agua,
        v.valor_energia, r.consumo_energia,
        v.valor_residuos,
        v.valor_reciclaveis, r.geracao_residuos, 
        v.valor_transporte,   r.uso_transporte
    FROM valores_sustentabilidade v
    JOIN resultados_sustentabilidade r ON v.data = r.data
    ORDER BY v.data DESC
    """
    cursor.execute(select_query)
    registros = cursor.fetchall()

    if not registros:
        print("\nNenhum monitoramento cadastrado.\n")
        return

    print("\nMonitoramentos cadastrados:\n")
    for (data, litros, cod_agua, energia, cod_energia, residuos, reciclaveis, cod_resíduos, transportes_str, cod_transporte) in registros:
        classif_agua = descriptografia(cod_agua)
        classif_energia = descriptografia(cod_energia)
        classif_resid = descriptografia(cod_resíduos)
        classif_transp = descriptografia(cod_transporte)

        print(f"Data: {data}\n")
        print(f"Consumo de Água: {litros} litros (Classificação: {classif_agua})")
        print(f"Consumo de Energia: {energia} kWh (Classificação: {classif_energia})")
        print(f"Resíduos não recicláveis gerados: {residuos} kg | Porcentagem de reciclados: {reciclaveis}% (Classificação: {classif_resid})")
        print(f"Uso de Transporte: {transportes_str} (Classificação: {classif_transp})")
        print("--------------------------------------------------")

def media_dados():
    media_query = """
    SELECT
      -- Água
      CASE
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'A1' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'C3' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
      END AS media_consumo_agua,

      -- Energia
      CASE
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'A1' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'C3' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
      END AS media_consumo_energia,

      -- Resíduos
      CASE
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'A1' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'C3' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
      END AS media_geracao_residuos,

      -- Transporte
      CASE
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'A1' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'C3' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
      END AS media_uso_transporte

    FROM resultados_sustentabilidade
    """
    cursor.execute(media_query)
    media = cursor.fetchone()

    print("\nMédias Classificadas de Sustentabilidade:\n")
    print(f"Consumo de Água: {media[0]}")
    print(f"Consumo de Energia: {media[1]}")
    print(f"Geração de Resíduos: {media[2]}")
    print(f"Uso de Transporte: {media[3]}")

def menu():    
    opcao = 0
    while opcao != 6:
        print(
            "\nMenu:\n"
            "\n1. Inserir dados de monitoramento\n"
            "2. Alterar dados de monitoramento\n"
            "3. Apagar dados de monitoramento\n"
            "4. Listar cada monitoramento diário e classificar\n"
            "5. Calcular e mostrar as médias dos parâmetros de monitoramento e classificar\n"
            "6. Saída do sistema"
        )

        opcao = input("\nEscolha uma opção: ")
        if not opcao.isdigit():
            print("Erro: digite um número de 1 a 6.")
            continue
        opcao = int(opcao)
        if opcao < 1 or opcao > 6:
            print("Escolha uma opção de 1 a 6.")
        elif opcao == 1:
            cadastrardados()
        elif opcao == 2:
            alterar_dados()
        elif opcao == 3:
            excluir_dados()
        elif opcao == 4:
            listar_dados()
        elif opcao == 5:
            media_dados()
        elif opcao == 6:
            print("\nSaindo do sistema.\n")
            cursor.close()
            conn.close()

menu()
