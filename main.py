from ast import Str
from tokenize import Double
import pyautogui 
import keyboard
import os
import time

i=0


def clear():
    os.system('cls')

def aototext():
    while 1:
        clear()
        print("자동을 입력 하실 문장을 입력 하세요(0 : 메인)\n\n")
        text = str(input())
        if text == '0':main()
        print("\n반복 횟수를 입력 해주세요(0일 경우 무한 반복) : ")
        count = int(input())
        while 1:
            print("\n입력 주기를 입력해주세요 : ")
            times = float(input())

            if times < 0 :
                clear()
                print("입력 주기는 0보다 작을수 없습니다\n")
                print('다시 입력 해주세요')
            else: break
        
        print("f5을 누를 경우 시작 합니다")
        while 1:
            if keyboard.is_pressed('f5'):
                break 

        if count != 0:
            for i in range(0,count):
                if keyboard.is_pressed('f3'):
                    break
                
                print(f"출력 성공 : {text}")
                pyautogui.typewrite(text, interval=0.01)
                time.sleep(times)
                if keyboard.is_pressed('f3'):
                    break
                
        else:
            while 1:
                if keyboard.is_pressed('f3'):
                    break
                
                print(f"출력 성공 : {text}")
                pyautogui.typewrite(text, interval=0.01)
                time.sleep(times)
                if keyboard.is_pressed('f3'):
                    break
                
        
def aotohot():
    while 1:
        clear()
        test = [1]
        while 1:
            print("자동으로 눌러질 단축키를 선택 해주세요\n")
            print("0 : 메인화면\n")
            print("1 : 자동 저장\n")
            hotkey = int(input())
            if hotkey == 0:main()
            elif hotkey in test:break
            else:
                clear()
                print("없는 기능 혹은 숫자를 선택 하셨습니다\n")
                print("다시 선택 해주세요\n")
                continue


        print("\n반복 횟수를 입력 해주세요(0일 경우 무한 반복) : ")
        count = int(input())
        while 1:
            print("\n입력 주기를 입력해주세요 : ")
            times = float(input())

            if times < 0 :
                clear()
                print("입력 주기는 0보다 작을수 없습니다\n")
                print('다시 입력 해주세요')
            else: break
        
        print("f5을 누를 경우 시작 합니다")
        while 1:
            if keyboard.is_pressed('f5'):
                break
        if count != 0:
            for i in range(0,count):
                if keyboard.is_pressed('f3'):
                    break
                
                if hotkey==1:
                    print("자동 저장")
                    pyautogui.hotkey('Ctrl','s')
                time.sleep(times)
        else:
            while 1:
                if keyboard.is_pressed('f3'):
                    break
                if hotkey==1:
                    print("자동 저장")
                    pyautogui.hotkey('Ctrl','s')
                time.sleep(times)

def main():
    clear()
    while 1:
        test = (1,2)
        print("1 : 자동 문장 입력\n")
        print("2 : 자동 단축키\n")
        print("본인이 원하는 작업의 숫자를 입력 해주세요")
        while 1:
            key = int(input())
            if key in test:
                break
            else:
                print("없는 기능 혹은 숫자 입니다 다시 입력 해주세요\n")
        clear()

        if key == 1 :
            print("문장 자동 입력 을 시작 합니다")
            time.sleep(2)
            aototext()
        elif key ==2 :
            print("자동 단축키를 시작 합나다")
            time.sleep(2)
            aotohot()

print("간단한 키보드 매크로\n\n")
time.sleep(2)
main()