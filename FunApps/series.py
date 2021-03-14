while True:
    series = list(
        map(int, input("Enter series of numbers seperate with spaces:\n").split()))
    if len(series) >= 3 and sum(series[-3:]) == 10:
        series = series[:-2]
    if len(series) >= 4 and sum(series[-4:]) == 20:
        series = []
    if sum(series) == 44:
        print("You Won!!")
        break
    elif print('Koose')
