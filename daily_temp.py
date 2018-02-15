def dailyTemperature(temperatures):
    temp_list = [-1] * 71
    answer_list = [0] * len(temperatures)
    for i in range(len(temperatures)-1,-1,-1):
        num = [j for j in temp_list[temperatures[i]-29:] if j > -1]
        if len(num) != 0:
            answer_list[i] = min(num)-i
        temp_list[temperatures[i]-30] = i
    return answer_list

def test():
    answers = dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])
    print(answers)

if __name__ == "__main__":
    test()