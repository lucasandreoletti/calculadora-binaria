import tkinter as tk
from tkinter import messagebox

def decimal_para_binario(decimal):
    return bin(decimal)[2:]

def decimal_para_hexadecimal(decimal):
    return hex(decimal).upper()[2:]

def decimal_para_octal(decimal):
    return oct(decimal)[2:]

def binario_para_decimal(binario):
    return int(binario, 2)

def hexadecimal_para_decimal(hexadecimal):
    return int(hexadecimal, 16)

def octal_para_decimal(octal):
    return int(octal, 8)

def adicao_binaria(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def subtracao_binaria(bin1, bin2):
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def multiplicacao_binaria(bin1, bin2):
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def divisao_binaria(bin1, bin2):
    if bin2 == '0':
        return "Erro: Divisão por zero"
    else:
        return bin(int(bin1, 2) // int(bin2, 2))[2:]

def limpar_campos():
    entry_decimal.delete(0, tk.END)
    entry_numero.delete(0, tk.END)
    entry_binario1.delete(0, tk.END)
    entry_binario2.delete(0, tk.END)
    resultado_binario.set("")
    resultado_hexadecimal.set("")
    resultado_octal.set("")
    resultado_decimal.set("")
    resultado_operacao.set("")

def converter_decimal():
    decimal = int(entry_decimal.get())
    resultado_binario.set(decimal_para_binario(decimal))
    resultado_hexadecimal.set(decimal_para_hexadecimal(decimal))
    resultado_octal.set(decimal_para_octal(decimal))

def converter_base():
    base = escolha_base.get()
    numero = entry_numero.get()
    if base == 'Binário':
        resultado_decimal.set(binario_para_decimal(numero))
    elif base == 'Hexadecimal':
        resultado_decimal.set(hexadecimal_para_decimal(numero))
    elif base == 'Octal':
        resultado_decimal.set(octal_para_decimal(numero))

def realizar_operacao():
    bin1 = entry_binario1.get()
    bin2 = entry_binario2.get()
    operacao = escolha_operacao.get()
    if operacao == 'Adição':
        resultado_operacao.set(adicao_binaria(bin1, bin2))
    elif operacao == 'Subtração':
        resultado_operacao.set(subtracao_binaria(bin1, bin2))
    elif operacao == 'Multiplicação':
        resultado_operacao.set(multiplicacao_binaria(bin1, bin2))
    elif operacao == 'Divisão':
        resultado_operacao.set(divisao_binaria(bin1, bin2))

def mostrar_erro():
    messagebox.showerror("Erro", "Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

# Criar janela principal
root = tk.Tk()
root.title("Calculadora Binária")

# Converter Decimal para Binário, Hexadecimal, Octal
frame_conversao_decimal = tk.LabelFrame(root, text="Decimal para Binário, Hexadecimal, Octal")
frame_conversao_decimal.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W+tk.E)

label_decimal = tk.Label(frame_conversao_decimal, text="Decimal:")
label_decimal.grid(row=0, column=0)
entry_decimal = tk.Entry(frame_conversao_decimal)
entry_decimal.grid(row=0, column=1)
botao_converter = tk.Button(frame_conversao_decimal, text="Converter", command=converter_decimal)
botao_converter.grid(row=0, column=2)

label_binario = tk.Label(frame_conversao_decimal, text="Binário:")
label_binario.grid(row=1, column=0)
resultado_binario = tk.StringVar()
entry_binario = tk.Entry(frame_conversao_decimal, textvariable=resultado_binario, state='readonly')
entry_binario.grid(row=1, column=1)

label_hexadecimal = tk.Label(frame_conversao_decimal, text="Hexadecimal:")
label_hexadecimal.grid(row=2, column=0)
resultado_hexadecimal = tk.StringVar()
entry_hexadecimal = tk.Entry(frame_conversao_decimal, textvariable=resultado_hexadecimal, state='readonly')
entry_hexadecimal.grid(row=2, column=1)

label_octal = tk.Label(frame_conversao_decimal, text="Octal:")
label_octal.grid(row=3, column=0)
resultado_octal = tk.StringVar()
entry_octal = tk.Entry(frame_conversao_decimal, textvariable=resultado_octal, state='readonly')
entry_octal.grid(row=3, column=1)

# Converter Binário, Hexadecimal, Octal para Decimal
frame_conversao_base = tk.LabelFrame(root, text="Binário, Hexadecimal, Octal para Decimal")
frame_conversao_base.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)

escolha_base = tk.StringVar(root)
escolha_base.set("Binário")
menu_base = tk.OptionMenu(frame_conversao_base, escolha_base, "Binário", "Hexadecimal", "Octal")
menu_base.grid(row=0, column=0)

label_numero = tk.Label(frame_conversao_base, text="Número:")
label_numero.grid(row=0, column=1)
entry_numero = tk.Entry(frame_conversao_base)
entry_numero.grid(row=0, column=2)

botao_converter_base = tk.Button(frame_conversao_base, text="Converter", command=converter_base)
botao_converter_base.grid(row=0, column=3)

label_resultado_decimal = tk.Label(frame_conversao_base, text="Resultado Decimal:")
label_resultado_decimal.grid(row=1, column=0)
resultado_decimal = tk.StringVar()
entry_resultado_decimal = tk.Entry(frame_conversao_base, textvariable=resultado_decimal, state='readonly')
entry_resultado_decimal.grid(row=1, column=1)

# Operações Aritméticas Binárias
frame_operacoes_binarias = tk.LabelFrame(root, text="Operações Aritméticas Binárias")
frame_operacoes_binarias.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W+tk.E)

label_binario1 = tk.Label(frame_operacoes_binarias, text="Binário 1:")
label_binario1.grid(row=0, column=0)
entry_binario1 = tk.Entry(frame_operacoes_binarias)
entry_binario1.grid(row=0, column=1)

label_binario2 = tk.Label(frame_operacoes_binarias, text="Binário 2:")
label_binario2.grid(row=1, column=0)
entry_binario2 = tk.Entry(frame_operacoes_binarias)
entry_binario2.grid(row=1, column=1)

escolha_operacao = tk.StringVar(root)
escolha_operacao.set("Adição")
menu_operacao = tk.OptionMenu(frame_operacoes_binarias, escolha_operacao, "Adição", "Subtração", "Multiplicação", "Divisão")
menu_operacao.grid(row=2, column=0)

botao_calcular = tk.Button(frame_operacoes_binarias, text="Calcular", command=realizar_operacao)
botao_calcular.grid(row=2, column=1)

label_resultado = tk.Label(frame_operacoes_binarias, text="Resultado:")
label_resultado.grid(row=3, column=0)
resultado_operacao = tk.StringVar()
entry_resultado = tk.Entry(frame_operacoes_binarias, textvariable=resultado_operacao, state='readonly')
entry_resultado.grid(row=3, column=1)

botao_limpar = tk.Button(root, text="Limpar", command=limpar_campos)
botao_limpar.grid(row=3, column=0, pady=10)

root.mainloop()
