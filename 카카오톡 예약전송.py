import os, time, sys
import pyautogui
import subprocess
import pyperclip
import schedule

def init():
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0.5
    
def kakao_run():
    kakao_path = 'C:/Program Files (x86)/Kakao/KakaoTalk/KakaoTalk.exe'
    
    try:
        subprocess.run(kakao_path)
    except Exception:
        print('[ERROR] Execute KaKaoTalk')
        raise
    
def img_click(img_file):
    img_path = os.path.join('img', img_file)
    location = pyautogui.locateCenterOnScreen(img_path, confidence=0.65)
    x, y = location
    
    pyautogui.moveTo(x, y)
    pyautogui.click()

def chatroom_search_and_enter(chatroom_name):
    pyperclip.copy(chatroom_name)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def send_message_and_exit(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.press('esc')

def reserved_transmission(info):
    chag_img = 'chat.png'
    search_img = 'search.png'
    
    kakao_run()
    
    img_click(chag_img)
    img_click(search_img)
    chatroom_search_and_enter(info['chatroom_name'])
    send_message_and_exit(info['msg'])
   
    return schedule.CancelJob

def main():
    init()
    num = pyautogui.prompt('예약할 메세지 개수를 입력하세요.', '카카오톡 예약전송')
    
    all_data = []
    for i in range(int(num)):
        chatroom_name = pyautogui.prompt('채팅방 이름을 입력하세요.', '카카오톡 예약전송')
        msg = pyautogui.prompt('내용을 입력하세요.', '카카오톡 예약전송')
        reserved_time = pyautogui.prompt('예약할 시간을 입력하세요. (ex: 16:30)', '카카오톡 예약전송')
        
        info = {}
        info['chatroom_name'] = chatroom_name
        info['msg'] = msg
        info['reserved_time'] = reserved_time
        
        all_data.append(info)
        
        schedule.every().day.at(reserved_time).do(reserved_transmission, info)
    
    shutdown = pyautogui.confirm('전송 후 컴퓨터를 종료할까요?', '카카오톡 예약전송', ['Yes', 'No'])
    alert_msg = '예약이 완료되었습니다.\n\n=====예약내역=====\n\n'
    
    for data in all_data:
        temp = '* 채팅방: ' + data['chatroom_name'] + ', 시간: ' + data['reserved_time'] + '\n'
        alert_msg += temp
        
    pyautogui.alert(alert_msg, '카카오톡 예약전송')
    
    while True:
        schedule.run_pending()
        time.sleep(10)
        
        all_jobs = schedule.get_jobs()
        if not all_jobs:
            if shutdown == 'Yes':
                os.system('shutdown -s -f')
            else:
                sys.exit()
    
if __name__ == '__main__':
    main()