'''Programa versão 2, para saber o lucro de corridas Uber, tirando gastos com combustível'''
from ast import Try
from ctypes.wintypes import SIZE
from sys import builtin_module_names
from turtle import color
from numpy import size
import requests
from tkinter import *
import tkinter.font as tkFont


janela = Tk() # janela 

def botao_click ():
    print('Batao click')

    try : # Faz o tratamento para que se não for números ele irá aplicar uma mensagem !e assim voltar do início 
        kmRodado = float(entrada_texto.get())
        ganhosNaCorrida = float(entrada_texto2.get())
        consumo_por_km = float(entrada_consumo_por_km.get())
        preçoLitro = float(entrada_preco_por_litro.get())
        litros = 1.00
        consumo = litros / consumo_por_km
        totalConsumo = consumo * kmRodado
        totalGasto = preçoLitro * totalConsumo
        lucroFinal = ganhosNaCorrida - totalGasto

        resultado["text"] = (f'Consumo gasto por {kmRodado} km é : {totalConsumo:.2f} ml')
        resultado2["text"] = (f'Combustível gasto : R${totalGasto:.2f}')
        resultado3["text"] = (f'Lucro: R${lucroFinal:.2f}')
    except :
        resultado["text"] = ('Valor inválido, coloque apenas números !') 

       

fontStyle = tkFont.Font(family="Lucida Grande", size=7)
fontStyle_2 = tkFont.Font(family="Arial", size=12)
fontStyle_3 = tkFont.Font(family="Arial", size=9)

janela.title('Lucro de corridas')
janela.geometry('400x500+200+200')

texto_orientacao_1 = Label(master= janela, text='CALCULAR O LUCRO DA CORRIDA', font=fontStyle_2)
texto_orientacao_1.place(x = 60, y = 20)

texto_orientacao_1 = Label(master= janela, text='Digite os dados a baixo, para fazer o cálculo', font=fontStyle_3)
texto_orientacao_1.place(x = 65, y = 40)

texto_orientacao_1_2 = Label(master= janela, text='CONSUMO DO VEÍCULO', font=fontStyle)
texto_orientacao_1_2.place(x = 55, y = 89)

entrada_consumo_por_km = Entry(janela, text= 'Consumo do seu veiculo')
entrada_consumo_por_km.place(x = 180, y = 90)

texto_orientacao_2 = Label(master= janela, text='PREÇO DO COMBUSTÍVEL', font=fontStyle)
texto_orientacao_2.place(x = 50, y = 149)

entrada_preco_por_litro = Entry(janela, text= 'preço por litro')
entrada_preco_por_litro.place(x = 180, y = 150)

texto_orientacao_3 = Label(master= janela, text='KM PERCORRIDO', font=fontStyle)
texto_orientacao_3.place(x = 85, y = 199)

entrada_texto = Entry(janela, text= 'R$')
entrada_texto.place(x = 180, y = 200)


texto_orientacao_4 = Label(master= janela, text='LUCRO DA CORRIDA', font=fontStyle)
texto_orientacao_4.place(x = 70, y = 259)

entrada_texto2 = Entry(janela)
entrada_texto2.place(x = 180, y = 260)

botao = Button(janela, text="CALCULAR", width=20, command=botao_click)
botao.place(x= 100, y= 300)

resultado = Label(janela,font=fontStyle_3)
resultado.place(x = 70, y = 360)

resultado2 = Label(janela,font=fontStyle_3)
resultado2.place(x = 70, y = 380)

resultado3 = Label(janela,font=fontStyle_3)
resultado3.place(x = 70, y = 400)



janela.mainloop()