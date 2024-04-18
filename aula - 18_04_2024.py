#Métodos da classe string

#Espaços em branco
curso = "pYthOn"

print(curso.upper())
print(curso.lower())
print(curso.title())

#Strip
strip = "   strip "

print(strip.strip())
print(strip.lstrip())
print(strip.rstrip())

#Center
center = "Python"

print(center.center(12, "*"))
print(".".join(center))

##############################################################################################

#Interpolaçã0 de variáveis
nome = "Levi"
idade = 18
profissao = "Programador"
linguagem = "Python"

#Old style
print('''Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e 
 estou matriculado no curso de %s.''' % (nome, idade, profissao, linguagem))

#.Format
print('''Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e
 estou matriculado no curso de {}.''' .format(nome, idade, profissao, linguagem))

#fstring
print(f'''Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e
 estou matriculado no curso de {linguagem}.''')

##############################################################################################

#Fatiamento de strings
nome = "Guilherme Arthur de Carvalho"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(f"nome ao contrario: {nome[::-1]}")