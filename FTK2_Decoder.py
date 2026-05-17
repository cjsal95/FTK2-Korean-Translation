# For The King II\For The King II_Data\StreamingAssets\Assets\Configs\JSON~\Langs
# 파일을...

import json
import os

# 디코딩할 원본 파일 이름과 결과 파일 이름 설정
input_file = "en.json"
output_file = "en_translated.json"

if not os.path.exists(input_file):
    print(f"❌ 에러: {input_file} 파일이 현재 폴더에 없습니다!")
    print("ko.json 파일을 이 스크립트와 같은 폴더에 두고 다시 실행하세요.")
else:
    try:
        # 1. 깨진 유니코드 상태의 JSON 파일을 그냥 일반 텍스트(utf-8)로 읽기
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # 2. 깨끗한 한글로 변환하여 새 파일로 저장 (ensure_ascii=False 가 핵심!)
        with open(output_file, "w", encoding="utf-8-sig") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("🎉 변환 성공! 한글 패치가 완료되었습니다.")
        print(f"📁 생성된 파일: {output_file}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
    except Exception as e:
        print(f"❌ 변환 도중 오류 발생: {e}")