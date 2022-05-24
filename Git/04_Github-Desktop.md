## 팀 프로젝트

Github-Desktop을 활용하여 팀 프로젝트를 하는 경우 내용 정리 📁



##### 머지 충돌 방지 😫

- 작업한 브랜치 위치에서 ``commit`` and ``push``
- merge할 브랜치로 가서 ``pull``
- 작업한 브랜치로 돌아와서 bash에 ``git pull <merge할 브랜치>``
- 작업한 브랜치에서 ``push``
- 작업한 브랜치를 merge



##### 예시 ✏

merge할 브랜치 : Front_develop

내가 작업한 브랜치 : feat/main

- feat/main에서 ``commit`` & ``push``
- Front_develop에서 ``pull``
- feat/main에서 bash(터미널)에 ``git pull origin Front_develop``
- feat/main에서 ``push``
- 작업한 브랜치를 merge