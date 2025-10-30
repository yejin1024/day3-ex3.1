for i in range(100, 0, -1):  # 100에서 1까지 역순 출력
    num_str = str(i)
    # 숫자 안에 포함된 3, 6, 9의 개수를 모두 합산
    clap_count = sum(num_str.count(d) for d in ['3', '6', '9'])

    if clap_count > 0:
        print("짝" * clap_count)
    else:
        print(i)