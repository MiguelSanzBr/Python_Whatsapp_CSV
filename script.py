import pandas as pd
import pywhatkit as pwk
import phonenumbers
import random
import pyautogui
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

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

def verifyLogin(driver):
    driver.get('https://web.whatsapp.com/')
    try:
        time.sleep(12)
        driver.find_element(By.XPATH, "//canvas[@aria-label='Scan me!']")
        print("Não está logado")
        print("Escaneie o QR Code,então precione Enter")
        input()
        return False
    except NoSuchElementException:
        return True



Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    
    # FIRE FOX 
    # servico = Service(GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=servico)
    
    while not verifyLogin(driver):
        pass
    lercsv(archivo_csv)
else:
    print("Nenhum arquivo foi selecionado.")
