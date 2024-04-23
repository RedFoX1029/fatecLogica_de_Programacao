contatos = []

while True:
    nome = input('Digite seu primeiro nome: ')
    telefone = int(input('Digite seu número sem caracteres especiais: '))
    email = input('Digite seu e-mail: ')

    contato = {'nome': nome, 'telefone': telefone, 'email': email}

    contatos.append(contato)

    print(f'\nNome: {contato["nome"]}\nTelefone: {contato["telefone"]}\nE-mail: {contato["email"]}\n')

    remover = input('Deseja remover algum contato? (sim / não): ')
    if remover.lower() == 'sim':
        indice = int(input('Digite o índice do contato que deseja remover: '))
        if indice >= 0 and indice < len(contatos):
            del contatos[indice]
            print('Contato removido com sucesso.')
        else:
            print('Índice inválido.')
 
    continuar = input('\nVocê deseja continuar? (sim / não): ')
    
    if continuar.lower() == 'sim' or continuar.lower() == 'não':
        if continuar.lower() == 'não':
            break
    else:
        print('Valor inválido! Tente novamente\n')