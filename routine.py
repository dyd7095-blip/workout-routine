day = input("오늘의 요일을 입력하세요 (예: 월, 화): ")

if day in ['월', '목']:
    print("오늘의 루틴: 가슴 / 삼두")
elif day in ['화', '금']:
    print("오늘의 루틴: 등 / 이두")
elif day in ['수']:
    print("오늘의 루틴: 하체")
elif day in ['토']:
    print("오늘의 루틴: 어깨")
else:
    print("오늘은 휴식입니다!")