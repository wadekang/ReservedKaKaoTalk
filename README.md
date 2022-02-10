<H3>카카오톡 예약전송 프로그램 with Python</H3>

***

<H3>사용된 주요 라이브러리</H3>
1. pyautogui & opencv - 현재 화면에서 이미지를 찾아 클릭, 마우스 제어, 키보드 제어 등<br>
2. schedule - 지정한 시간에 함수가 실행되도록 예약<br>
3. pyqt5 - 프로그램의 GUI 구성
4. pyinstaller - py 파일을 exe 파일로 빌드

***

<H3>프로그램 사용법</H3>
<p align="center">
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbTkZi1%2Fbtrs3VJKR73%2FfzeA2kBWlZ7mVVrT7LVdXK%2Fimg.png" style="margin:20px auto">  
</p>
<p>exe 파일을 다운로드 받아 실행하면 다음과 같이 프로그램이 실행됩니다. (다운로드 링크는 아래에 있습니다.)</p>
<p align="center">
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAA7Xc%2Fbtrs2EIAGEq%2FkpyvPCc7LoixMS1fmCYhQK%2Fimg.png" style="margin:20px auto" width="300px">
</p>
<p>예약할 메세지 개수를 입력한 후 Start 버튼을 누르면 다음과 같이 내용을 입력할 화면이 나옵니다.</p>

<div style="text-align: center;">
  <img style="margin-right: 10px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fvo79c%2Fbtrs2EV1ZTQ%2FAzsSk7tgF2F6YM3EHRriI1%2Fimg.png" width="250px" />
  <img style="margin-right: 10px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbp9HlA%2Fbtrs1SN3rHQ%2FWjOk6zSXkKC6YDRNYKKK2k%2Fimg.png" width="250px" />
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcyGwHr%2Fbtrs21QV3XM%2FA6oaAXrRejMuzIt4REuAmk%2Fimg.png" width="250px" />
</div>

***

<H3>프로그램 사용 시 주의사항! 🙆‍♂️</H3>
- Windows에서만 가능해요! 🙆‍♂️<br>
- 메세지 전송을 예약한 후 컴퓨터가 반드시 켜져있어야 해요! 🙆‍♂️ (절전, 시스템종료 X)<br>
- PC 카카오톡에 로그인 되어 있어야 해요! 🙆‍♂️<br>
- 코드로 마우스, 키보드를 제어해서 메세지를 전송하는 방식이라 메세지를 전송하는 순간에는 다른 인터럽트를 주시면 안돼요! 🙅‍♂️<br> (예약한 시간까지는 괜찮아요! 작동되는 그 순간에만 가만히 두시면 됩니다!)<br>

***
<H3>py 파일 exe파일로 build하기</H3>

> pyinstaller 설치
>> pip install pyinstaller

> build exe file
>> pyinstaller -w -F "{filename}.py"

> 아이콘 넣을 때
>> pyinstaller -w -F --icon={iconfile_path} "{filename}.py"


***
<H3>exe 실행파일 다운로드</H3>
- <a href="https://drive.google.com/file/d/1-P8NltULUfMU5JBZZ40Gw5uz1HyWG-qp/view?usp=sharing" target="_blank">프로그램 다운로드 링크</a>
