import pandas as pd
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pywhatkit as pwk
import phonenumbers

def validNumber(phone):
    try:
        parsed_number = phonenumbers.parse(phone)
        return phonenumbers.is_valid_number(parsed_number) and parsed_number.country_code == 55
    except phonenumbers.NumberParseException:
        return False
    
def enviarmsg(phone, menssage):
    if validNumber('+55' + str(phone)):
        pwk.sendwhatmsg_instantly('+55' + str(phone), menssage)
    else: 
        print("{phone} não é valido ")    


def leercsv(archivo):
    df = pd.read_csv(archivo)
    columnas = df.columns.tolist()
    if 'phone' in columnas and 'menssage' in columnas:
        telefonos = df['phone'].tolist()
        mensajes = df['menssage'].tolist()
        for phone, menssage in zip(telefonos, mensajes):
            time.sleep(5)
            enviarmsg(phone, menssage)
            time.sleep(5)
            print(f"mensagem enviado a {phone}: {menssage}")
    else:
        print("O arquivo CSV não possui as colunas 'telefone' e 'mensagem'.")


Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    leercsv(archivo_csv)
else:
    print("Nenhum arquivo foi selecionado.")
