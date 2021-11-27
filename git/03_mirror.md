## 저장소 이동(Mirroring)

#### ``$ git clone --bare https://gitlab.com/<회원ID>/기존repo.git``

- gitlab (복사하려는 저장소)의 주소를 bare clone 하기

#### ``$ cd 기존repo.git``

#### ``$ git push --mirror https://github.com/<회원ID>/새로운repo.git``

- github (새로운 저장소)로 mirror push 하기

