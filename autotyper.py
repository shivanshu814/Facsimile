import pyautogui
import time
import tkinter as tk
import keyboard

def StartTyping(text, wait_time):
    time.sleep(wait_time)
    active_window = pyautogui.getActiveWindow()
    lines = text.splitlines()
    for line in lines:
        pyautogui.typewrite(line)
        pyautogui.press('enter')
        if keyboard.is_pressed('esc'):  
            break

def StartMachine():
    text = TextBox.get('1.0', 'end-1c')
    wait_time = int(WaitingTime.get())
    StartTyping(text, wait_time)

window = tk.Tk()

window.title("Shivanshu Facsimile") 

window.geometry("600x600")  
window.config(bg='#050000')  

window.resizable(True, True)  

Text = tk.Label(window, text="Enter Your Code Here:", font=("Handwritten", 14), bg='#050000', fg='white')
Text.pack(pady=10)

TextBox = tk.Text(window, height=10, width=50, font=("Handwritten", 14), bg='#050000', fg='white')
TextBox.pack(padx=18,pady=10)

Waiting = tk.Label(window, text="Waiting time (sec):", font=("Handwritten", 12), bg='#050000', fg='white')
Waiting.pack(pady=5)

WaitingTime = tk.Entry(window, font=("Handwritten", 14), bg='#050000', fg='white')
WaitingTime.pack(pady=10)

Start = tk.Button(window, text="Start Facsimile", font=("Handwritten", 14), command=StartMachine, bg='#f70505', fg='white')
Start.pack(pady=20,padx=50)

copyright_label = tk.Label(window, text="Created by Shivanshu Pathak", font=("Handwritten", 12), bg='#f7ef57', fg='red')
copyright_label.pack(side='bottom', pady=5)

window.mainloop()
