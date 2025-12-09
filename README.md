---

## 프로젝트 소개
Selenium 기반 웹 자동화와 JSON 데이터 관리 기능을 제공하는 Python 프로젝트입니다.  

---

# Git & GitHub 사용법 가이드

## 각자의 브랜치에서 코드를 수정하고 커밋할때 주의점
## master 브랜치로 병합하기 전에 꼭 팀원들에게 알려줘야 합니다! 

1. 커밋전에 항상 최신 master를 pull해서 받아주세요! <br>
git checkout master  <br>
git pull origin master <br>

2. 각자의 브랜치로 이동 <br>
git checkout 개인브랜치이름 <br>

3. merge해서 병합하기 <br>
git merge master <br>

4. 내 브랜치를 원격에 push해서 반영 <br>
git push origin 개인브랜치이름    <br>

이렇게 해야 conflit를 방지할 수 있어요!  <br>
master브랜치로 업데이트 받기전에 커밋하시면 큰1나요 <br>




# git사용시 유용한 것들
1. git checkout master <br>
2. 최근 커밋 확인 <br>
git log --oneline <br>
3. 변경 사항 비교 <br>
git diff <br>
4. 특정 커밋 되돌리기 <br>
git revert <commit_id>



---

## 설치
```bash

# 가상환경 생성 (Python 3.11.9 기준)
python -m venv .venv      
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 패키지 설치
pip install -r requirements.txt


## 기술 스택
Python 3.11
Selenium
webdriver-manager
JSON 데이터 처리

📁 각 폴더에 대한 상세한 설명
helpychat-project/
├─ reports/
│   ├─ logs/          # 테스트 실행 로그
│   └─ screenshots/   # 테스트 실패/성공 시 캡처된 스크린샷
│
├─ src/
│   ├─ config/        # 환경별 URL, 브라우저 옵션 등 설정 파일
│   ├─ managers/      # DriverManager, FileManager 등 관리 클래스
│   ├─ pages/         # Page Object Model(POM) 클래스
│   ├─ resources/     # 테스트 데이터 및 이미지 리소스
│   └─ utils/         # 공통 유틸리티 함수 및 도구
│       ├─ defines.py # Selector, XPath 등 관리
│       └─ headers.py # 헤더 정보 관리
├─ tests/
│   ├─ conftest.py    # 테스트 초기 설정 관리(fixture 등)
│   └─ test_main.py   # 실제 Pytest 테스트 케이스
│
├─ pytest.ini          # Pytest 실행 옵션 (ex: pythonpath=src)
├─ requirements.txt    # 프로젝트 Python 패키지 명시
└─ Jenkinsfile         # CI/CD 파이프라인 정의
