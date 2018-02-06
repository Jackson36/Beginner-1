def main():
    
    a=input()
    b=input()

    for num in range(a,b+1):
        sum = 0
        temp = num
        while temp > 0:
            digit=temp%10
            sum=sum+(digit**3)
            temp//=10

        if num == sum:
            print(num)

if __name__ == '__main__':
    main()
