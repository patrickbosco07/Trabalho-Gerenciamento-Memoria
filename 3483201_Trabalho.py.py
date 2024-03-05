import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
memoria = [' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x']
#for i in range(100):
#    if(random.randint(0,11) >= 5):
#        memoria[i] = 'x'
#    else:
#        memoria[i] = ' ' 
#print(memoria)                             

#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):
    print(memoria[i], end="|")
print()
for i in range(20,40):
    print(memoria[i], end="|")
print()
for i in range(40,60):
    print(memoria[i], end="|")
print()
for i in range(60,80):
    print(memoria[i], end="|")
print()
for i in range(80,100):
    print(memoria[i], end="|")
print()                                    
        

while (opcao != 4):
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    #Logica da quarta escolha
    if(opcao == 4):
        print('encerrando programa...')
        break                     
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()
    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        ini = 0
        while ini < 100:
            if memoria[ini] == ' ':
                print("Inicio", ini)	
                fim = ini + 1
                while fim < 100:
                    if memoria[fim] != ' ':
                        break
                    fim += 1
                print("Fim", fim)
                tamanhoburaco = fim - ini
                print("Tamanho buraco", tamanhoburaco)
                if tamanhoburaco >= tamanho:
                    print("Grande o suficiente") 
                    gravando = 0
                    while gravando >= ini and gravando < fim:
                        memoria[gravando] = letra
                        gravando += 1       
                    break
                else:
                    if omenorburaco < tamanho:
                        print("memória cheia")
                        break    
                ini = fim + 1
            ini += 1
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            ini = 0
            omenorburaco = 9999
            finaldomenorburaco = 0
            while ini < 100:
                if memoria[ini] == ' ':
                    print("Inicio", ini)	
                    fim = ini + 1
                    while fim < 100:
                        if memoria[fim] != ' ':
                            break
                        fim += 1
                    print("Fim", fim)
                    tamanhoburaco = fim - ini
                    print("Tamanho buraco", tamanhoburaco)
                    if tamanhoburaco >= tamanho:
                        if tamanhoburaco < omenorburaco:
                            omenorburaco = tamanhoburaco
                            iniciomenorburaco = ini
                            finaldomenorburaco = fim
                            if tamanhoburaco == tamanho:
                                break
                    ini = fim + 1
                ini += 1
            if omenorburaco >= tamanho:    
                for gravando in range(iniciomenorburaco, iniciomenorburaco + tamanho):
                    memoria[gravando] = letra                            
            else:
                if omenorburaco < tamanho:
                    print("memória cheia")
        else:
            if (opcao == 3):
                #Implemente aqui a lógica da pior escolha
                ini = 0
                omaiorburaco = 0
                finalomaiorburaco = 0
                while ini < 100:
                    if memoria[ini] == ' ':
                        print("Inicio", ini)	
                        fim = ini + 1
                        while fim < 100:
                            if memoria[fim] != ' ':
                                break
                            fim += 1
                        print("Fim", fim)
                        tamanhoburaco = fim - ini
                        print("Tamanho buraco", tamanhoburaco)
                        if tamanhoburaco >= tamanho:
                            if tamanhoburaco > omaiorburaco:
                                omaiorburaco = tamanhoburaco
                                iniciomaiorburaco = ini
                                finalomaiorburaco = fim
                                if tamanhoburaco == tamanho:
                                    break
                        ini = fim + 1
                    ini += 1
                if omaiorburaco >= tamanho:
                    gravando = 0
                    for gravando in range(iniciomaiorburaco, iniciomaiorburaco + tamanho):
                        memoria[gravando] = letra
                else:
                    if omaiorburaco < tamanho:
                        print("memória cheia")
    #Aqui você deve imprimir todo o conteúdo atualizado da variável memória                       
    print('Memória atualizada:')
    for i in range(0,20):
        print(memoria[i], end="|")
    print()
    for i in range(20,40):
        print(memoria[i], end="|")
    print()
    for i in range(40,60):
        print(memoria[i], end="|")
    print()
    for i in range(60,80):
        print(memoria[i], end="|")
    print()
    for i in range(80,100):
        print(memoria[i], end="|")
    print()                                
    
    
    
