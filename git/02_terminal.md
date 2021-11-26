## ``$ ls``
- 현재 위치한 폴더 내부의 파일/폴더 확인 


## ``$ ls -a``
- 현재 위치한 폴더 내부의 모든파일/폴더(숨김 포함) 확인

## ``$ touch <파일명>``
- <파일명>으로 파일 생성

## ``$ mkdir <폴더명>``
- <폴더명>으로 폴더 생성

## ``$ start <파일명>``
- <파일명> 실행

## ``$ rm -r <폴더명>``
- 지정한 폴더 및 파일 삭제

## ``$ rm -rf <폴더명>``
- 지정한 폴더 및 파일 강제 삭제


## ``$ cd``
- 지정 위치로 이동
- ``<폴더명>`` : 지정 폴더로 이동
- ``~`` : Home directory
- ``.`` : 현재 위치한 폴더
- ``..`` : 현재 위치한 폴더 기준으로 상위 폴더

```
user@DESKTOP-OCP1CDQ MINGW64 ~/00_yh/01_yh/02_yh (master) 
```
- 여기서 (master)는 repo(저장소)이다.

## ``$ ctrl + l``
- 터미널 창 정리

## ``$ pip list``
- 현재 어떤 패키지가 설치되어있는지 보여주는 명령어

## ``$ pip freeze > requirements.txt``
- ``requirements.txt`` 는 사용한 패키지들을 텍스트 형식으로 모음
- pip install을 설치한 모든 패키지 등을 저장하는 목록

## ``$ pip install -r requirements.txt``
- requirements.txt에 저장한 모든 패키지 목록들을 다운받아서 다른 환경에서도 그대로 사용

## ``$ python -m venv venv``
- 가상환경 설정

## ``$ source venv/Scripts/activate``
- 가상환경 활성화

## ``$ deactivate``
- 가상환경 비활성화