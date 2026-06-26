import os
import tweepy
import codecs
import tempfile
from tkinter import *
import threading
import tkinter as tk

BG_MAIN = "#121214"      
BG_CARD = "#1a1a1e"      
TEXT_MAIN = "#e2e8f0"    
TEXT_MUTED = "#94a3b8"   
ACCENT_BLUE = "#3b82f6"  
ACCENT_GREEN = "#10b981" 
ACCENT_RED = "#ef4444"   

FONT_TITLE = ("Segoe UI", 20, "bold")
FONT_SUB = ("Segoe UI", 11, "bold")
FONT_BODY = ("Segoe UI", 10)

def find_file(filename):
    for root, dirs, files in os.walk('.'):
        if filename in files:
            return os.path.join(root, filename)

def exit_after_25_seconds():
    root = tk.Tk()
    root.iconbitmap("Configuration\BlackvariantButtonUiSystemFoldersDrivesSystem.ico")
    root.title('Countdown')
    root.geometry("280x150")
    root.configure(bg=BG_MAIN)
    root.resizable(False, False)
    
    title_lbl = tk.Label(root, text="Closing App In:", font=FONT_BODY, bg=BG_MAIN, fg=TEXT_MUTED)
    title_lbl.pack(pady=(25, 5))
    
    label = tk.Label(root, font=('Segoe UI', 36, 'bold'), bg=BG_MAIN, fg=ACCENT_BLUE)
    label.pack()
    
    def countdown():
        for i in range(25, 0, -1):
            label.config(text=str(i))
            root.update()
            root.after(1000)
        root.destroy()
    countdown()
    root.mainloop()
    os._exit(0)

t = threading.Thread(target=exit_after_25_seconds)
t.start()
lock_file = tempfile.NamedTemporaryFile(dir=tempfile.gettempdir(), delete=False)
try:
    lock_file_path = lock_file.name
finally:
    lock_file.close()

def twwet():
    file_path = find_file('Tweet_information.txt')
    
    gSS = Label(log_frame, text=f"📄 Info Path: {file_path}", bg=BG_CARD, fg=TEXT_MUTED, font=FONT_BODY)
    gSS.pack(anchor='w', padx=15, pady=2)
    
    try:
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_info_text = f.readlines()
            
            API_KEY = file_info_text[3].strip()
            API_SECRET_KEY = file_info_text[4].strip()
            Bearer_Token = file_info_text[5].strip()
            ACCESS_TOKEN = file_info_text[6].strip()
            ACCESS_TOKEN_SECRET = file_info_text[7].strip()
            Tweet_Text = ''.join(file_info_text[8:])
            
            am = Label(log_frame, text=f"📝 Text: {Tweet_Text.strip()}", bg=BG_CARD, fg=TEXT_MAIN, font=FONT_BODY, justify=LEFT, wraplength=520)
            am.pack(anchor='w', padx=15, pady=8)
            
            auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            client = tweepy.Client(Bearer_Token, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)
            
            file_path = find_file('pic.jpeg')
            gSAS = Label(log_frame, text=f"🖼️ Media Path: {file_path}", bg=BG_CARD, fg=TEXT_MUTED, font=FONT_BODY)
            gSAS.pack(anchor='w', padx=15, pady=2)

            if file_path:
                upload_img = api.media_upload(file_path).media_id_string
                client.create_tweet(text=Tweet_Text, media_ids=[upload_img])
                a = ' Your tweet with image was successfully sent!'
                b = Label(log_frame, fg=ACCENT_GREEN, bg=BG_CARD, text=a, font=FONT_SUB)
                b.pack(anchor='w', padx=15, pady=5)
            else:
                client.create_tweet(text=Tweet_Text)
                a = ' No picture found. Tweeted text only!'
                b = Label(log_frame, fg=ACCENT_BLUE, bg=BG_CARD, text=a, font=FONT_SUB)
                b.pack(anchor='w', padx=15, pady=5)
                
            file_path = find_file('result.txt')
            knm = Label(log_frame, text=f"📁 Result Path: {file_path}", bg=BG_CARD, fg=TEXT_MUTED, font=FONT_BODY)
            knm.pack(anchor='w', padx=15, pady=2)
            
            message = 'Tweeted'
            with codecs.open(file_path, 'r+', encoding='utf-8') as file:
                file.seek(0)
                file.truncate()
                file.write(message)
                
            k = Label(log_frame, text=f"Status: {message}", bg=BG_CARD, fg=ACCENT_GREEN, font=FONT_BODY)
            k.pack(anchor='w', padx=15, pady=2)
        else:
            acbv = ' Tweet_information.txt not found!'
            file_path = find_file('result.txt')
            with codecs.open(file_path, 'r+', encoding='utf-8') as file:
                file.seek(0)
                file.truncate()
                file.write(acbv)
            bdc = Label(log_frame, fg=ACCENT_RED, bg=BG_CARD, text=acbv, font=FONT_SUB)
            bdc.pack(pady=10)
            
    except Exception as error:
        file_path = find_file('result.txt')
        message = error
        with codecs.open(file_path, 'r+', encoding='utf-8') as file:
            file.write(str(message))
        h = f" Error: {str(error)}"
        g = Label(log_frame, fg=ACCENT_RED, bg=BG_CARD, text=h, font=FONT_BODY, justify=LEFT, wraplength=520)
        g.pack(anchor='w', padx=15, pady=5)

window = Tk()
window.iconbitmap("Configuration\BlackvariantButtonUiSystemFoldersDrivesSystem.ico")
window.title('Client - TweeBot')
window.configure(bg=BG_MAIN)
window.resizable(False, False)

window.update_idletasks()
window_width = 580
window_height = 380
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = (screen_width // 2) - (window_width // 2)
center_y = (screen_height // 2) - (window_height // 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

Label(window, text='TweeBot', font=FONT_TITLE, bg=BG_MAIN, fg=ACCENT_BLUE).pack(pady=(15, 2))
Label(window, text='Automated Twitter Client', font=FONT_BODY, bg=BG_MAIN, fg=TEXT_MUTED).pack(pady=(0, 10))

log_frame = Frame(window, bg=BG_CARD, bd=1, relief=SOLID, highlightbackground="#2e2e33", highlightthickness=1)
log_frame.pack(fill=BOTH, expand=True, padx=20, pady=(0, 20))

file_path = find_file('result.txt')

with codecs.open(file_path, 'r+', encoding='utf-8') as file:
    if file.read() == '':
        file.write('1')

twwet()

window.after(7000, window.destroy)
window.mainloop()

