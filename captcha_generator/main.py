import PySimpleGUI as sg
from captcha.image import ImageCaptcha
from random import randint as rd

image = ImageCaptcha(width=280, height=90)
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
captcha_text = ''

sg.theme('DefaultNoMoreNagging')

layout = [
    [sg.Text('Responda o captcha abaixo')],
    [sg.Image(key='captcha_img')],
    [sg.Input('', size=(8, 1), key='captcha'), sg.Button(
        'Refresh', key='refresh'), sg.Button('Ok', key='send')],
]

window = sg.Window('Captcha', layout, finalize=True)


def captcha_generator():
    global captcha_text
    captcha_text = ''
    for each_letter in range(6):
        if rd(0, 1) == 0:
            captcha_text += alphabet[rd(0, len(alphabet) - 1)]
        else:
            captcha_text += alphabet[rd(0, len(alphabet) - 1)].upper()

    # print(captcha_text)
    image.write(captcha_text, 'captcha.png')


def program():
    while True:
        captcha_generator()
        window['captcha_img']('captcha.png')
        event, values = window.Read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        if event == 'refresh':
            window['captcha']('')
            captcha_generator()
            window['captcha_img']('captcha.png')

        if values['captcha'] == captcha_text and event != 'refresh':
            # print('ok')
            break
        else:
            print(values['captcha'])
            window['captcha']('')


program()
