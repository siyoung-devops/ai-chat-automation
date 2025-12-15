from utils.headers import *


def test_search_agent_list(logged_in_agent):
    agent_page = logged_in_agent
    agent_page.go_to_agent_page()
    agent_page.search_input("project")
    result = agent_page.search_result()
    
    assert "project" in result.text.strip(), "PHC-TS06-TC001 : Test Fail"
    print("PHC-TS06-TC001 : Test Success")