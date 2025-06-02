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
    要求：输入一个大于 1 的正整数，判断它是不是素数。
    提示：素数指的是只能被 1 和自身整除的大于 1 的整数。
    '''
    
    prime = int(input("请打出一个正整数"))
    divisor = 2

    if prime <= 2:
        if prime == 1:
            print("您输入的是1, 素数从2才能开始")
            return
        else:
            print(f"数字{prime}是一个偶素数")
            return
    
    while divisor <= prime:
        if prime % divisor == 0:
            if prime == divisor:
                print(f"数字{prime}是一个素数")
                return
            else:
                print(f"数字{prime}不是素数, 它可以被{divisor}整除")
                return
        else:
            print(f"正在尝试{prime}除以{divisor}")
        divisor += 1

if __name__ == "__main__":
    '''
    table_of_ninenine()
    prime_numbers()
    '''
    table_of_ninenine()