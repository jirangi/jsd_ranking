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
# 3. 실행부 (수정된 버전)
# ==========================================
import requests

# 👇 [입력 1] 본인 캐릭터 닉네임을 여기에 적으세요
character_name = "핑뚝이환수사" 

# 👇 [입력 2] 발급받은 API 키(JWT)를 따옴표 안에 붙여넣으세요 (ey...로 시작하는 아주 긴 문자열)
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDA1NzMzOTQifQ.nXLXdQmDX5DenGtdMVaJZ11_GqDvE1FuxR0tcRAFESAvsYJvGMjbMfzRwT7uXIHDczAu-xK54XQLE8A0fJAgzFX6NAq49oC_E6UL9v_IUlizSGheoYYSb8-wOMYtRcXSCM1ZgBQD40i6hm5IXDVBXtOnAne0vWjclkd3LGS37MubwtcQKVFfXojAsk-O1268-yDfrLK02ZXHnrVMZneojZSB3u63Cjdr1Xr5BUi0UIVLWXni1H45tJ2FVQQTTdgB_b5OG1HQINvwy0vC5cg7IXJU0AE59EF3W9cotHXspT-HcLJGKL68MUjqNj2yDoGy1fgDhk2ZmRCjUSmU7QbplA"


# ---------------------------------------------------------
# (여기서부터는 건드리지 않아도 됩니다)
# ---------------------------------------------------------

# 1. URL 설정 (캐릭터의 모든 장비/스탯 정보를 가져오는 주소)
# 한글 닉네임이 들어가므로 f-string을 사용합니다.
url = f"https://developer-lostark.game.onstove.com/armories/characters/{character_name}"

# 2. 헤더 설정 (인증 정보)
headers = {
    'accept': 'application/json',
    'authorization': f'bearer {api_key}'  # 'bearer ' 뒤에 키가 붙는 형식입니다.
}

print(f"🚀 '{character_name}'의 정보를 서버에서 가져오는 중...")

try:
    # API 호출
    response = requests.get(url, headers=headers)

    # 응답 코드가 200(성공)이 아니면 에러 메시지 출력
    if response.status_code != 200:
        print(f"❌ API 호출 실패! (상태 코드: {response.status_code})")
        print("이유:", response.text)
        data = None
    else:
        data = response.json() # 데이터를 data 변수에 저장
        print("✅ 데이터 로드 성공! 이제 분석을 시작합니다.")

    # ---------------------------------------------------------
    # 데이터 탐색 시작 (data 변수가 준비됨)
    # ---------------------------------------------------------
    print("\n" + "="*40)
    print("🕵️‍♂️ 탐색 시작 (찾는 값: 3443)...")
    print("="*40)
    
    found_paths = [] 
    
    # data 변수가 정상적으로 만들어졌는지 확인 후 실행
    if 'data' in locals() and data is not None:
        find_key_path(data, 3443)
        
        if not found_paths:
            print("😭 결과 없음. (혹시 전투력이 바뀌었거나, 다른 숫자인가요?)")
    else:
        print("⚠️ 데이터가 비어있어서 탐색을 할 수 없습니다.")

except Exception as e:
    print(f"오류 발생: {e}")
