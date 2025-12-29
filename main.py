import requests
import os
import json
import sys

# 1. 안전장치: API 키 가져오기
RAW_API_KEY = os.environ.get('LOA_API_KEY', '')
API_KEY = RAW_API_KEY.replace("Bearer ", "").replace("bearer ", "").strip()

def main():
    print("🚀 데이터 분석 시작...")
    
    # 결과 내용을 담을 변수
    result_html = ""
    
    try:
        if not API_KEY:
            result_html = "<h1>🚫 API 키가 없습니다. Settings > Secrets를 확인하세요.</h1>"
            print("❌ API 키 없음")
        else:
            nickname = "핑뚝이환수사"
            print(f"🔍 '{nickname}' 정보 조회 중...")
            
            headers = {'accept': 'application/json', 'authorization': f'bearer {API_KEY}'}
            
            # (1) 프로필 데이터
            url_prof = f'https://developer-lostark.game.onstove.com/armories/characters/{requests.utils.quote(nickname)}/profiles'
            res_prof = requests.get(url_prof, headers=headers)
            str_prof = json.dumps(res_prof.json(), indent=4, ensure_ascii=False) if res_prof.status_code == 200 else f"Error: {res_prof.status_code}"

            # (2) 장비 데이터
            url_equip = f'https://developer-lostark.game.onstove.com/armories/characters/{requests.utils.quote(nickname)}/equipment'
            res_equip = requests.get(url_equip, headers=headers)
            str_equip = json.dumps(res_equip.json(), indent=4, ensure_ascii=False) if res_equip.status_code == 200 else f"Error: {res_equip.status_code}"

            # 찾을 숫자 (전투력 앞자리)
            target = "3443"
            msg = "❌ 못 찾았습니다."
            if target in str_prof: msg = f"✅ 프로필 데이터에서 '{target}' 발견!"
            elif target in str_equip: msg = f"✅ 장비 데이터에서 '{target}' 발견!"
            
            print(msg)

            # HTML 내용 채우기
            result_html = f"""
            <!DOCTYPE html>
            <html lang="ko">
            <head><meta charset="UTF-8"><title>데이터 분석</title></head>
            <body style="background:#121214; color:#fff; padding:20px; font-family:monospace; white-space:pre-wrap;">
            <h1 style="color:#ffca5c">{msg}</h1>
            <h2>1. 프로필 데이터</h2>
            <div style="background:#222; padding:10px; border:1px solid #555;">{str_prof.replace(target, f'<b style="background:red; color:white">{target}</b>')}</div>
            <h2>2. 장비 데이터</h2>
            <div style="background:#222; padding:10px; border:1px solid #555;">{str_equip.replace(target, f'<b style="background:red; color:white">{target}</b>')}</div>
            </body>
            </html>
            """
            
    except Exception as e:
        print(f"💥 에러 발생: {e}")
        result_html = f"<h1>💥 에러가 발생했습니다: {e}</h1>"

    # [중요] 무조건 파일 저장 (들여쓰기 주의!)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(result_html)
    print("💾 index.html 파일 저장 완료!")

if __name__ == "__main__":
    main()
