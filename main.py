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
# 👇 [이 부분이 빠져 있습니다!] 👇
# 원래 작성하셨던 데이터를 가져오는 코드를 여기에 적어야 합니다.
# 예: url = "..." 하고 requests.get 하는 부분입니다.
import requests  # 만약 위에서 안 했다면
url = "https://developer-lostark.game.onstove.com/..." # (사용자분의 원래 URL)
headers = { ... } # (사용자분의 원래 인증키)

response = requests.get(url, headers=headers) # API 호출
data = response.json()  # 👈 데이터를 'data'라는 변수에 담습니다. (중요!)


# 👇 [여기서부터는 제가 드린 코드 그대로] 👇
try:
    print("🕵️‍♂️ 탐색 시작 (찾는 값: 3443)...")
    
    found_paths = [] 
    
    # 이제 'data' 변수가 있으니 정상 작동할 겁니다!
    if 'data' in locals() or 'data' in globals():
        find_key_path(data, 3443)
        
        if not found_paths:
            print("😭 결과 없음.")
    else:
        print("⚠️ 주의: 'data' 변수가 정의되지 않았습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
