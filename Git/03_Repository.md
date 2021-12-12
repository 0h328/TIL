## 저장소 이동(Mirroring)

##### ``$ git clone --bare https://gitlab.com/<회원ID>/기존repo.git``

- gitlab (복사하려는 저장소)의 주소를 bare clone 하기

##### ``$ cd 기존repo.git``

##### ``$ git push --mirror https://github.com/<회원ID>/새로운repo.git``

- github (새로운 저장소)로 mirror push 하기



## git pull 에러 해결

에러명 : git pull 에러 해결방법 (Your local changes to the following files would be overwritten by merge )

##### ``$ git stash``

- 현재 디렉토리의 파일을 임시로 백업하고 깨끗한 상태로 돌린다.
- 버전관리 대상 파일들을 임시저장 해둔 상태
- 해당 명령어를 통해 현재 Staging 영역에 있는 파일의 변경사항을 스택에 넣어 둔다.

##### `` $ git pull origin master ``

- master에서 pull하여, 원격 저장소에서 내 로컬 브랜치로 변경사항을 적용한다.

##### ``$ git stash pop``

- 변경 사항을 적용하고, 스택에서 제거한다.

##### ``$ git stash && git pull origin master && git stash pop``

- 위에 3단계를 한번에 하는 기능



## 원격 저장소 병합

* 병합 명령어

```bash
# 병합할 저장소와 유지할 저장소에 동일한 이름의 파일이 없도록 한다. (README.md 등)

$ git remote add <병합할 저장소 이름> <병합할 저장소 주소>
$ git fetch <병합할 저장소 이름>
$ git merge --allow-unrelated-histories <병합할 저장소 이름>/<병합하고 싶은 branch 이름>
$ git remote remove <병합할 저장소 이름>
$ git commit -m "Merge : <병합할 저장소 이름> into <유지할 저장소 이름>"
```



- 커밋 로그를 병합하기 위해 병합할 원격 저장소를 <병합할 저장소 이름>으로 추가한다.

```bash
$ git remote add <병합할 저장소 이름> <병합할 저장소 주소>  # 기본 형태
$ git remote add pre https://github.com/... .../pre  # pre: 병합할 저장소 예시
```



- 원격 저장소에 저장된 커밋 기록들을 가져온다. (병합은 하지 않는다.)

```bash
$ git fetch <병합할 저장소 이름>
$ git fetch pre						# git pull = git fetch + git merge
```



- 연관이 없는 기록들을 병합한다.

```bash
$ git merge --allow-unrelated-histories <병합할 저장소 이름>/<병합하고 싶은 branch 이름>
$ git merge --allow-unrelated-histories pre/master
```



- 병합이 완료되었으니 병합된 원격 저장소를 지운다.

```bash
$ git remote remove <병합할 저장소 이름>
$ git remote remove pre
```



- 병합 완료된 로그를 커밋한다.

```bash
$ git commit -m "Merge : <병합할 저장소 이름> into <유지할 저장소 이름>"
```



