#Bibliotecas importadas para poder ler a planilha e abrir no navegador (pois o Python não possui essas ações nativas)
import time
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Link do Rpa Challenge
link = 'https://www.rpachallenge.com'

#Instância do código que abre o navegador
browser = webdriver.Chrome()
browser.get ("https://www.rpachallenge.com")

#Leitura do arquivo Excel & Print da tabela no Terminal
df_tabela = pd.read_excel("challenge.xlsx")
print(df_tabela.info())


#Print das colunas do arquivo no Terminal
print("Nomes das Colunas:", df_tabela.columns)


        
        
#Localizador do elemento "Start"
iniciar_desafio = element = browser.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/div[2]/app-rpa1[1]/div[1]/div[1]/div[6]/button[1]")
iniciar_desafio.click()

#Função For Each que faz a leitura das informações da tabela (e coloca cada informação em sua respectiva row)
for i, row in df_tabela.iterrows(): 
    
 FirstName = row['First Name']
 LastName = row['Last Name ']
 Email = row['Email']
 Role = row['Role in Company']
 Company = row['Company Name']
 Phone = row['Phone Number']
 Address = row['Address']
 
 
 #Mapeamento da textbox de cada elemento do site (usando Xpath)
 digitar_nome = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
 digitar_nome.clear()
 digitar_nome.send_keys(FirstName)
 digitar_email = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
 digitar_email.clear()
 digitar_email.send_keys(Email)
 digitar_celular = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
 digitar_celular.clear()
 digitar_celular.send_keys(Phone)
 digitar_endereco = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
 digitar_endereco.clear()
 digitar_endereco.send_keys (Address)
 digitar_sobrenome = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
 digitar_sobrenome.clear()
 digitar_sobrenome.send_keys (LastName)
 digitar_emprego = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
 digitar_emprego.clear()
 digitar_emprego.send_keys (Company)
 digitar_cargo = element = browser.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
 digitar_cargo.clear()
 digitar_cargo.send_keys (Role)
 botao = element = browser.find_element(By.XPATH,"//input[@type='submit']")
 botao.click()
 #função time sleep para dar delay (ver o tempo de conclusão da automoção)
 time.sleep(0.5)










