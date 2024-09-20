import os

# 이미지 파일들이 저장된 폴더 경로
folder_path = r"C:\Users\user.SKTP124162PN005\Desktop\'24년 Safety Golden Rules(안전 수칙) SKO 向 SGR 세부규칙_9.1 개정"

# 폴더 내 파일명을 반복하며 변경
for filename in os.listdir(folder_path):
    if filename.startswith("슬라이드") and filename.endswith(".JPG"):
        # 번호 추출
        number_part = filename.replace("슬라이드", "").replace(".JPG", "")
        new_filename = f"{number_part}.jpg"
        # 파일명 변경
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("파일명이 성공적으로 변경되었습니다!")