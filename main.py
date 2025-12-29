import requests
import os
import json

# API 키 가져오기
RAW_API_KEY = os.environ.get('LOA_API_KEY', '')
API_KEY = RAW_API_KEY.replace("Bearer ", "").replace("bearer ", "").strip()

def main():
    print("\n" + "="*50)
    print("🚀 [분석 시작] 데이터 출력을 시작합니다!")
    print("="*50 + "\n")

    if not API_KEY:
        print("❌ [오류] API 키가 없습니다! Settings > Secrets를 확인하세요.")
        return

    nickname = "핑뚝이환수사"
    target = "3443" # 찾을 숫자

    headers = {'accept': 'application/json', 'authorization': f'bearer {API_KEY}'}
    
    # 1. 프로필 데이터 출력
    print(f"\n📂 [1] 프로필 데이터 (Profiles) 검색 중...")
    url_prof = f'https://developer-lostark.game.onstove.com/armories/characters/{requests.utils.quote(nickname)}/profiles'
    res_prof = requests.get(url_prof, headers=headers)
    
    if res_prof.status_code == 200:
        data = res_prof.json()
        print("✅ 데이터를 성공적으로 가져왔습니다. 내용을 확인하세요:\n")
        # 데이터 전체 출력 (이걸 로그에서 볼 거예요)
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f"❌ 데이터 가져오기 실패: {res_prof.status_code}")

    # 2. 장비 데이터 출력
    print(f"\n\n⚔️ [2] 장비 데이터 (Equipment) 검색 중...")
    url_equip = f'https://developer-lostark.game.onstove.com/armories/characters/{requests.utils.quote(nickname)}/equipment'
    res_equip = requests.get(url_equip, headers=headers)
    
    if res_equip.status_code == 200:
        data = res_equip.json()
        print("✅ 데이터를 성공적으로 가져왔습니다. 내용을 확인하세요:\n")
        # 데이터 전체 출력
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f"❌ 데이터 가져오기 실패: {res_equip.status_code}")

    print("\n" + "="*50)
    print("🏁 [분석 종료] 위 로그에서 '3443'을 찾아보세요!")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
