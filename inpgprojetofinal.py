#modulos
import time
#informações dos blocos
def printtexto(texto):
    f = open(texto, 'r', encoding='utf-8')
    print(f.read())
    f.close()
def espera(segundos):
    time.sleep(segundos)
#apresentação
dados_para_contato=dict()
print(".........................\033[;1mOlá, essa é sua nave de exploração espacial 🚀\033[m .............................")
print(":.Aqui iremos inciar nossa jornada em exploração ao que há de mais incrivel fora de nossa atmosfera.:\n")
print("Mas antes, precisamos saber quem é nosso explorador...")
time.sleep(3)
#coleta de dados do usuário
dados_para_contato["Nome do Explorador"]=input("Qual seu nome?: ")
dados_para_contato["Idade do Explorador"]=int(input("Qual sua idade?: "))
dados_para_contato["Email para contato"]=input("Qual seu Email (Manteremos contato): ")
print("Preparado para sua jornada?! \n\033[;1mCarregando sua nave...\033[m")
time.sleep(2)
#processamento e sáida
cont = 0
while True:
    if cont == 0:
        escolha=int(input("\033[;1m|Esses são seus destinos de exploração!\033[;1m [recomedamos seguir pela ordem numérica]\n"
                          "Começe digitando o número correspondente a seu destino\n\n"
                          "[1]Sol-------[2]Mercurio------>[3]Vênus-----┐\n"
                          "                                            |\n"
                          "┌-[6]Saturno------[5]Jupiter-----[4]Marte---┘\n"
                          "|                                             "
                        "\n└------[7]Urano------[8]Netuno------[9]Plutão\n\n"
                          "Resposta: "))
    elif cont >= 1:
        continue1 = input("Deseja continuar explorando?\n"
                          "[se sim responda S]"
                          "[se não responda N]: ")
        if continue1 == "S":
            escolha = int(
                input(
                    "\033[;1m|Esses são seus destinos de exploração!\033[;1m [recomedamos seguir pela ordem numérica]\n"
                    "Começe digitando o número correspondente a seu destino\n\n"
                    "[1]Sol-------[2]Mercurio------>[3]Vênus-----┐\n"
                    "                                            |\n"
                    "┌-[6]Saturno------[5]Jupiter-----[4]Marte---┘\n"
                    "|                                             "
                    "\n└------[7]Urano------[8]Netuno------[9]Plutão\n\n"
                    "Resposta: "))
        elif continue1 == "N":
            print("\033[;1mObrigado por explorar conosco!\033[m")
            break
        else:
            print("\033[31mRespostas não identificada, Tente novamente\033[m")
            continue
    cont += 1

    if escolha == 1:
        print("Carregando seu destino..., Aguarde enquanto sobrevoamos vênus e mercúrio!")
        espera(3)
        print("Enfim chegamos a nossa estrela!")
        printtexto(texto='sol.charm.txt')
        espera(10)
    elif escolha == 2:
        print("Carregando seu destino..., estamos nos aproximando cada vez mais do sol!")
        espera(3)
        printtexto(texto='mercurio.charm.txt')
        espera(10)
        continue
    elif escolha == 3:
        print("Carregando seu destino..., estamos indo ao planeta mais prórximo, não demoraremos ")
        espera(3)
        printtexto(texto='venus.charm.txt')
        espera(10)
        continue
    elif escolha == 4:
        print("Carregando seu destino..., indo para nosso planeta vizinho, não demoraremos muito")
        espera(4)
        printtexto(texto='marte.charm.txt')
        espera(10)
        continue
    elif escolha == 5:
        print("Carregando seu destino..., aguarde enquanto viajamos sobre o centurão de asteróides")
        espera(6)
        printtexto(texto='jupiter.charm.txt')
        espera(10)
        continue
    elif escolha == 6:
        print("Carregando seu destino..., Aguarde enquando sobrevoamos marte e jupiter!")
        espera(7)
        printtexto(texto='saturno.charm.txt')
        espera(10)
        continue
    elif escolha == 7:
        print("Carregando seu destino..., estamos indo para o final do sistema solar, podemos demorar um pouco")
        espera(8)
        printtexto(texto='urano.charm.txt')
        espera(10)
        continue
    elif escolha == 8:
        print("Carregando seu destino..., a distância é Grande. podemos demorar um pouco!")
        espera(9)
        printtexto(texto='netuno.charm.txt')
        espera(10)
        continue
    elif escolha == 9:
        print("Carregando seu destino..., Essa é nossa viagem mais longa, podemos demorar")
        espera(10)
        print("Ufa, até que enfim chegamos, ao fim do sistema solar!")
        printtexto(texto='plutao.charm.txt')
        espera(10)
        continue
    else:
        caso_erro=input("\033[31mResposta não identificada, Tente novamente\033[m")
        continue
