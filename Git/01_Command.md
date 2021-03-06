## 사용자 정보 설정

```
$ git config --global user.name <이름>
$ git config --global user.email <이메일>
```
- git 설치 이후, 사용자 이름과 이메일 주소를 딱 한번만 설정
- git은 커밋할 때마다 이 정보를 사용
- 프로젝트마다 다른 이름과 이메일 주소를 사용해야 한다면 ``--global`` 빼고 실행   

##### ``$ git init``
- 기존 폴더를 저장소로 이동시켜 관리할 수 있게 해준다.
- 업그레이드 하고 싶은 폴더에 들어가서 ``$ git init``을 하면 저장소로 이동되어 관리된다.
- 이미 ``$ git init`` 한 폴더 안에서는 또 ``$ git init`` 을 하지 않는다.   

##### ``$ git add``
- 작업공간 -> 스테이징
- 디렉토리 내 일부 파일 -> 스테이징 : ``$ git add <파일/디렉토리 경로>`` 
- 디렉토리 내 모든 파일 -> 스테이징 : ``$ git add .``

##### ``$ git commit -m <내용>``
- 스테이징 -> 로컬 저장소
- ``$ git commit -a``은 ``$ git add``와 ``$ git commit -m <내용>``이 합쳐진 것으로 바로 저장소로 이동

##### ``$ git status``
- 작업공간에서의 현재 파일 상태 확인 (변경 내역 확인)

##### ``$ git log``
- 저장소 내 커밋들을 확인할 수 있는 명령어

##### ``$ git push``
- 로컬 저장소 -> 원격 저장소

##### ``$ git pull``
- 원격 저장소 -> 로컬 저장소

##### ``$ git remote add origin <remote URL>``
- 현재 작업 중인 저장소에 중앙 원격 저장소를 연결

##### ``$ git clone <HTTPS clone URL>``
- 원격 저장소의 내용을 개인 컴퓨터에 저장하여 작업 가능

