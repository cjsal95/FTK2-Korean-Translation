import json
import os

# 원본(내가 수정한 한글 파일)과 결과물(게임에 넣을 파일) 이름 설정
input_file = "ko_translated.json"
output_file = "ko.json"

if not os.path.exists(input_file):
    print(f"❌ 에러: '{input_file}' 파일이 현재 폴더에 없습니다!")
else:
    try:
        # 1. 사람이 읽을 수 있게 수정된 한글 JSON 파일 읽기
        with open(input_file, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        
        # 2. 게임 원본 포맷인 유니코드 이스케이프(\\uXXXX) 형태로 변환하여 저장
        # (ensure_ascii=True 옵션이 한글을 유니코드 코드로 강제 변환합니다)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=True, indent=2)
            
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("🎉 인코딩 성공! 게임 원본 포맷으로 변환되었습니다.")
        print(f"📁 생성된 파일: {output_file}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
    except Exception as e:
        print(f"❌ 변환 도중 오류 발생: {e}")