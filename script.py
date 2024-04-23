import pandas as pd
import pywhatkit as pwk
import phonenumbers
import random
import pyautogui
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# NOMES DAS COLUNAS
########################
colMsg = 'FRASE'
colTel= 'TEL' 
######################

def validNumber(phone):
    try:
        pNum = phonenumbers.parse(phone)
        return phonenumbers.is_valid_number(pNum) and pNum.country_code == 55
    except phonenumbers.NumberParseException:
        return False
def enviarmsg(phone, menssage):
    if validNumber('+55' + str(phone)):
        #time.sleep(random.randint(50,120))
        pwk.sendwhatmsg_instantly('+55' + str(phone), menssage)
        time.sleep(12)
        pyautogui.hotkey("ctrl", "w")
        pyautogui.press("enter")
        print(f"mensagem enviado a {phone}: {menssage}")
        #time.sleep(random.randint(50,120))
    else: 
        now = time.localtime()
        date = f"{now.tm_mday}/{now.tm_mon}/{now.tm_year}"
        hora = f"{now.tm_hour}:{now.tm_min}"
        with open('ERRO_NUMBER_DB.txt', 'a') as f:
            f.write(f"{phone} \n")
        print(phone,"error 404")   
    
def lercsv(archivo):
    df = pd.read_csv(archivo)
    columnas = df.columns.tolist()
    if colTel in columnas and colMsg in columnas:
        tell = df[colTel].tolist()
        msg = df[colMsg].tolist()
        for phone, menssage in zip(tell, msg):
            enviarmsg(phone, menssage)
    else:
        print(f"O arquivo CSV não possui as colunas '{colTel}' e '{colMsg}'.")

Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    lercsv(archivo_csv)
else:
    print("Nenhum arquivo foi selecionado.")
