import requests
import os
import json

# API 키 설정
RAW_API_KEY = os.environ.get('LOA_API_KEY', '')
API_KEY = RAW_API_KEY.replace("Bearer ", "").strip()

def find_real_combat_power():
    if not API_KEY:
        print("🚫 API 키가 없습니다.")
        return

    nickname = "핑뚝이환수사"
    target_value = "3443" # 우리가 찾는 보물 (핑뚝이의 전투력 앞자리)

    print(f"🕵️‍♂️ '{nickname}'의 데이터에서 '{target_value}'를 찾는 중입니다...\n")
    
    headers = {'accept': 'application/json', 'authorization': f'bearer {API_KEY}'}
    encoded_name = requests.utils.quote(nickname)
    
    # 1. 프로필(Profiles) 뒤지기
    url_profile = f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/profiles'
    res_prof = requests.get(url_profile, headers=headers)
    
    if res_prof.status_code == 200:
        data_prof = res_prof.json()
        print("--- [1] 프로필(Profile) 검사 ---")
        # 데이터를 문자열로 바꿔서 검색
        str_prof = json.dumps(data_prof, ensure_ascii=False)
        if target_value in str_prof:
            print(f"✅ 발견! 프로필 데이터 어딘가에 '{target_value}'가 있습니다!")
            # 상세 위치 찾기 (Stats 안에 있는지 확인)
            if 'Stats' in data_prof:
                for stat in data_prof['Stats']:
                    if target_value in str(stat['Value']):
                        print(f"   👉 찾았다! [Stats] 목록의 이름: '{stat['Type']}' / 값: {stat['Value']}")
        else:
            print("❌ 프로필에는 없습니다. (여기 있는 '공격력'은 가짜입니다)")

    # 2. 장비(Equipment) 뒤지기 (여기에 있을 확률이 높음)
    url_equip = f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/equipment'
    res_equip = requests.get(url_equip, headers=headers)

    if res_equip.status_code == 200:
        data_equip = res_equip.json()
        print("\n--- [2] 장비(Equipment) 검사 ---")
        str_equip = json.dumps(data_equip, ensure_ascii=False)
        
        if target_value in str_equip:
            print(f"✅ 대박! 장비 데이터 안에서 '{target_value}'를 찾았습니다!")
            print("   (아마 무기 툴팁 안에 숨어있는 '기본 효과'이거나 '무기 공격력'일 수 있습니다.)")
            
            # 무기만 따로 떼서 툴팁 내용을 보여줌
            for item in data_equip:
                if item['Type'] == "무기":
                    print(f"\n   🗡️ [무기 정보]: {item['Name']}")
                    # 툴팁 안에 숫자가 있는지 확인
                    if target_value in item['Tooltip']:
                        print(f"   👉 무기 툴팁(Tooltip) 안에 '{target_value}'가 포함되어 있습니다.")
        else:
            print("❌ 장비 데이터에도 없습니다.")

if __name__ == "__main__":
    find_real_combat_power()
