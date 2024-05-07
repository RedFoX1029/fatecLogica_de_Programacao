nomes = []
telefones = []
emails = []
print('\n\n ===========CADASTROS DE CONTATOS=========== ')
while True:
    nome = input('Informe o nome do seu contato(0 - Finaliza): ')
    if nome == '0':
        break
    nomes.append(nome)
    telefones.append(input('Informe o telefone do seu contato: '))
    emails.append(input('Informe o email do seu contato: '))
print('\n\n ===========PESQUISANDO CONTATO CADASTRADO===========')
buscaNome = input('\nInforme o nome para pesquisar: ')
achou = False
for i in range(len(nomes)):
    if nomes[i] == buscaNome:
        print(nomes[i])
        print(telefones[i])
        print(emails[i])
        achou = True
        break
    else:
        achou = False
if achou == False:
    print('Contato não encontrado')