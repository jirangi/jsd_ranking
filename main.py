import math
# ==========================================
# [추가됨] 변수명(Key) 추적 함수
# ==========================================
def find_key_path(data, target_value, current_path=""):
    """
    데이터(JSON) 안에서 특정 값(3443)을 가진 'Key(변수명)'를 찾아냅니다.
    """
    # 비교를 위해 목표값을 문자열(정수)로 변환 (예: 3443.85 -> "3443")
    target_str = str(target_value).split('.')[0] 

    if isinstance(data, dict):
        for k, v in data.items():
            # 경로 기록 (예: stats['attack'])
            new_path = f"{current_path}['{k}']" if current_path else k
            
            # 1. 값이 일치하는지 확인 (소수점 버리고 비교)
            try:
                if str(v).split('.')[0] == target_str:
                    print(f"\n" + "="*40)
                    print(f"🎉 찾았습니다! 범인은 바로 이 Key입니다: '{k}'")
                    print(f"📌 전체 경로: data[{new_path}]")
                    print(f"💰 실제 들어있는 값: {v}")
                    print("="*40 + "\n")
            except:
                pass
            
            # 2. 더 깊은 구조 탐색 (재귀)
            if isinstance(v, (dict, list)):
                find_key_path(v, target_value, new_path)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{current_path}[{i}]"
            find_key_path(item, target_value, new_path)
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
# print("🕵️‍♂️ 전체 데이터에서 값 '3443'을 가진 변수명(Key)을 수색합니다...")

# (중요) 여기에 실제 데이터 변수를 넣어야 합니다!
# 예를 들어, 위에서 data = response.json() 이라고 했다면 그대로 두시면 됩니다.
find_key_path(data, 3443)
if not found:
    print("\n😭 모든 곳을 뒤졌는데도 안 나옵니다...")
