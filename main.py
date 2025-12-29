import math

# 찾은 결과를 저장할 리스트 (이걸로 'found' 여부를 판단합니다)
found_paths = []

# ==========================================
# 1. 비교 로직 함수 (사용자가 만든 것 활용)
# ==========================================
def is_match(target_input, data_value):
    """
    target_input: 찾는 값 (예: 3443)
    data_value: 데이터 값 (예: 3443.85, "3443", 3443)
    """
    if data_value is None:
        return False
        
    str_target = str(target_input).strip()
    str_data = str(data_value).strip()

    # 쉼표 제거 (예: "1,234" -> "1234")
    str_data_clean = str_data.replace(',', '')

    try:
        # 소수점 버리고 정수로 변환하여 비교 (3443.99 -> 3443 == 3443)
        num_target = int(float(str_target))
        num_data = int(float(str_data_clean))

        if num_target == num_data:
            return True
    except ValueError:
        pass

    # 문자열 포함 여부 (보조)
    if str_target in str_data:
        return True
        
    return False

# ==========================================
# 2. 변수명(Key) 추적 함수 (재귀)
# ==========================================
def find_key_path(data, target_value, current_path=""):
    # 딕셔너리 탐색
    if isinstance(data, dict):
        for k, v in data.items():
            # 경로 기록
            new_path = f"{current_path}['{k}']" if current_path else f"['{k}']"

            # ★ 핵심 수정: 여기서 is_match 함수를 호출합니다!
            if is_match(target_value, v):
                print(f"\n" + "="*40)
                print(f"🎉 찾았습니다! Key: '{k}'")
                print(f"📌 전체 경로: data{new_path}")
                print(f"💰 실제 값: {v}")
                print("="*40 + "\n")
                found_paths.append(new_path) # 찾았다고 기록

            # 더 깊이 탐색 (재귀)
            if isinstance(v, (dict, list)):
                find_key_path(v, target_value, new_path)

    # 리스트 탐색
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{current_path}[{i}]"
            
            # 리스트 안의 값 자체가 목표값일 경우 체크
            if is_match(target_value, item):
                 print(f"\n" + "="*40)
                 print(f"🎉 찾았습니다! Index: [{i}]")
                 print(f"📌 전체 경로: data{new_path}")
                 print(f"💰 실제 값: {item}")
                 print("="*40 + "\n")
                 found_paths.append(new_path)

            find_key_path(item, target_value, new_path)

# ==========================================
# 실행부
# ==========================================

# (중요) data 변수가 이미 정의되어 있어야 합니다.
# 예: data = response.json() 

print("🕵️‍♂️ 탐색을 시작합니다...")

# 찾은 목록 초기화
found_paths = [] 

# 함수 실행 (찾는 값: 3443)
find_key_path(data, 3443) 

# 결과 확인
if len(found_paths) == 0:
    print("\n😭 모든 곳을 뒤졌는데도 안 나옵니다... (데이터가 로드되었는지 확인해주세요)")
else:
    print(f"\n✅ 총 {len(found_paths)}개의 위치를 발견했습니다.")
