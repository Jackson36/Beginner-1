def main():
    
    a=input()
    b=input()

    for n in range(a,b+1):
        sum = 0
        temp = n
        while temp > 0:
            digit=temp%10
            sum=sum+(digit**3)
            temp//=10

        if n == sum:
            print(n)

if __name__ == '__main__':
    main()
