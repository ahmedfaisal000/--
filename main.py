def on_gesture_logo_down():
    basic.show_number(ahmed1 - ahmed2)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    global ahmed1
    ahmed1 = 1
    basic.show_number(ahmed1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ahmed1, ahmed2
    ahmed1 = 0
    ahmed2 = 0
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_logo_up():
    basic.show_number(ahmed1 + ahmed2)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_b():
    global ahmed2
    ahmed2 = 1
    basic.show_number(ahmed2)
input.on_button_pressed(Button.B, on_button_pressed_b)

ahmed2 = 0
ahmed1 = 0
ahmed1 = 0
ahmed2 = 0