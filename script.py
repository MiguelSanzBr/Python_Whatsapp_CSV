import pandas as pd
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pywhatkit as pwk
import phonenumbers

# NOMES DAS COLUNAS
########################
collMsg = 'menssage'
colTel = 'phone' 
######################

def validNumber(phone):
    try:
        pNum = phonenumbers.parse(phone)
        return phonenumbers.is_valid_number(pNum) and pNum.country_code == 55
    except phonenumbers.NumberParseException:
        return False
    
def enviarmsg(phone, menssage):
    if validNumber('+55' + str(phone)):
        pwk.sendwhatmsg_instantly('+55' + str(phone), menssage,tap_close=True)
    else: 
        print("{phone} não é valido ")    


def lercsv(archivo):
    df = pd.read_csv(archivo)
    columnas = df.columns.tolist()
    if colTel in columnas and collMsg in columnas:
        tell = df[colTel].tolist()
        msg = df[collMsg].tolist()

        for phone, menssage in zip(tell, msg):
            time.sleep(5)
            enviarmsg(phone, menssage)
            time.sleep(5)
            print(f"mensagem enviado a {phone}: {menssage}")
    else:
        print("O arquivo CSV não possui as colunas 'telefone' e 'mensagem'.")


Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    lercsv(archivo_csv)
else:
    print("Nenhum arquivo foi selecionado.")
