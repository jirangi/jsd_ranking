import math

def is_match(target_input, data_value):
    """
    target_input: 사용자가 입력한 목표값 (예: 3443)
    data_value: 게임 데이터에서 가져온 값 (예: 3443.85)
    """
    # 데이터가 없으면 False
    if data_value is None:
        return False

    # 모든 값을 문자열로 변환해 둡니다
    str_target = str(target_input).strip()
    str_data = str(data_value).strip()

    # ---------------------------------------------------
    # 방법 1: 소수점을 버리고 정수끼리 비교 (가장 추천)
    # ---------------------------------------------------
    try:
        # 데이터를 실수(float)로 바꾼 뒤 정수(int)로 내림 처리
        # 예: 3443.85 -> 3443
        num_target = int(float(str_target))
        num_data = int(float(str_data))
        
        if num_target == num_data:
            return True
    except ValueError:
        pass  # 숫자가 아닌 경우(이름 등)는 넘어갑니다

    # ---------------------------------------------------
    # 방법 2: 문자열 포함 여부 확인 (보조 수단)
    # ---------------------------------------------------
    # 예: "전투력 3443.85" 라는 문자에 "3443"이 들어있는지 확인
    if str_target in str_data:
        return True

    return False

# ==========================================
# 실행 테스트
# ==========================================
target = 3443
game_data_list = [
    {"name": "아크 패시브", "value": None},
    {"name": "각인", "value": "원한"},
    {"name": "전투 특성", "value": 3443.85},  # 여기가 문제였던 부분!
]

print(f"🎯 목표값: {target} (전투력)\n")

found = False
for item in game_data_list:
    category = item['name']
    value = item['value']
    
    print(f"🔎 [{category}] 검사 중... (값: {value})")
    
    # 수정된 함수로 비교!
    if is_match(target, value):
        print(f"✅ 찾았습니다!! -> {category}: {value}")
        found = True
        break
    else:
        print(f"❌ 없음")

if not found:
    print("\n😭 모든 곳을 뒤졌는데도 안 나옵니다...")
