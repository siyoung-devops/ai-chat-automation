from enum import Enum, auto


# 요즘엔 숫자를 쓰지않고 auto()를 쓴다고 한다.
class AIresponse(Enum):
    COMPLETED = auto()   # ai가 응답을 완료한 상태
    STOPPED = auto()     # 취소 버튼을 클릭한 상태
    TIMEOUT = auto()     # 무한 로딩 상태(15초 이상으로 기준)
    
class MenuStatus(Enum):
    OPENED = auto()
    CLOSED = auto()
    
class ModelBarStaus(Enum):
    EXPANDED = auto()   # 모델 선택창 확장
    COLLAPSED = auto()  # 모델 선택창 축소
    