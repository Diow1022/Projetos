import mysql.connector

# conexão com MySQL (XAMPP)
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # padrão do XAMPP é vazio
    database="sistema_pedidos"
)

cursor = conexao.cursor()

# função para adicionar pedido
def adicionar_pedido():
    pedido = input("Número do pedido: ")
    cliente = input("Nome do cliente: ")
    valor = float(input("Valor: "))

    sql = "INSERT INTO pedidos (pedido, cliente, valor) VALUES (%s, %s, %s)"
    valores = (pedido, cliente, valor)

    cursor.execute(sql, valores)
    conexao.commit()

    print("✅ Pedido adicionado com sucesso!\n")


# função para listar pedidos
def listar_pedidos():
    cursor.execute("SELECT * FROM pedidos")

    resultados = cursor.fetchall()

    print("\n📋 Lista de pedidos:")
    for linha in resultados:
        print(linha)
    print()


# menu simples
while True:
    print("1 - Adicionar pedido")
    print("2 - Listar pedidos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_pedido()
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida\n")

# fechar conexão
conexao.close()
