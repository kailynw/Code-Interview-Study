def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        one, two = two, one+two
    return two

def climbStairsPt2(n: int) -> int:
    pass

if __name__ == "__main__":
    value = climbStairs(5)
    print(value)




    [None, None, 3, 2, 1, 1]

    # one, two = 1,1
    # temp = 2
    # one = 1 #two
    # two =  2

    # one, two = 1, 2
    # temp = 3
    # one  = 2
    # two = 3

    one, two = 2, 3


    one, two = two, one+two
