import math

# ==========================================
# 1. 비교 로직 함수 (is_match)
# ==========================================
def is_match(target_input, data_value):
    """
    값 비교 함수
    target_input: 찾는 값 (예: 3443)
    data_value: 데이터 값
    """
    if data_value is None:
        return False
        
    str_target = str(target_input).strip()
    str_data = str(data_value).strip()

    # 쉼표 제거 (예: "1,234" -> "1234")
    str_data_clean = str_data.replace(',', '')

    try:
        # 소수점 버리고 정수로 변환하여 비교
        num_target = int(float(str_target))
        num_data = int(float(str_data_clean))

        if num_target == num_data:
            return True
    except ValueError:
        pass

    # 문자열 포함 여부 확인
    if str_target in str_data:
        return True
        
    return False

# ==========================================
# 2. 변수명(Key) 추적 함수 (find_key_path)
# ==========================================
# 찾은 경로를 저장할 전역 리스트
found_paths = []

def find_key_path(data, target_value, current_path=""):
    """
    재귀적으로 데이터를 탐색하여 Key를 찾습니다.
    """
    # 딕셔너리 탐색
    if isinstance(data, dict):
        for k, v in data.items():
            new_path = f"{current_path}['{k}']" if current_path else f"['{k}']"

            # 값 비교
            if is_match(target_value, v):
                print(f"🎉 찾음! 경로: data{new_path} | 값: {v}")
                found_paths.append(new_path)

            # 더 깊이 탐색
            if isinstance(v, (dict, list)):
                find_key_path(v, target_value, new_path)

    # 리스트 탐색
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{current_path}[{i}]"
            
            # 리스트 안의 값 자체 비교
            if is_match(target_value, item):
                 print(f"🎉 찾음! 경로: data{new_path} | 값: {item}")
                 found_paths.append(new_path)

            # 더 깊이 탐색
            find_key_path(item, target_value, new_path)

# ==========================================
# 3. 실행부 (이 부분을 주의하세요!)
# ==========================================
# data 변수가 있다고 가정하고 실행합니다.
# 만약 'data'가 정의되지 않았다는 오류가 나면 
# 위쪽 코드 어딘가에서 data = ... 로 데이터를 불러오는 부분이 있어야 합니다.

try:
    print("🕵️‍♂️ 탐색 시작 (찾는 값: 3443)...")
    
    # 이전에 찾은 목록 초기화
    found_paths = [] 
    
    # ★ 중요: data 변수가 코드 상단에 정의되어 있어야 합니다.
    # 만약 data 변수명이 다르다면 아래 'data'를 실제 변수명으로 바꿔주세요.
    if 'data' in locals() or 'data' in globals():
        find_key_path(data, 3443)
        
        if not found_paths:
            print("😭 결과 없음. (데이터에 해당 값이 없거나 data 변수가 비어있음)")
    else:
        print("⚠️ 주의: 'data' 변수가 정의되지 않았습니다. 데이터를 먼저 로드해주세요.")

except Exception as e:
    print(f"오류 발생: {e}")
