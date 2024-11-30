"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Sistema Acadêmico
Data: 08/11/2021
Atualização: 13/12/2021
"""
#Bibliotecas

from tabulate import tabulate#Importa a biblioteca "tabulate", utilizada para gerar o boletim em formato de tabela

#Variáveis e Listas

materias = ["Língua Portugesa","Matemática","Física","Química","História","Educação Física","Filosofia","Sociologia","Artes","SO","FHMMC","LTP"]#Lista contendo as matérias escolares
medias =[]#Lista que vai receber as notas finais de cada matéria
reprovacao = []#Lista que vai receber as matérias em que o aluno foi reprovado
semestres = ["primeiro", "segundo"]#Lista contendo os dois semestres escolares
primeiroS = []#Lista que recebe as notas do aluno no primeiro semestre de cada matéria
segundoS = []#Lista que recebe as notas do aluno no segundo semestre de cada matéria
statusM = []#Lista que recebe o status de aprovação do aluno em cada matéria
soma = 0#Variável que recebe a soma das notas do primeiro e segundo semestre em cada matéria
validarE = 0#Variável utilizada para verificar o email
validarE2 = 0#Variável utilizada para verificar o email
validarE3 = 0#Variável utilizada para verificar o email
validarE4 = 0#Variável utilizada para verificar o email
validarN = 0#Variável utilizada para verificar o nome
validarN2 = 0#Variável utilizada para verificar o nome
validarN3 = 0#Variável utilizada para verificar o nome
repetir = 0#Variável utilizada para verificar se deve pular uma linha
repetir1 = 0#Variável utilizada para verificar se deve pular uma linha
validarI = 0#Variável utilizada para verificar a identidade
validarI2 = 0#Variável utilizada para verificar a identidade
validarI3 = 0#Variável utilizada para verificar a identidade
numeros_cpf = []#Lista que vai receber os números do CPF
validarCPF = 0#Variável utilizada para verificar o CPF
validarCPF2 = 0#Variável utilizada para verificar o CPF
repetir2 = 0#Variável utilizada para verificar se deve pular uma linha

#Entrada e Processamento de dados

def Front (F1):#Função que define o front-end de cada parte do programa
    if(F1==1):#Front-end mostrando quando F1 vale 1
        print(("=")*134)
        print(("SISTEMA ACADÊMICO").center(134,"="))
        print(("=")*134)
        print(" ")
        print(" ")
        print(("-")*134)
        print(("-Preencha os dados pessoais exigidos abaixo-").center(134, "-"))
        print(("-")*134)
        print(" ")
        print(" ")
    elif(F1==2):#Front-end mostrando quando F1 vale 2
        print(" ")
        print(("-")*134)
        print(("-Preencha com suas notas do ano-").center(134, "-"))
        print(("-")*134)
        print(" ")
        print(" ")
    elif(F1==3):#Front-end mostrando quando F1 vale 3
        print(("=")*134)
        print(("DADOS PESSOAIS").center(134,"="))
        print(("=")*134)
        print(" ")
    elif(F1==4):#Front-end mostrando quando F1 vale 4
        print(" ")
        print(" ")
        print(("=")*134)
        print(("BOLETIM").center(134,"="))
        print(("=")*134)
        print(" ")
        
Front(1)#Comando que mostra o front-end quando F1 vale 1

nome = str(input("➤ Informe seu nome completo: "))#Comando que pede para o usuário inserir seu nome
while(validarN<1):#Comando que valida o nome
    for no in range (len(nome)):#Comando que verifica se o nome é válido
        if (nome[no] == " "):#Adiciona 1 à variável "validarN2" quando len do nome correspondente à variável "no" for igual à " "
            validarN2 += 1
        if (nome[no]=="1")or(nome[no]=="2")or(nome[no]=="3")or(nome[no]=="4")or(nome[no]=="5")or(nome[no]=="6")or\
        (nome[no]=="7")or(nome[no]=="8")or(nome[no]=="9")or(nome[no]=="0"):
            validarN3 += 1
    if(len(nome)<3)or(validarN2>(len(nome)-3))or(validarN2==len(nome))or(nome[0]==" ")or(validarN3!=0):#Comando que exige um nome válido
        if (repetir==0):#Pula uma linha na primeira repetição do while
            print(" ")
        print("Informação inválida!")
        nome = str(input("➢ Nome com três ou mais letras (não use espaço no começo e nem números): "))#Comando que pede para o usuário reinserir seu nome
        print(" ")
        no = 0#Zera a variável "no"
        validarN2 = 0#Zera a variável "validarN2"
        validarN3 = 0#Zera a variável "validarN3"
        repetir += 1#Adiciona 1 à variável "repetir"
    else:#Comando que adiciona 1 à variável "validarN" quando o nome é válido, parando o while
        validarN += 1
            
cpf = str(input("➤ Informe seu CPF (apenas números): "))#Comando que pede para o usuário inserir seu CPF
while (validarCPF<1):#Comando que valida o CPF
    for cpff in range (len(cpf)):#Comando que verifica se o CPF é formado apenas por números
        if (cpf[cpff]=="1")or(cpf[cpff]=="2")or(cpf[cpff]=="3")or(cpf[cpff]=="4")or(cpf[cpff]=="5")or(cpf[cpff]=="6")or\
        (cpf[cpff]=="7")or(cpf[cpff]=="8")or(cpf[cpff]=="9")or(cpf[cpff]=="0"):
            validarCPF2 += 1
    if(len(cpf)!=11)or(validarCPF2!=len(cpf)):#Gera o resultado quando o CPF não é formado por onze números
        if(repetir2==0):#Pula uma linha na primeira repetição do while
            print(" ")
        print("Informação inválida!")
        cpf = str(input("➢ CPF com onze caracteres (contendo apenas números): "))#Comando que pede para o usuário reinserir seu CPF
        print(" ")
        cpff = 0#Zera a variável "cpff"
        cpff2 = 0#Zera a variável "cpff2"
        validarCPF2 = 0#Zera a variável "validarCPF2"
        repetir2 += 1#Adiciona 1 à variável "repetir2"
    elif(len(cpf)==11)and(validarCPF2==len(cpf)):#Comando que verifica se o CPF os números inseridos são válidos
        for cpff2 in range (len(cpf)):#Comando que coloca os números do CPF em uma lista
            numeros_cpf.append(cpf[cpff2])
        numero0 = int(numeros_cpf[0])#Tranforma o primeiro número da lista em int
        numero1 = int(numeros_cpf[1])#Tranforma o segundo número da lista em int
        numero2 = int(numeros_cpf[2])#Tranforma o terceiro número da lista em int
        numero3 = int(numeros_cpf[3])#Tranforma o quarto número da lista em int
        numero4 = int(numeros_cpf[4])#Tranforma o quinto número da lista em int
        numero5 = int(numeros_cpf[5])#Tranforma o sexto número da lista em int
        numero6 = int(numeros_cpf[6])#Tranforma o sétimo número da lista em int
        numero7 = int(numeros_cpf[7])#Tranforma o oitavo número da lista em int
        numero8 = int(numeros_cpf[8])#Tranforma o nono número da lista em int
        numero9 = int(numeros_cpf[9])#Tranforma o décimo número da lista em int
        numero10 = int(numeros_cpf[10])#Tranforma o décimo primeiro número da lista em int
        resto1 = ((((numero0*10)+(numero1*9)+(numero2*8)+(numero3*7)+(numero4*6)+(numero5*5)+(numero6*4)+(numero7*3)+(numero8*2))*10)%11)#Primeiro cálculo de validação de CPF
        resto2 = ((((numero0*11)+(numero1*10)+(numero2*9)+(numero3*8)+(numero4*7)+(numero5*6)+(numero6*5)+(numero7*4)+(numero8*3)+(numero9*2))*10)%11)#Segundo cálculo de validação de CPF
        if(resto2>=10):#Define o "resto2" como 0 se o resto da divisão for maior ou igual a 10
            resto2 = 0
        if(resto1>=10):#Define o "resto1" como 0 se o resto da divisão for maior ou igual a 10
            resto1 = 0
        if(resto1==numero9)and(resto2==numero10)and(cpf!="11111111111")and(cpf!="22222222222")and(cpf!="33333333333")and(cpf!="44444444444")and(cpf!="55555555555")and\
        (cpf!="66666666666")and(cpf!="77777777777")and(cpf!="88888888888")and(cpf!="99999999999")and(cpf!="00000000000"):#Adiciona 1 à "validarCPF" quando o CPF é válido, parando o while
            validarCPF += 1
        else:#Gera o resultado quando CPF é inválido
            if(repetir2==0):#Pula uma linha na primeira repetição do while
                print(" ")
            print("Informação inválida!")
            cpf = str(input("➢ Insira um CPF com números válidos: "))#Comando que pede para o usuário reinserir seu CPF
            print(" ")
            numeros_cpf.clear()#Limpa a lista "numeros_cpf"
            cpff = 0#Zera a variável "cpff"
            cpff2 = 0#Zera a variável "cpff2"
            validarCPF2 = 0#Zera a variável "validarCPF2"
            repetir2 += 1#Adiciona 1 à variável "repetir2"
        
identidade = str(input("➤ Informe o seu RG: "))#Comando que pede para o usuário inserir sua identidade
while(validarI<1):#Comando que valida a identidade
    for iden in range (len(identidade)):#Comando que verifica se a identidade é válida
        if (identidade[iden] == " "):#Adiciona 1 à variável "validarI2" quando len da identidade correspondente à variável "iden" for igual à " "
            validarI2 += 1
        elif (identidade[iden] == "1")or(identidade[iden] == "2")or(identidade[iden] == "3")or(identidade[iden] == "4")or(identidade[iden] == "5")or(identidade[iden] == "6")or\
        (identidade[iden] == "7")or(identidade[iden] == "8")or(identidade[iden] == "9")or(identidade[iden] == "0"):#Adiciona 1 à variável "validarI3" quando len da identidade correspondente à variável "iden" for igual à um número
            validarI3 += 1
    if(len(identidade)<6)or(validarI3<6)or(validarI2!=0)or(validarI3>=6)and((len(identidade)-validarI3)>3):#Comando que exige uma identidade válida                                                                                                                                                 
        if (repetir1==0):#Pula uma linha na primeira repetição do while
            print(" ")
        print("Informação inválida!")
        identidade = str(input("➢ RG com seis ou mais números e no máximo três letras: "))#Comando que pede para o usuário reinserir sua identidade
        print(" ")
        iden = 0#Zera a variável "iden"
        validarI2 = 0#Zera a variável "validarI2"
        validarI3 = 0#Zera a variável "validarI3"
        repetir1 += 1#Adiciona 1 à variável "repetir1"
    else:#Comando que adiciona 1 à variável "validarI" quando a identidade é válida, parando o while
        validarI += 1
    
cep = int(input("➤ Informe seu CEP (apenas números): "))#Comando que pede para o usuário inserir seu CEP
cep2 = str(cep)#Cria uma variável para o CEP convertido em string
if(len(cep2)!=8)or(cep<0):#Comando que pula uma linha quando o CEP tem len menor que 8 ou é negativo
    print(" ")
while(len(cep2)!=8)or(cep<0):#Comando que exige um cep com mais do que 8 caracteres e positivo
    print("Informação inválida!")
    cep = int(input("➢ CEP com oito caracteres (e positivo): "))#Comando que pede para o usuário reinserir seu CEP
    cep2 = str(cep)#Cria uma variável para o CEP convertido em string
    print(" ")
    
email = str(input("➤ Informe seu email: "))#Comando que pede para o usuário inserir seu email
print(" ")
while(validarE<1):#Comando que valida o email
    for e in range (len(email)):#Comando que verifica se o email é válido
        if (email[e] != "@"):#Adiciona 1 à variável "validarE2" quando len do email correspondente à variável "e" for diferente de "@"
            validarE2 += 1
        if (email[e] != "."):#Adiciona 1 à variável "validarE3" quando len do email correspondente à variável "e" for diferente de "."
            validarE3 += 1
        if (email[e] == " "):#Adiciona 1 à variável "validarE4" quando len do email correspondente à variável "e" for diferente de " "
            validarE4 += 1
    if(validarE3==len(email))or(validarE2==len(email))or(len(email)<8)or(validarE4!=0):#Comando que exige um email com mais do que 8 caracteres, além de conter "@" e "."
        print("Informação inválida!")
        email = str(input("➢ Email com mais do que oito caracteres (contendo '@' e '.' e sem espaço): "))#Comando que pede para o usuário reinserir seu email
        print(" ")
        e = 0#Zera a variável "e"
        validarE2 = 0#Zera a variável "validarE2"
        validarE3 = 0#Zera a variável "validarE3"
        validarE4 = 0#Zera a variável "validarE4"
    else:#Comando que adiciona 1 à variável "validarE" quando o email é válido, parando o while
        validarE += 1
                    
Front(2)#Comando que mostra o front-end quando F1 vale 2

for w in range (12):#Comando que pede as notas de cada matéria (se repete 12 vezes)
    print(("Informe suas notas semestrais de %s" %(materias[w])).center(134, "-"))#Mostra o nome da matéria cuja nota deve ser inserida
    print(" ")
    for wh in range (2):#Comando que pede as notas semestrais de cada matéria (se repete 2 vezes)
        nota1 = float(input("➤ Insira sua nota do %s semestre: " %(semestres[wh])))#Comando que pede a nota para o usuário
        if(nota1<0)or(nota1>50):#Comando que pula uma linha quando a nota é inválida
            print(" ")
        while(nota1<0)or(nota1>50):#Comando que exige uma nota entre 0 e 50
            print("Informação inválida!")
            nota1 = float(input("➢ Insira uma nota entre zero e cinquenta: "))#Comando que pede a nota para o usuário
            if(nota1<0)or(nota1>50)or(wh==0):#Comando para pular linha quando a nota é inválida ou quando está na primeira repetição do for
                print(" ")
        nota = int(nota1)#Variável que recebe a parte inteira da nota digitada
        if(nota1-nota>=0.5):#Adiciona 1 à variável da nota inteira quando a ela subtraída da nota digitada tem como resto um número maior ou igual a 0.5
            nota += 1
        if(wh==0):#Adiciona a nota digitada à lista do primeiro semestre na primeira repetição do for
            primeiroS.append(nota)
        elif(wh==1):#Adiciona a nota digitada à lista do segundo semestre na segunda repetição do for
            segundoS.append(nota)
        soma += nota#Adiciona a nota inteira à variável soma
    print(" ")
    print(" ")
    medias.append(soma)#Adiciona a variável soma à lista "médias"
    if(soma<60):#Adiciona a soma à lista "reprovacao" quando ela é menor que 60, também adicionando esse status à lista "statusM"
        reprovacao.append(materias[w])
        statusM.append("Reprovado.")
    elif(soma>=60)and(soma!=100):#Adiciona a soma à lista "statusM" quando ela é maior ou igual a 60 e diferente de 100
        statusM.append("Aprovado.")
    elif(soma==100):#Adiciona a soma à lista "statusM" quando ela é igual a 100
        statusM.append("Aprovado com distinção.")
    soma = 0#Zera a variável soma
    wh = 0#Zera a variável wh

media_geral = (sum(medias)/len(medias))#Calcula a média das notas finais em todas as disciplinas

def status (S):#Função que gera a situação final do aluno
    if (S==0):#Define a situação como "Aprovado!" quando S vale 0
        return "Aprovado."
    elif (S==1):#Define a situação como "Aprovado com uma dependência!" com uma dependencia quando S vale 1
        return "Aprovado com uma dependência."
    elif (S==2):#Define a situação como "Aprovado com duas dependências!" quando S vale 2
        return "Aprovado com duas dependências."
    elif (S>2):#Define a situação como "Reprovado!" quando S vale 3
        return "Reprovado."
    
colunas = [
    ["-Matéria-","-S1-","-S2-","-Nota Final-","-Status-"],
    [materias[0],primeiroS[0],segundoS[0],medias[0],statusM[0]],
    [materias[1],primeiroS[1],segundoS[1],medias[1],statusM[1]],
    [materias[2],primeiroS[2],segundoS[2],medias[2],statusM[2]],
    [materias[3],primeiroS[3],segundoS[3],medias[3],statusM[3]], 
    [materias[4],primeiroS[4],segundoS[4],medias[4],statusM[4]],
    [materias[5],primeiroS[5],segundoS[5],medias[5],statusM[5]],
    [materias[6],primeiroS[6],segundoS[6],medias[6],statusM[6]],
    [materias[7],primeiroS[7],segundoS[7],medias[7],statusM[7]],
    [materias[8],primeiroS[8],segundoS[8],medias[8],statusM[8]],
    [materias[9],primeiroS[9],segundoS[9],medias[9],statusM[9]],
    [materias[10],primeiroS[10],segundoS[10],medias[10],statusM[10]],
    [materias[11],primeiroS[11],segundoS[11],medias[11],statusM[11]]
]#Comando que define as colunas do boletim, com as matérias e suas respectivas notas do primeiro e segundo semestre, nota final e status
   
#Saída de dados

Front(3)#Comando que mostra o front-end quando F1 vale 3

print("⮞ Nome do estudante: %s." %(nome))#Comando que mostra o nome do aluno
print("⮞ CPF: %s.%s.%s-%s." %(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:11]))#Comando que mostra o CPF do aluno em seu formato padrão
print("⮞ RG: %s." %(identidade))#Comando que mostra a identidade do aluno
print("⮞ CEP: %s-%s." %(cep2[:5],cep2[5:8]))#Comando que mostra o CEP do aluno em seu formato padrão
print("⮞ Email do aluno: %s." %(email))#Comando que mostra o email do aluno

Front(4)#Comando que mostra o front-end quando F1 vale 4

print((tabulate(colunas, tablefmt = "fancy_grid", stralign = "center")))#Mostra a o boletim (tabela com as matérias, notas e status)
    
print(" ")
print("⮞ Média total: %.2f." %(media_geral))#Comando que mostra a média geral do aluno
print("⮞ Situação: %s" %(status(len(reprovacao))))#Comando que mostra a situação final do aluno (status em função do len da lista "reprovacao")
