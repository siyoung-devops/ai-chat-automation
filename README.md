






📁 각 폴더에 대한 상세한 설명
- src/
    1. 자동화 프레임워크의 핵심 코드입니다. POM 클래스와 공통 유틸리티 함수 등 Selenium을 활용하여 UI 자동화에 필요한 코드들이 포함됩니다.
- tests/
    1. Pytest를 사용하여 작성된 실제 테스트 케이스가 위치하며, confest.py 파일을 통해 초기 설정을 관리합니다.
    2. confesrt.py를 기반으로 test_mai.py, test_login.py 등의 테스트를 진행합니다. 
- src/resources/assets 와 src/resources/testdata
    1. 테스트 수행에 필요한 데이터 파일, 이미지 등 리소스를 관리합니다.
    2. ex) user_data.json
- config/
    1. 환경별 URL, 브라우저 설정 등 다양한 환경 구성을 관리하는 설정 파일을 보관합니다.
- reports/
    1. 테스트 실행 결과로 생성된 HTML 보고서, 로그 파일, 실패 시 스크린샷 등을 저장합니다.
- pytest.ini
    1. Pytest 실행 시 적용할 옵션을 정의하는 설정 파일입니다. ex) 테스트 경로 지정, 마커 설정
    2. 현재 pythonpath = src로 지정되어, src 기준 임포트 가능하게 했습니다. 
- requirements.txt
    1. 프로젝트에서 사용하는 모든 Python 관련 설치 파일을 명시합니다.
- Jenkinsfile
    1. Jenkins CI/CD 파이프라인 정의로 Build, Test, Report 단계 등을 명시적으로 관리합니다.
- defines.py, headers.py
    1. 각자 찾은 selector, xpath와 헤더들을 따로 관리하기 위한 파일입니다. 
