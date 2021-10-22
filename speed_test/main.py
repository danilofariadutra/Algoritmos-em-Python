import PySimpleGUI as sg
from speedtest import Speedtest

sg.theme('DarkGrey14')

layout = [
    [sg.Text('DOWNLOAD: '), sg.Text('', key='download')],
    [sg.Text('UPLOAD: '), sg.Text('', key='upload')],
    [sg.Button('Iniciar', size=(8, 2), key='begin')],
]

window = sg.Window('Medidor de velocidade',
                   layout, size=(300, 100), finalize=True)


def speed_test():
    global fDown, fUp
    test = Speedtest()

    down = test.download()
    rsDown = round(down)
    fDown = int(rsDown / 1e+6)

    upload = test.upload()
    rsUp = round(upload)
    fUp = int(rsUp / 1e+6)


while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'begin':
        try:
            speed_test()
            window['download'](str(fDown) + ' Mbps')
            window['upload'](str(fUp) + ' Mbps')
            #print(f'Velocidade de Download é {fDown} Mbps')
            #print(f'Velocidade de Upload é {fUp} Mbps')
        except:
            pass
