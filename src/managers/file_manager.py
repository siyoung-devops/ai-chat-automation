from utils.headers import *

## csv, json read / save 등 파일을 관리 하는 곳입니다. 

class FileManager:
    def __init__(self):
        # 현재 managers 폴더 경로
        current_dir = os.path.dirname(os.path.abspath(__file__))  # src/managers
        
        # src 폴더 경로
        self.src_dir = os.path.dirname(current_dir)
        
        # resources/testdata 폴더 경로
        self.resources_dir = os.path.join(self.src_dir, "resources", "testdata")

    def read_json_file(self, file_name:str):
        
        file_path = os.path.join(self.resources_dir, file_name)
        try: 
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"😵 {file_path} 파일을 찾을 수 없음")
            return None
        except json.JSONDecodeError:
            print(f"😵 {file_path} 파일이 올바른 JSON 형식이 아님")
            return None
    
    def save_json_file(self, file_name:str, data):
        file_path = os.path.join(self.resources_dir, file_name)
        try: 
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"{file_path} 저장 완료!!")
        except Exception as e:
            print(f"{file_path} 저장 실패!: {e}")