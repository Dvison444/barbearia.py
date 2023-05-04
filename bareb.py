import tkinter as tk
import datetime

def calcular_preco():
    nome = entrada_nome.get()
    num_cortes = int(entrada_cortes.get())
    preco = 15
    
    if num_cortes == 1:
        mensagem_preco.configure(text=f"Seu corte, {nome} ficará normal!")
    elif num_cortes == 2:
        preco *= 0.85
        mensagem_preco.configure(text=f"{nome}, seu preço com desconto é R${preco:.2f}")
    elif num_cortes >= 3:
        mensagem_preco.configure(text=f"{nome}, seu corte de cabelo é grátis!")
        preco = 0

    # Gravar informações em um arquivo de texto
    with open("barbearia.txt", "a") as arquivo:
        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"{data_hora} - {nome} - {num_cortes} cortes - R${preco:.2f}\n")
        

janela = tk.Tk()
janela.title("Barbearia")

# Labels
tk.Label(janela, text="     Nome:").grid(row=0, column=0)
tk.Label(janela, text="      Quantidade de cortes no mês:").grid(row=1, column=0)
tk.Label(janela, text="      Preço:").grid(row=2, column=0)

# Entradas de texto
entrada_nome = tk.Entry(janela)
entrada_cortes = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)
entrada_cortes.grid(row=1, column=1)

# Botão calcular
botao_calcular = tk.Button(janela, text="Calcular preço", command=calcular_preco)
botao_calcular.grid(row=3, column=1)

# Mensagem de preço
mensagem_preco = tk.Label(janela, text="")
mensagem_preco.grid(row=2, column=1)

janela.mainloop()
