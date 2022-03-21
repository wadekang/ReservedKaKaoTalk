import sys, os, time
import pyautogui
import subprocess
import pyperclip
import schedule

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

num_reserved = None
chatroom = None
chatmsg = None
timelist = None
shutdown = None

icon_path = None
mainui = None
inputui = None
confirmui = None
chatimg = None
searchimg = None

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi(mainui, self)

        self.startButton.clicked.connect(self.start_program)
        
    def start_program(self):
        widget.addWidget(InputWindow(self.numReserve.value()))

        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedHeight(630)
        widget.setFixedWidth(470)
        
class InputWindow(QWidget):
    def __init__(self, numReserve):
        super().__init__()
        uic.loadUi(inputui, self)
        self.backButton.clicked.connect(self.back_button)
        self.nextButton.clicked.connect(self.next_button)

        self.numReserve = numReserve
        self.chatRoomList = ['']*(self.numReserve+1)
        self.chatMsgList = ['']*(self.numReserve+1)
        self.timeList = ['']*(self.numReserve+1)
        self.curIdx = 1
        for i in range(self.numReserve):
            self.messageSelect.addItem('예약 ' + str(i+1))

        self.messageSelect.activated[str].connect(self.message_select_activated)

    def back_button(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        widget.setFixedHeight(470)
        widget.setFixedWidth(470)

    def next_button(self):
        self.chatRoomList[self.curIdx] = self.chatroomName.toPlainText()
        self.chatMsgList[self.curIdx] = self.chatMessage.toPlainText()
        self.timeList[self.curIdx] = self.reservedTime.toPlainText()

        widget.addWidget(ConfirmWindow(self.numReserve, self.chatRoomList, self.chatMsgList, self.timeList, self.shutdownCheck.isChecked()))

        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setFixedHeight(300)
        widget.setFixedWidth(400)

    def message_select_activated(self, text):
        self.chatRoomList[self.curIdx] = self.chatroomName.toPlainText()
        self.chatMsgList[self.curIdx] = self.chatMessage.toPlainText()
        self.timeList[self.curIdx] = self.reservedTime.toPlainText()
        
        nextIdx = int(text.split()[1])
        self.chatroomName.setPlainText(self.chatRoomList[nextIdx])
        self.chatMessage.setPlainText(self.chatMsgList[nextIdx])
        self.reservedTime.setPlainText(self.timeList[nextIdx])

        self.curIdx = nextIdx

class ConfirmWindow(QWidget):
    def __init__(self, numReserve, chatRoomList, chatMsgList, timeList, shutdown):
        super().__init__()
        uic.loadUi(confirmui, self)
        self.backButton.clicked.connect(self.back_button)
        self.confirmButton.clicked.connect(self.confirm_button)

        self.alert_msg = '===========예약내역===========\n\n'
        for i in range(numReserve):
            temp = '* 채팅방: ' + chatRoomList[i+1] + ', 시간: ' + timeList[i+1] + '\n'
            self.alert_msg += temp

        self.alertMessage.setPlainText(self.alert_msg)

        self.numReserve = numReserve
        self.chatRoomList = chatRoomList
        self.chatMsgList = chatMsgList
        self.timeList = timeList
        self.shutdown = shutdown

    def back_button(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(self)
        widget.setFixedHeight(630)
        widget.setFixedWidth(470)

    def confirm_button(self):
        QMessageBox.information(self, '카카오톡 예약전송', '예약 되었습니다.')

        global num_reserved, chatroom, chatmsg, timelist, shutdown
        num_reserved = self.numReserve
        chatroom = self.chatRoomList
        chatmsg = self.chatMsgList
        timelist = self.timeList
        shutdown = self.shutdown

        app.exit()

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
    
def img_click(img_path):
    location = pyautogui.locateCenterOnScreen(img_path, confidence=0.75)
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
    kakao_run()
    
    img_click(chatimg)
    img_click(searchimg)
    chatroom_search_and_enter(info['chatroom_name'])
    send_message_and_exit(info['msg'])
   
    return schedule.CancelJob

def data_load():
    global icon_path, mainui, inputui, confirmui, chatimg, searchimg

    try:
        icon_path = os.path.join(getattr(sys, '_MEIPASS'), 'icon\paper-plane.png')
        mainui = os.path.join(getattr(sys, '_MEIPASS'), 'ui\mainui.ui')
        inputui = os.path.join(getattr(sys, '_MEIPASS'), 'ui\inputui.ui')
        confirmui = os.path.join(getattr(sys, '_MEIPASS'), 'ui\confirmui.ui')
        chatimg = os.path.join(getattr(sys, '_MEIPASS'), 'img\chat_focus_badge.png')
        searchimg = os.path.join(getattr(sys, '_MEIPASS'), 'img\search.png')

    except:
        icon_path = 'icon\paper-plane.png'
        mainui = 'ui\mainui.ui'
        inputui = 'ui\inputui.ui'
        confirmui = 'ui\confirmui.ui'
        chatimg = 'img\chat_focus_badge.png'
        searchimg = 'img\search.png'

def program_exited():
    global num_reserved, chatroom, chatmsg, timelist, shutdown
    if num_reserved is None or chatroom is None or chatmsg is None or timelist is None or shutdown is None:
        return True
    else:
        return False

if __name__ == "__main__" :
    data_load()

    app = QApplication(sys.argv)
    
    widget = QtWidgets.QStackedWidget()
    widget.setWindowTitle('카카오톡 예약전송')
    widget.setWindowIcon(QIcon(icon_path))

    startWindow = StartWindow()

    widget.addWidget(startWindow)

    widget.setFixedHeight(470)
    widget.setFixedWidth(470)
    widget.show()
    
    app.exec_()

    widget.hide()

    if program_exited():
        sys.exit()

    init()
    for i in range(num_reserved):
        chatroom_name = chatroom[i+1]
        msg = chatmsg[i+1]
        reserved_time = timelist[i+1]
        
        info = {}
        info['chatroom_name'] = chatroom_name
        info['msg'] = msg
        info['reserved_time'] = reserved_time
        
        schedule.every().day.at(reserved_time).do(reserved_transmission, info)

    while True:
        schedule.run_pending()
        time.sleep(5)
        
        all_jobs = schedule.get_jobs()
        if not all_jobs:
            if shutdown:
                os.system('shutdown -s -f')
            else:
                sys.exit()

