import pyautogui as pya
import pandas as pd
import pyperclip
from time import sleep

pya.PAUSE = 1

pya.press('win')
pya.write('chrome')
pya.press('enter')
sleep(2)
pya.click(395, 442)
pya.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pya.hotkey('ctrl', 'v')
pya.press('enter')
sleep(5)
pya.click(346, 304, clicks=2)
sleep(2)
pya.click(406, 405, button='right')
pya.click(434, 650)
sleep(3)
pya.click(359, 48)
pyperclip.copy(r'C:\Users\rafae\Downloads')
pya.hotkey('ctrl', 'v')
pya.press('enter')
pya.click(507, 441)

tabela = pd.read_excel(r'C:\Users\rafae\Downloads\Vendas - Dez.xlsx')
faturamento = tabela['Valor Final'].sum()
qnt_produtos = tabela['Quantidade'].sum()

pya.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pya.hotkey('ctrl', 'v')
pya.press('enter')
sleep(5)
pya.click(117, 200)
pyperclip.copy('orafasouzacorrea@gmail.com')
pya.hotkey('ctrl', 'v')
pya.press('tab')
pya.write('FATURAMENTO E PRODUTOS VENDIDOS')
pya.press('tab')
pya.write(f'Faturamento: R${faturamento} \nProdutos vendidos: {qnt_produtos} \n\nAtt \nRafael')
sleep(1.2)
pya.click(846, 654)
