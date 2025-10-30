for i in range(100, 0, -1):
    num_str = str(i)
    clap_count = num_str.count('3')
    if clap_count > 0:
        print("짝" * clap_count)
    else:
        print(i)