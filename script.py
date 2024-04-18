import pandas as pd
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pywhatkit as pwk
import phonenumbers
import random

# NOMES DAS COLUNAS
########################
collMsg,colTel= 'menssage','phone' 
######################

def validNumber(phone):
    try:
        pNum = phonenumbers.parse(phone)
        return phonenumbers.is_valid_number(pNum) and pNum.country_code == 55
    except phonenumbers.NumberParseException:
        return False
    
def enviarmsg(phone, menssage):
    if validNumber('+55' + str(phone)):
        pwk.sendwhatmsg_instantly('+55' + str(phone), menssage)
        print(f"mensagem enviado a {phone}: {menssage}")
    else: 
        now = time.localtime()
        date = f"{now.tm_mday}/{now.tm_mon}/{now.tm_year}"
        hora = f"{now.tm_hour}:{now.tm_min}"
        with open('ERRO_NUMBER_DB.txt', 'a') as f:
            f.write(f"{phone} \n")

        print(phone,"não é valido")    


def lercsv(archivo):
    df = pd.read_csv(archivo)
    columnas = df.columns.tolist()
    if colTel in columnas and collMsg in columnas:
        tell = df[colTel].tolist()
        msg = df[collMsg].tolist()

        for phone, menssage in zip(tell, msg):
            time.sleep(random.randint(50,120))
            enviarmsg(phone, menssage)
            time.sleep(random.randint(50,120))
            
    else:
        print("O arquivo CSV não possui as colunas 'telefone' e 'mensagem'.")


Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    lercsv(archivo_csv)
else:
    print("Nenhum arquivo foi selecionado.")
