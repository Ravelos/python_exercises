import datetime

renda_mensal = []
gastos_mensais = []
saldo = 0

def adicionar_renda(quantia, data):
    global saldo
    renda_mensal.append({
        "quantia": quantia,
        "data": data,
    })
    saldo += quantia

def adicionar_despesas(quantia, data, descricao):
    global saldo

    if isinstance(data, str):
        data_valida = datetime.datetime.strptime(data, '%d/%m/%Y').date()
    else:
        data_valida = data

    data_atual = datetime.datetime.now().date()

    if data_valida > data_atual:
        print("Data não pode ser maior à data atual.")
        return

    gastos_mensais.append({
        "quantia": quantia,
        "data": data_valida,
        "descricao": descricao,
    })
    saldo -= quantia

def atualizar_saldo():
    global saldo
    saldo = sum(renda["quantia"] for renda in renda_mensal) - sum(despesas["quantia"] for despesas in gastos_mensais)
    return round(saldo,2)

def mostrar_tabela():
    print("\n--- Rendas Mensais ---")
    print("quantia       data")
    for renda in renda_mensal:
        print(f"{renda['quantia']}       {renda['data']}")

    print("\n--- Despesas Mensais ---")
    print("   quantia        data       descricao")
    for despesa in gastos_mensais:
        print(f"    {despesa['quantia']}       {despesa['data']}   {despesa['descricao']}")


def main():
    while True:
        quantia = float(input("Insira o valor recebido no mês: "))
        data = input("Insira a data nesse formato (dd/mm/aaaa): ")
        adicionar_renda(quantia, datetime.datetime.strptime(data, '%d/%m/%Y').date())
        resposta = input("Você deseja adicionar outro valor recebido? (s/n): ")
        if resposta.lower() == 'n':
            break

    while True:
      quantia = float(input("Insira o valor a pagar: "))
      while True:
            data_input = input("Insira a data nesse formato (dd/mm/aaaa): ")
            data = datetime.datetime.strptime(data_input, '%d/%m/%Y').date()
            data_atual = datetime.datetime.now().date()
            if data > data_atual:
              print("Data não pode ser maior à data atual.")
            else:
              descricao = input("Insira a descrição do gasto: ")
              adicionar_despesas(quantia, data, descricao)

              resposta = input("Você deseja adicionar outra despesa? (s/n): ")
            if resposta.lower() == 'n':
                 break
      break
    # Atualiza o saldo
    saldo_atualizado = atualizar_saldo()
    mostrar_tabela()
    print(f"\nSaldo Atual: {saldo_atualizado}")
    print(saldo_atualizado)
if __name__ == "__main__":
    main()
