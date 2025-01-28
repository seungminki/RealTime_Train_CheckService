# RealTime_Train_CheckService (실시간 열차 조회 서비스)
제목: STT(Speech-To-Text)를 활용한 1호선 지하철 실시간 열차 조회 서비스   
의의: 천재교육 부트캠프 AI*빅데이터 서비스 개발자 양성 과정을 수강하면서 한 중간프로젝트로, 총 2명이 2주동안 진행함. STT를 메인으로 실생활에 접목할 수 있는 서비스를 만드는 것이 목표였음.  
프로젝트 소개: 서울특별시에서 제공하는 오픈 API를 사용하여 사용자가 마이크를 통해 문장(원하는 역, 방향 - 종로오가역 하행 열차 시간 알려줘)을 말하면 STT을 통해 글자로 옮기고 API에 보낼 값을 추출하여 받아온 결과 값을 화면에 띄울 수 있도록 하였습니다. STT 또한 오픈소스를 사용하므로 STT 그 자체의 성능보다는 API로 값을 보내기 전 최대한 정확도를 높일 수 있도록 (종로오가 -> 종로5가, 광 화문 -> 광화문)등의 후처리 작업을 하였습니다. 사용자별로 최근 조회 값을 볼 수 있도록 하거나, 가장 많이 조회가 되는 역을 상단에 띄울 수 있도록 To-BE를 위해 결과 값이 DB에 저장될 수 있도록 하였습니다.  
문제 정의:  
문제 해결:  
결과:  

![poster](./example.png)
1. "등록" 버튼은 음성을 넣어 조회할 수 있음
2. 임의 버튼은 문장을 임의대로 넣어 조회할 수 있음

## AWS EC2 내에서 서버 실행 방법
1. 인스턴스 생성
2. Key Pair 권한 설정 변경(microsoft account)
3. 보안 그룹 설정(5000, 80 port)
4. cmd 열기
5. User/rltmdals/.ssh/{Key pair 위치} 
6. 키 위치에서 "ssh -i ".pem" ubuntu@"
7. sudo apt update
8. sudo apt install python3
9. sudo apt install python3-pip
10. sudo apt install python3-venv
11. mkdir venvs
12. (ubuntu@jumpto:~/venvs$) python3 -m venv myproject
13. (ubuntu@jumpto:~/venvs/myproject/bin$) . activate
14. pip install wheel
15. pip install flask
16. pip install flask-migrate
17. pip install Flask-SQLAlchemy==2.5.1
18. pip list
```Python
Package            Version
------------------ ---------
alembic            1.10.1
certifi            2022.12.7
charset-normalizer 3.1.0
click              8.1.3
Flask              2.2.3
Flask-Migrate      4.0.4
Flask-SQLAlchemy   3.0.3
greenlet           2.0.2
idna               3.4
itsdangerous       2.1.2
Jinja2             3.1.2
Mako               1.2.4
MarkupSafe         2.1.2
pip                23.0.1
PyAudio            0.2.13
requests           2.28.2
setuptools         67.4.0
SQLAlchemy         2.0.3
typing_extensions  4.5.0
urllib3            1.26.14
Werkzeug           2.2.3
wheel              0.38.4
```
(버전을 잘 확인해볼것)


19. git clone "git-url" myproject
20. 환경변수 설정
```Python
export FLASK_APP=pybo
export FLASK_DEBUG=true
export FLASK_RUN_PORT=80
```
21. pybo 파일 윗단으로 이동하여
```Python
flask db init (데이터 베이스 초기화하는 명령어)
flask db migrate
flask db upgrade
```
23. sudo 권한없이 80번 포트로 바꾸는 법
```Python
sudo apt install authbind
sudo touch /etc/authbind/byport/80
sudo chmod 777 /etc/authbind/byport/80
authbind --deep flask run --host=0.0.0.0
```
22. pyaudio 설치 오류났을 때
```Python
pip list
pip install pyaudio - (error: subprocess-exited-with-error)라는 오류 발생
sudo apt-get install portaudio19-dev
pip install pyaudio (설치 성공)
pip list로 확인
```
