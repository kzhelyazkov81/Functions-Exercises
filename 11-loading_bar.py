def loading_bar(percents):
    if percents == 100:
        print('100% Complete!')
        print(f"[{'%' * 10}]")
    else:
        done = '%' * int(percents//10)
        left = '.' * int((100 - percents) // 10)
        print(f'{percents}% [{done}{left}]')
        print('Still loading...')


loading_bar(int(input()))
