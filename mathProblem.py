import random

def GCD(a,b):
    # 최대공약수 구하기
    while b != 0:
        a, b = b, a%b
    return a

def LCD(a,b):
    #최소공배수 구하기
    return a*b/GCD(a,b)

def changeB():
    # 분수를 나눗셈으로 혹은 나눗셈을 분수로 바꾸는 문제
    j = random.randrange(1,10)
    m = j
    while(m==j):
        m = random.randrange(1,10)
    cc = random.randrange(2)
    if cc == 0:
        c = random.randrange(2)
        print("{0} ÷ {1}\n".format(j,m))
        if c==0:
            print("(1)  {0}   (2)   {1}".format(m,j))
            print("    ---       --- ")
            print("     {0}         {1}".format(j,m))
        else:
            print("(1)  {0}   (2)   {1}".format(j,m))
            print("    ---       --- ")
            print("     {0}         {1}".format(m,j))
        a = int(input("올바른 답은 (1)과 (2)중 어디인가요?"))
        if(a==1 and c!=0) or (a==2 and c==0):
            print("\n정답!!!!!!!\n")
            return 1
        else:
            print("\n오답@@@@@@@\n")
            return -1
    else:
        c = random.randrange(2)
        print("     {0}".format(j))
        print("    --- ")
        print("     {0}".format(m))
        if c==0:
            print("(1) {0} ÷ {1}\n(2) {1} ÷ {0}".format(j,m))
        else:
            print("(1) {0} ÷ {1}\n(2) {1} ÷ {0}".format(m,j))
        a = int(input("올바른 답은 (1)과 (2)중 어디인가요?"))
        if(a==1 and c==0) or (a==2 and c!=0):
            print("\n정답!!!!!!!\n")
            return 1
        else:
            print("\n오답@@@@@@@\n")
            return -1

def plus():
    # 분수와 분수의 덧셈과 뺄셈
    print("다음 식을 계산하시오.")
    j = random.randrange(1,10)
    m = random.randrange(2,10)
    j1 = j
    while(j1==j):
        j1 = random.randrange(1,10)
    m1 = m
    while(m1 == m):
        m1 = random.randrange(2,10)
    c = random.randrange(2)
    if c != 0:
        if j/m<j1/m1:
            j,j1 = j1,j
            m,m1 = m1,m
    print("{0:2d}   {1:2d}".format(j,j1))
    if c == 0:
        print("-- + -- =")
    else:
        print("-- - -- =")
    print("{0:2d}   {1:2d}".format(m,m1))
    answerM = int(input("분모를 입력하시오:"))
    answerJ = int(input("분자를 입력하시오:"))
    print()
    # 부동소수점 때문에 계산이 안 될 수도 있어서 분모, 분자를 따로 입력받습니다.
    am = LCD(m,m1)
    if c != 0:
        aj1 = (am/m)*j - (am/m1)*j1
    else:
        aj1 = (am/m)*j + (am/m1)*j1
    mymistake = GCD(am,aj1)
    am = am/mymistake
    aj1 = aj1/mymistake

    
    if answerM == am and answerJ == aj1:
        print()
        print("정답")
        print()
        return 1
    else:
        print("틀렸어 답은")
        print()
        print("{0}".format(int(aj1)))
        print("---")
        print("{0}".format(int(am)))
        print()
        return -1

def multiple():
    # 자연수와 분수의 곱셈과 나눗셈
    swi = random.randrange(2)
    if swi == 0:
        j = random.randrange(1,20)
        m = random.randrange(1,20)
        x = m * random.randrange(1,20)
        print("      {0:2d}".format(j))
        print("{0:3d} X -- =".format(x))
        print("      {0:2d}".format(m))
        answer = int(input("답: "))
        if answer == x*j/m:
            print("정답")
            return 1
        else:
            print("틀렸어 답은 {0}".format(x*j/m))
            print()
            return -1
    else:
        j = random.randrange(1,20)
        m = random.randrange(1,20)
        x = m * random.randrange(1,20)
        print("      {0:2d}".format(m))
        print("{0:3d} ÷ -- =".format(x))
        print("      {0:2d}".format(j))
        answer = int(input("답: "))
        if answer == x*j/m:
            print("정답")
            return 1
        else:
            print("틀렸어 답은 {0}".format(x*j/m))
            print()
            return -1


def multipleB():
    # 분수끼리의 곱셈과 나눗셈
    swi = random.randrange(2)
    j = random.randrange(1,16)
    j1 = random.randrange(1,16)
    m = random.randrange(1,16)
    m1 = random.randrange(1,16)
    if swi == 0:
        print("{0:2d}   {1:2d}".format(j,j1))
        print("-- X -- =")
        print("{0:2d}   {1:2d}".format(m,m1))
        answerM = int(input("분모를 입력하시오:"))
        answerJ = int(input("분자를 입력하시오:"))
        am = m * m1
        aj = j * j1
        ar = GCD(am,aj)
        am = am/ar
        aj = aj/ar
        if answerM == am and answerJ == aj:
            print("정답")
            return 1
        else:
            print("틀렸어 답은")
            print()
            print("{0}".format(int(aj)))
            print("---")
            print("{0}".format(int(am)))
            print()
            return -1
    else:
        print("{0:2d}   {1:2d}".format(j,j1))
        print("-- ÷ -- =")
        print("{0:2d}   {1:2d}".format(m,m1))
        answerM = int(input("분모를 입력하시오:"))
        answerJ = int(input("분자를 입력하시오:"))
        am = m * j1
        aj = j * m1
        ar = GCD(am,aj)
        am = am/ar
        aj = aj/ar
        if answerM == am and answerJ == aj:
            print("정답")
            return 1
        else:
            print("틀렸어 답은")
            print()
            print("{0}".format(int(aj)))
            print("---")
            print("{0}".format(int(am)))
            print()
            return -1

score = 0
while(True):
    print("------------------------------------------------------------------------")
    c = random.randrange(4)
    if c==0:
        score += multiple()
    elif c==1:
        score += multipleB()
    elif c==2:
        score += plus()
    else:
        score += changeB()
    print("현재 점수{0}\n".format(score))
    if score>=50:
        print("수고했다!!!!!!!")
        break
