import datetime
import time


def lin():
    print("-"*50)


def hora_extra():
    salario = float(input(" Informe o seu Salario : ")) # o valor de salario e dado pelo usuario
    vale = salario * 0.3 # vale é igual a 30% do salario
    quantidade_he60 = int(input(" Informe a quantidade de hora extras 60%: ")) 
    quantidade_he100 = int(input(" Informe a quantidade de hora extras 100% :"))
    formula_he60 = salario/220*1.6 #Descobrindo o valor da hora extra 60%
    formula_he100 = salario/220*2 #Descobrindo o valor da hora extra 100%
    hora_extra60 = quantidade_he60 * formula_he60 # Valor da hora extra 60% calculado em cima da quantidade feita
    hora_extra100 = quantidade_he100*formula_he100 # Valor da hora extra 1000% calculado em cima da quantidade feita
    total = hora_extra60 + hora_extra100  
    pagamento = salario + hora_extra60 + hora_extra100
    dias_uteis = float(input("Informe a quantidade de dias uteis: ")) #Quantidade de dias uteis trabalhados no mes
    dias_nao_uteis = float(input("Informe a quantidade de domingos e feriados: ")) # Quantidades de domingos e feriados trabalhados no mes
    dsr  = total / dias_uteis *dias_nao_uteis # Calcula o valor do dsr (descanso semanal remunerado)
    print('\n Adiantamento no valor de  R${:.2f} \n '.format(vale)) # Imprime o valor do vale
    lin()
    
    #Condições do INSS 2021
    
    if pagamento <= 1100.00: 
        desconto = pagamento * 0.075
        salario_bruto = pagamento - desconto - vale + dsr
        print('R$ {:.2f} em hora extra 60% '.format(hora_extra60))
        lin()
        print('R$ {:.2f} em hora extra 100%'.format(hora_extra100))
        lin()
        print("R$ {:.2f} Pagos de Descanso Semanal Remunerado".format(dsr))
        lin()
        print('R$ {:.2f} Recolhidos pelo INSS '.format(desconto))
        lin()
        print('Totalizando R$ {:.2f} de Salario Liquido '.format(salario_bruto))

    if pagamento <= 2203.45:
        desconto = pagamento * 0.09
        salario_bruto = pagamento  - desconto - vale + dsr
        print('R$ {:.2f} em hora extra 60% '.format(hora_extra60))
        lin()
        print('R$ {:.2f} em hora extra 100%'.format(hora_extra100))
        lin()
        print("R$ {:.2f} Pagos de Descanso Semanal Remunerado".format(dsr))
        lin()
        print('R$ {:.2f} Recolhidos pelo INSS '.format(desconto))
        lin()
        print('Totalizando R$ {:.2f} de Salario Liquido '.format(salario_bruto))


    elif pagamento <= 3305.22:  
        desconto = pagamento * 0.12
        salario_bruto = pagamento - desconto - vale + dsr
        print('R$ {:.2f} em hora extra 60% '.format(hora_extra60))
        lin()
        print('R$ {:.2f} em hora extra 100%'.format(hora_extra100))
        lin()
        print("R$ {:.2f} Pagos de Descanso Semanal Remunerado".format(dsr))
        lin()
        print('R$ {:.2f} Recolhidos pelo INSS '.format(desconto))
        lin()
        print('Totalizando R$ {:.2f} de Salario Liquido '.format(salario_bruto))


    elif pagamento <=6433.57 :
        desconto = pagamento * 0.14
        salario_bruto = pagamento - desconto - vale + dsr
        print('R$ {:.2f} em hora extra 60% '.format(hora_extra60))
        lin()
        print('R$ {:.2f} em hora extra 100%'.format(hora_extra100))
        lin()
        print("R$ {:.2f} Pagos de Descanso Semanal Remunerado".format(dsr))
        lin()
        print('R$ {:.2f} Recolhidos pelo INSS '.format(desconto))
        lin()
        print('Totalizando R$ {:.2f} de Salario Liquido '.format(salario_bruto))
        lin()


def mensagem():
    print("\nObrigado por utilizar nossos serviços!\n")  #Imprime uma mensagem de agradecimento
    despedir = datetime.datetime.now() #Define despedir com o horario do momento que esta sendo executado
    if despedir.hour <=12 :  #Se despedir for menor ou igual a 12
        print("Tenha um bom dia!") # imprime bom dia
    elif despedir.hour <=18 : # Se despedir for menor ou igual a 18
        print("Tenha uma boa tarde!") #Imprime boa tarde
    elif despedir.hour > 18 : #Se despedir for maior que 18
        print("Tenha uma boa noite! ") #imprime boa noite
        





hora_extra() 
mensagem()

time.sleep(30) #Programa fica aberto por 30 segundos

