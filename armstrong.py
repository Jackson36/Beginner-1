def main():
    n=int(input())
    on=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+(digit**3)
        n//=10
    if on==sum:
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
