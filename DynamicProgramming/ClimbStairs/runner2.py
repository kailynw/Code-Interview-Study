def climb_stairs(num: int):
    if num == 0: return 0
    if num == 1: return 1
    if num == 2: return 2
    one_step = 1
    two_step = 2
    [0, 1, 2, 3, 5, 8]
    for _ in range(num - 2):
        temp = one_step + two_step
        one_step = two_step
        two_step = temp
    return two_step



if __name__ == "__main__":
    print(climb_stairs(6))