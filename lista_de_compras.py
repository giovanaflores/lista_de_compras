from time import sleep
def menu():
    print('\n=== Lista de Compra ===')
    print('[1] Adicionar item')
    print('[2] Remover item')
    print('[3] Exibir a lista')
    print('[4] Pagar a compra')

lista_compras = []
lista_valor = []

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        try:
            item = input('Digite o nome do item: ')
            if not item.isalpha():
                raise ValueError
        except ValueError:
            print('⚠ Opção inválida! Digite apenas palavras.')
            continue
        item.capitalize()
        lista_compras.append(item)
        qtd_unidades_item = int(input('Quantidade de unidades deste item: '))
        valor_item = float(input('Valor do item: R$ '))
        valor_unidade = qtd_unidades_item * valor_item
        lista_valor.append(valor_unidade)
        lista_valor.append(valor_item)
       
        if item in lista_compras:
            print(f'✅ {item} adicionado!')
        else:
            print('⚠ Item duplicado!')
            continue
        
    if opcao == '2':
        item = input('Digite o nome do item a remover: ')
        if item in lista_compras:
            lista_compras.remove(item)
            lista_valor.remove(valor_item)
            print(f'❌ {item} removido!')
        else:
            print('⚠ Item não encontrado!')
            continue

    if opcao == '3':
        if lista_compras and lista_valor:
            for i, item in enumerate(lista_compras):
                print(f'{item} - R$ {lista_valor[i*2]}')
        else:
            print('A lista está vazia.')
            continue

    if opcao == '4' : 
        if lista_compras and lista_valor:
            total_itens_lista = len(lista_compras) #quantidade de itens na lista
            print(f'Quantidade de itens na lista: {total_itens_lista} item(s)')
            total_compra = sum(lista_valor[::2]) #soma os valores dos itens
            print(f'Total da compra: R$ {total_compra:.2f}')
            opcao_pagamento = input('Digite a forma de pagamento (Pix/Cartão ou Dinheiro): ')
            opcao_pagamento = opcao_pagamento.lower().capitalize().strip().upper()
            valor_pago = float(input('Digite o valor a pagar: R$ ')) # para o usuario pagar a conta

            if valor_pago < total_compra:
                print('⚠ Valor pago insuficiente!')
                continue
            elif valor_pago == total_compra:
                print('✅ Pagamento efetuado com sucesso!')
                break

            elif valor_pago > total_compra:
                if opcao_pagamento == 'Pix' or opcao_pagamento == 'Cartao':
                    print('Você pagou mais do que o valor da compra')

                elif opcao_pagamento == 'Dinheiro':
                    print('Você pagou mais do que o valor da compra em dinheiro')
                troco = valor_pago - total_compra
                print(f'Troco: R$ {troco:.2f}')
                sleep(2)
                print('✅ Pagamento efetuado com sucesso!')
                break
           	
            if opcao_pagamento != 'Pix' or opcao_pagamento != 'Cartao' or opcao_pagamento != 'Dinheiro':
                print('⚠ Forma de pagamento inválida! Formas de pagamento: Pix, Cartão ou Dinheiro')
                continue
        else:
            print('A lista está vazia.')
            continue
    
    if opcao not in ['1', '2', '3', '4']:
        print('⚠ Opção inválida!')
        continue
