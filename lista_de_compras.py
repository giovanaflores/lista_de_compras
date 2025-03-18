from time import sleep
import os

ARQUIVO = 'lista_compras.txt'

def carregar_lista():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as file:
            return file.read().splitlines()
    return []

def salvar_lista():
    with open(ARQUIVO, 'w') as file:
        file.write('\n'.join(lista_compras))

def menu():
    print('\n=== Lista de Compra ===')
    print('[1] Adicionar item')
    print('[2] Remover item')
    print('[3] Exibir a lista')
    print('[4] Sair')

lista_compras = carregar_lista()

while True:
    menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        item = input('Digite o nome do item: ')
        lista_compras.append(item)
        print(f'✅ {item} adicionado!')
    
    elif opcao == '2':
        item = input('Digite o nome do item a remover: ')
        if item in lista_compras:
            lista_compras.remove(item)
            print(f'❌ {item} removido!')
        else:
            print('⚠ Item não encontrado!')

    elif opcao == '3':
        if lista_compras:
            print("🛒 Itens da Lista: ", lista_compras)
        else:
            print('A lista está vazia.')

    elif opcao == '4':
        print('👋 Saindo...')
        sleep(2)
        salvar_lista()  # Salva a lista antes de sair
        print("🛒 Itens da Lista: ", lista_compras)
        break

    else:
        print('⚠ Opção inválida! Tente novamente.')
