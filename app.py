import pyautogui
from time import sleep

# 1 - Clicar em cadastrar novo usuário
pyautogui.click(708,441, duration=2)
# 2 - Clicar e digitar meu usuario
pyautogui.click(692,387, duration=2) 
pyautogui.write('EmanuelaFC')
# 3 - Clicar e digitar minha senha
pyautogui.click(689,417,duration=2)
pyautogui.write('000000')
# 4 - Clicar em registrar novo usuário
pyautogui.click(596,440,duration=2)

# 5 - Clicar e digitar meu usuario
pyautogui.click(692,387,duration=2) 
pyautogui.write('EmanuelaFC')
# 6 - Clicar e digitar minha senha
pyautogui.click(689,417,duration=2)
pyautogui.write('000000')
# 7 - Clicar em entrar
pyautogui.click(596,440,duration=2)
# 8 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # 	1 - Clicar e digitar produto
        pyautogui.click(391,373,duration=2)
        pyautogui.write(produto)
        # 	2 - Clicar e digitar quantidade
        pyautogui.click(388,402,duration=2)
        pyautogui.write(quantidade)
        # 	3 - Clicar e digitar preço
        pyautogui.click(385,421,duration=2)
        pyautogui.write(preço)
        # 	# 4 - Clicar em registrar
        pyautogui.click(314,579,duration=1)
        sleep(1)