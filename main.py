def on_button_pressed_a():
    global Cpt
    if Cpt <= MAX:
        # 10 est une constante est un magic number
        Cpt += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Cpt
    if Cpt > 0:
        Cpt += -1
input.on_button_pressed(Button.B, on_button_pressed_b)

MAX = 0
Cpt = 0
# déclaration de la variable et initialisation
Cpt = 0
MAX = 10
# valeur maximale dans le bus

def on_forever():
    basic.show_number(Cpt)
basic.forever(on_forever)
