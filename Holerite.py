import datetime
import time


def lin():
    print("-"*50)


def hora_extra():
    salario = float(input(" Informe o seu Salario : ")) 
    vale = salario * 0.3 
    quantidade_he60 = int(input(" Informe a quantidade de hora extras 60%: ")) 
    quantidade_he100 = int(input(" Informe a quantidade de hora extras 100% :"))
    formula_he60 = salario/220*1.6 
    formula_he100 = salario/220*2 
    hora_extra60 = quantidade_he60 * formula_he60 
    hora_extra100 = quantidade_he100*formula_he100 
    total = hora_extra60 + hora_extra100  
    pagamento = salario + hora_extra60 + hora_extra100
    dias_uteis = float(input("Informe a quantidade de dias uteis: ")) 
    dias_nao_uteis = float(input("Informe a quantidade de domingos e feriados: ")) 
    dsr  = total / dias_uteis *dias_nao_uteis 
    print('\n Adiantamento no valor de  R${:.2f} \n '.format(vale)) 
    lin()

    
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
    print("\nObrigado por utilizar nossos serviços!\n")  
    despedir = datetime.datetime.now()
    if despedir.hour <=12 :  
        print("Tenha um bom dia!") 
    elif despedir.hour <=18 : 
        print("Tenha uma boa tarde!") 
    elif despedir.hour > 18 :
        print("Tenha uma boa noite! ") 
        





hora_extra() 
mensagem()

time.sleep(30) 

