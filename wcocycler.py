from ast import Break
import pyautogui
import time

loc = ''
pyautogui.size()  # current screen resolution width and height
(3840, 2160)
page_number = ''
class Function:

    def cursloc(self):

        loc = pyautogui.position()
        print(f'{loc}')
        self.xcor = loc[0]
        self.ycor = loc[1]

    def loop(self):
        
        page_number =  input('Number of Episodes/cycles?')
        page_number = int(page_number)
        countset =  input('where did we leave off?')
        countset = int(countset)
        uselessvar = input('press enter when cursor is over browser in taskbar')
        run.cursloc()
        
        
        pyautogui.click(x=self.xcor,  y=self.ycor, button='left')
        time.sleep(1)

        count = countset
        page_number = int(page_number)
        for i in range(page_number):
            if count <= page_number: 
                pyautogui.moveTo(x=1185, y=178)
                time.sleep(2)
                pyautogui.leftClick()
                pyautogui.scroll(-700)
                #test next ep location
                #break
                
                #video CLick
                pyautogui.moveTo(x=845, y=251)
                pyautogui.leftClick()
                pyautogui.rightClick()

                time.sleep(1)

                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.press('down')


                time.sleep(3)
                pyautogui.press('enter')

                time.sleep(3)

                print(f'{count}')
                pyautogui.keyDown('ctrl')
                pyautogui.press('a')
                #pyautogui.PAUSE = 1
                pyautogui.press('del')
                pyautogui.keyUp('ctrl')
                time.sleep(1)
                pyautogui.write(f'{count}') 
                pyautogui.press('enter')

                time.sleep(1)

                print(f'{count} completed')
                count = count + 1 

                time.sleep(1)
#next ep click
                pyautogui.click(x=1131, y=571, button='left')
                time.sleep(3)

            else:
                print('borked')
                break
 

start = input('Begin? (y/n): ')


if start == 'y':
    run = Function()
    run.loop()