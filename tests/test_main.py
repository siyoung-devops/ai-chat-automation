from utils.headers import *


def test_main(main_page, fm):
    main_page.go_to_main_page()

    # 임시 코드
    user_data = fm.read_json_file("user_data.json")
    print(user_data)
    
    