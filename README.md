<H3>카카오톡 예약전송 프로그램 with Python</H3>

***

<H3>사용된 주요 라이브러리</H3>
1. pyautogui & opencv - 현재 화면에서 이미지를 찾아 클릭, 마우스 제어, 키보드 제어 등<br>
2. schedule - 지정한 시간에 함수가 실행되도록 예약<br>
3. pyqt5 - 프로그램의 GUI 구성<br>
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
  <img style="margin-right: 10px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fvo79c%2Fbtrs2EV1ZTQ%2FAzsSk7tgF2F6YM3EHRriI1%2Fimg.png" width="32%" />
  <img style="margin-right: 10px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbp9HlA%2Fbtrs1SN3rHQ%2FWjOk6zSXkKC6YDRNYKKK2k%2Fimg.png" width="32%" />
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcyGwHr%2Fbtrs21QV3XM%2FA6oaAXrRejMuzIt4REuAmk%2Fimg.png" width="32%" />
</div>

<p>예약할 메세지 개수를 입력하면, 2번 그림과 같이 각 예약 별로 내용을 입력할 수 있도록 예약을 선택할 수 있습니다. 각 예약 별로 다른 채팅방에, 다른 내용으로, 다른 시간에 메세지를 전송할 수 있습니다. 오른쪽 위에 '전송 후 컴퓨터 종료' 를 체크하면 예약한 시간에 메세지가 전송된 후 컴퓨터가 종료됩니다. 내용을 다 입력했다면 Next 버튼을, 메세지 개수를 다시 입력하려면 Back 버튼을 누릅니다.</p>
<p>※ 시간은 24H 형식으로 입력합니다. 오전 8:30 -> 08:30, 오후 8:08 -> 20:08</p>
<p>※ 예를 들어 현재 시간이 10일 21:30분 인데 다음날 아침(11일) 08:30분에 메세지를 전송하고 싶다면 08:30으로 입력하시면 됩니다. 현재 시간 기준 이후로 입력한 시간을 만나면 메세지가 전송됩니다.</p>

<div style="text-align: center;">
  <img style="margin-right: 10px;" src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FION3y%2FbtrsY8RrvIM%2FSpvciZVl1FXHa0gCaEsre1%2Fimg.png" width="49%" />
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLxUSC%2Fbtrs2nG1Q14%2FhEszKybuYfGe0Pd3sQ8Vu1%2Fimg.png" width="49%" />
</div>

<p>내용을 모두 입력한 후 Next 버튼을 누르면 다음과 같이 확인하는 화면이 나옵니다. 예약 내역이 잘못되었다면 Back 버튼을 눌러 다시 내용을 입력하고, 이대로 예약하려면 Confirm 버튼을 누릅니다. Confirm을 누르면 오른쪽 사진과 같이 작은 확인 창이 뜨고 예약이 완료됩니다.</p>

***

<H3>프로그램 사용 시 주의사항! 🙆‍♂️</H3>
- Windows에서만 가능해요! 🙆‍♂️<br>
- 메세지 전송을 예약한 후 컴퓨터가 반드시 켜져있어야 해요! 🙆‍♂️ (절전, 시스템종료 X)<br>
- PC 카카오톡에 로그인 되어 있어야 해요! 🙆‍♂️<br>

***
<H3>py 파일 exe파일로 build하기</H3>

> github repository clone
>> git clone https://github.com/wadekang/ReservedKaKaoTalk.git

clone 한 후 카카오톡 예약전송.spec 파일의 workspace='YOUR WORK SPACE' 이 부분에서 YOUR WORK SPACE 부분을 해당 폴더 경로로 바꿔줍니다.

> pyinstaller 설치
>> pip install pyinstaller

> build exe file
>> pyinstaller --clean "카카오톡 예약전송.spec"

***
<H3>exe 실행파일 다운로드</H3>
- <a href="https://drive.google.com/file/d/1wUL1TMew9p-KXiZ6G1naLaxBlCzxzR6v/view?usp=sharing" target="_blank">프로그램 다운로드 링크</a>
