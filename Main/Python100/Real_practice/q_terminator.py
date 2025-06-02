import random

def table_of_ninenine():
    '''
    请输出九九乘法表, 格式如下
    1x1=1 
    2x1=2 2x2=4 
    3x1=3 3x2=6 3x3=9
    4x1=4 4x2=8 4x3=12 4x4=16
    5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
    6x1=6 6x2=12 6x3=18 6x4=24 6x5=30 6x6=36
    7x1=7 7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49
    8x1=8 8x2=16 8x3=24 8x4=32 8x5=40 8x6=48 8x7=56 8x8=64
    9x1=9 9x2=18 9x3=27 9x4=36 9x5=45 9x6=54 9x7=63 9x8=72 9x9=81

    知识点: 
    for循环
    range(start, end, step)
    print()函数的 end 参数用于指定每次打印结束时追加的字符串。默认情况下, end='\n', 即每次打印后会自动换行
    '''
    for a in range(1, 10, 1):
        for b in range(1, a + 1, 1):
            print(f"{a}x{b}={a*b}", end = " ")
        print()

def prime_numbers():
    '''
    要求: 输入一个大于 1 的正整数, 判断它是不是素数。
    提示: 素数指的是只能被 1 和自身整除的大于 1 的整数。
    '''
    
    prime = int(input("please input a positive integer"))
    divisor = 2

    if prime <= 2:
        if prime == 1:
            print("you input 1, but prime start from 2")
            return
        else:
            print(f"{prime}is a even prime number")
            return
    
    while divisor <= prime:
        if prime % divisor == 0:
            if prime == divisor:
                print(f"{prime} is a prime!")
                return
            else:
                print(f"{prime} is not a prime, it can be divided by {divisor}")
                return
        else:
            print(f"trying...{prime}/{divisor}")
        divisor += 1

def auto_guess_machine():
    '''
    猜数字
    要求: 人类选择一个区间, 计算机随机选择一个数字，并模拟人类玩猜数字游戏。
    计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”, 
    如果猜中了数字, 计算机统计一共猜了多少次, 游戏结束, 否则游戏继续。

    知识点: 
    二分查找的正确性依赖于两个条件: 
    有序性: 数组必须是升序或降序排列的。
    区间收缩: 每次迭代后, 搜索范围必须严格缩小, 且目标值始终存在于新的搜索范围内。
    '''
    while True:
        try:
            low = int(input("low: "))
            high = int(input("high: "))
            if low > high:
                low, high = high, low
        except Exception as e:
            print("you may need to input again...")
        choice = random.randint(low, high)
        input(f"machine auto choosed a number between {low} and {high}!should player start guessing? please enter...")

        count = 1
        while True:
            player = (low+high)//2
            if player < choice:
                print(f"you guess {player}, too small, please guess again!")
                low = player + 1
            elif player > choice:
                print(f"you guess {player}, too big, please guess again!")
                high = player - 1
            else:
                print(f"right! the number is {choice}, you guess {count} times\n")
                return
            count += 1

if __name__ == "__main__":
    '''
    table_of_ninenine()
    prime_numbers()
    auto_guess_machine()
    '''
    auto_guess_machine()