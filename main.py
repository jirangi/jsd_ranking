import requests
import os
import json

RAW_API_KEY = os.environ.get('LOA_API_KEY', '')
API_KEY = RAW_API_KEY.replace("Bearer ", "").strip()

def main():
    if not API_KEY:
        print("❌ API 키가 없습니다!")
        return

    nickname = "핑뚝이환수사"
    target = "3443" # 찾을 숫자
    encoded_name = requests.utils.quote(nickname)
    headers = {'accept': 'application/json', 'authorization': f'bearer {API_KEY}'}

    print(f"🚀 '{nickname}'의 모든 정보를 샅샅이 뒤지는 중...")
    print(f"🎯 목표물: {target} (전투력)\n")

    # 검색할 보물지도 목록 (API 주소들)
    endpoints = {
        "1. 아크 패시브 (ArkPassive)": f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/arkpassive',
        "2. 각인 (Engravings)": f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/engravings',
        "3. 카드 (Cards)": f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/cards',
        "4. 보석 (Gems)": f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/gems',
        "5. 전투 스킬 (CombatSkills)": f'https://developer-lostark.game.onstove.com/armories/characters/{encoded_name}/combat-skills'
    }

    found_any = False

    for title, url in endpoints.items():
        print(f"🔎 [{title}] 검사 중...", end=" ")
        try:
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                data = res.json()
                # 데이터를 문자열로 바꿔서 검색
                str_data = json.dumps(data, ensure_ascii=False)
                
                if target in str_data:
                    print("✅ 발견!!! 🎉")
                    print(f"\n[✨ 정답은 '{title}' 안에 있었습니다!]")
                    print("▼ 아래 데이터에서 숫자를 찾아보세요 ▼")
                    # 보기 좋게 출력
                    print(json.dumps(data, indent=4, ensure_ascii=False))
                    found_any = True
                    break # 찾으면 즉시 종료
                else:
                    print("❌ 없음")
            else:
                print(f"⚠️ 오류 ({res.status_code})")
        except Exception as e:
            print(f"에러: {e}")
            
    if not found_any:
        print("\n😱 모든 곳을 뒤졌는데도 안 나옵니다... 숫자가 '3,443' 처럼 콤마가 있거나 조금 다를 수 있습니다.")

if __name__ == "__main__":
    main()
