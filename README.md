---

## 프로젝트 소개
Selenium 기반 웹 자동화와 JSON 데이터 관리 기능을 제공하는 Python 프로젝트입니다.  

---

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
