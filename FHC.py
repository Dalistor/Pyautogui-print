import pyautogui as py
from pynput import mouse

import time
import uuid
import os

area = []
run = True
def getParameters(x, y, button, pressed):
    global area
    global run

    if str(button) == 'Button.right':
        print('Preparado para nova captura!')
        run = True
        return

    if not run:
        return

    if pressed and len(area) < 2:
        area.append((x, y))

    if len(area) == 2:
        print(area)

        try:
            x1 = int(area[0][0])
            x2 = int(area[1][0])

            y1 = int(area[0][1])
            y2 = int(area[1][1])

            if x2 < x1:
                x = x2
                width = x1 - x2
            
            else:
                x = x1
                width = x2 - x1
            
            if y2 < y1:
                y = y2
                height = y1 - y2

            else:
                y = y1
                height = y2 - y1
            
            image = py.screenshot(region=(x, y, width, height))

            image.save(f'../../prints/{int(time.time())}_{uuid.uuid4()}.png')

            print('Imagem salva na pasta prints')
            area = []
            run = False
            print('Aperte o botão direito para uma nova captura')

        except Exception as e:
            print(f'Erro: {e}')


listener = mouse.Listener(on_click=getParameters)

if __name__ == '__main__':
    print('Clique em dois pontos da tela para fazer a área da imagem e avaliar a sua confidência.\n')
    input('Aperte Enter para iniciar.\n')
    listener.start()
    listener.join()