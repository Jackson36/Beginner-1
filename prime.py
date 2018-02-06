def main():
    x=int(input())
    flag=1
    for i in  range(2,x//2):
        if x%i==0:
            flag=0
    if flag==1:
        print("yes")
    else:
        print("no")
if __name__=='__main__':
    main()
