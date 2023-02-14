import math
import PySimpleGUI as sg

# Define o estilo da janela
sg.theme("DarkBlue13")

# Define o estilo dos botões
button_style = {"font": ("Arial", 14),
                "size": (5, 2),
                "pad": (2, 2)}

# Define o layout da janela
layout = [[sg.InputText(size=(35, 1), key="-INPUT-")],
          [sg.Button("7", **button_style), sg.Button("8", **button_style), sg.Button("9", **button_style), sg.Button("/", **button_style), sg.Button("sqrt", **button_style)],
          [sg.Button("4", **button_style), sg.Button("5", **button_style), sg.Button("6", **button_style), sg.Button("*", **button_style), sg.Button("log", **button_style)],
          [sg.Button("1", **button_style), sg.Button("2", **button_style), sg.Button("3", **button_style), sg.Button("-", **button_style), sg.Button("sin", **button_style)],
          [sg.Button("0", **button_style), sg.Button(".", **button_style), sg.Button("C", **button_style), sg.Button("+", **button_style), sg.Button("cos", **button_style)],
          [sg.Button("(", **button_style), sg.Button(")", **button_style), sg.Button("pi", **button_style), sg.Button("tan", **button_style), sg.Button("=", **button_style)],
          [sg.Text(size=(35, 1), key="-OUTPUT-", font=("Arial", 14))]]

# Cria a janela a partir do layout
window = sg.Window("Calculadora Científica", layout)

# Loop principal da janela
while True:
    event, values = window.read()

    # Encerra o programa se a janela for fechada
    if event == sg.WINDOW_CLOSED:
        break

    # Atualiza a entrada de texto na janela
    if event in "0123456789.+-*/()":
        window["-INPUT-"].update(values["-INPUT-"] + event)
    elif event == "C":
        window["-INPUT-"].update("")
        window["-OUTPUT-"].update("")

    # Calcula o resultado da expressão
    if event == "=":
        try:
            result = eval(values["-INPUT-"])
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")

    # Realiza operações matemáticas especiais
    if event == "sqrt":
        try:
            result = math.sqrt(float(values["-INPUT-"]))
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")
    elif event == "log":
        try:
            result = math.log10(float(values["-INPUT-"]))
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")
    elif event == "sin":
        try:
            result = math.sin(float(values["-INPUT-"]))
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")
    elif event == "cos":
        try:
            result = math.cos(float(values["-INPUT-"]))
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")
    elif event == "tan":
        try:
            result = math.tan(float(values["-INPUT-"]))
            window["-OUTPUT-"].update(result)
        except:
            window["-OUTPUT-"].update("Erro")
    elif event == "pi":
        window["-INPUT-"].update(values["-INPUT-"] + str(math.pi))

# Fecha a janela
window.close()