<H3>카카오톡 예약전송 프로그램 with Python</H3>

***

<H3>사용된 주요 라이브러리</H3>
1. PyAutoGui - 현재 화면에서 이미지를 찾아 클릭, 키보드, 마우스 제어 등<br>
2. Schedule - 설정한 시간에 따라 코드가 실행되도록 하는 라이브러리

***

<H3>프로그램 동작 프로세스</H3>
1. PyAutoGui Prompt를 통해 사용자로부터 예약할 메세지 개수, 각자의 채팅방 이름 및 내용, 예약할 시간을 입력받는다. <br><br>
<p align="center">
  <img src="https://images.velog.io/images/wadekang/post/a8d133f3-f88a-40b6-b7c5-4b04208dd4d0/%EB%A9%94%EC%84%B8%EC%A7%80%EA%B0%9C%EC%88%98.png" style="margin:20px auto"><br>
  <img src="https://images.velog.io/images/wadekang/post/11077137-905c-4270-8ca8-b3ecb3292cdc/%EC%B1%84%ED%8C%85%EB%B0%A9%20%EC%9D%B4%EB%A6%84.png" style="margin:20px auto"><br>
  <img src="https://images.velog.io/images/wadekang/post/ac800c8d-c7e1-4d1a-ba6f-1bef5e15dbc5/%EB%82%B4%EC%9A%A9.png" style="margin:20px auto"><br>
  <img src="https://images.velog.io/images/wadekang/post/9b2fc71d-0cfc-4649-bd69-21b0ce42e800/%EC%8B%9C%EA%B0%84%EC%9E%85%EB%A0%A5.png" style="margin:20px auto"><br>
  <img src="https://images.velog.io/images/wadekang/post/a894cff6-7b57-4954-83f9-8d84ecd62051/%EC%A2%85%EB%A3%8C.png" style="margin:20px auto"><br>
  <img src="https://images.velog.io/images/wadekang/post/bd349776-bba4-47cb-b548-72e1b1f2fc7e/%EC%99%84%EB%A3%8C.png" alt="text" width="number" style="margin:5px auto" /><br>PyAutoGui로 구현하여 디자인은 전혀,,,😅
</p>
2. 입력 받은 시간(현 시간 이후로 24시간 이내)을 기준으로 카카오톡 메세지 전송을 Schedule 한다.<br>
3. 시간이 되면 PC 카카오톡을 실행시켜 입력한 채팅방 검색 후 채팅방에 입장하여 메세지를 전송한다. 

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
- <a href="https://drive.google.com/file/d/1-P8NltULUfMU5JBZZ40Gw5uz1HyWG-qp/view?usp=sharing" target="_blank">프로그램 다운로드 링크</a>
