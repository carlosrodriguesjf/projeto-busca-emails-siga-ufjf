#PROGRAMA BUSCA O NOME E EMAIL ATRAVÉS DA MATRÍCULA DO ALUNO

import pyautogui as pgui
import webbrowser
import pyperclip as pyp
from time import sleep

#1) Navegar até o site siga.ufjf.break

webbrowser.open('https://siga.ufjf.br')
sleep(3)

# 2) Encontrar o campo usuário e senha e entrar no site

pgui.tripleClick(480,472, duration=2)
cpf = pyp.copy('04746017654')
pgui.hotkey('ctrl','v')
sleep(1)
pgui.tripleClick(560,568, duration=2)
cpf = pyp.copy('Croc3887')
pgui.hotkey('ctrl','v')
sleep(1)

pgui.scroll(-100)
pgui.click(duration=2)
sleep(2)

# 3) Acessar a página Acadêmico/Consultas/Consulta Alunos

pgui.click(88,339, duration=0.5)
sleep(2)
pgui.click(83,340, duration=0.5)
sleep(2)
pgui.click(197,331, duration=0.5)
sleep(2)

#4) Digitar a matrícula



matriculas = ['200550001','200550002','200550003','200550014','200550005','200550006','200550007','200550008','200550009',
'200550018','200550022','200550032']

for matricula in matriculas:
    pgui.tripleClick(37,312, duration=0.5)
    pyp.copy(matricula)
    pgui.hotkey('ctrl','v')
    sleep(1)
    pgui.click(51,337,duration=0.5)

    #5) Busca o nome
    sleep(1)
    pgui.tripleClick(52,412, duration=0.5)
    pgui.hotkey('ctrl','c')
    nome = pyp.paste()

    #6) Busca e copia o e-mail
    sleep(1)
    pgui.click(37,312, duration=0.5)
    pgui.scroll(-1000)

    pgui.tripleClick(797,223,duration=0.5)
    pgui.hotkey('ctrl','c')
    email = pyp.paste()
    print(f'{matricula} - {nome} - {email}')
    pgui.scroll(1000)