## 저장소 이동(Mirroring)

#### ``$ git clone --bare https://gitlab.com/<회원ID>/기존repo.git``

- gitlab (복사하려는 저장소)의 주소를 bare clone 하기

#### ``$ cd 기존repo.git``

#### ``$ git push --mirror https://github.com/<회원ID>/새로운repo.git``

- github (새로운 저장소)로 mirror push 하기



## git pull 에러 해결

에러명 : git pull 에러 해결방법 (Your local changes to the following files would be overwritten by merge )

#### ``$ git stash``

- 현재 디렉토리의 파일을 임시로 백업하고 깨끗한 상태로 돌린다.
- 버전관리 대상 파일들을 임시저장 해둔 상태
- 해당 명령어를 통해 현재 Staging 영역에 있는 파일의 변경사항을 스택에 넣어 둔다.

#### `` $ git pull origin master ``

- master에서 pull하여, 원격 저장소에서 내 로컬 브랜치로 변경사항을 적용한다.

#### ``$ git stash pop``

- 변경 사항을 적용하고, 스택에서 제거한다.

#### ``$ git stash && git pull origin master && git stash pop``

- 위에 3단계를 한번에 하는 기능
