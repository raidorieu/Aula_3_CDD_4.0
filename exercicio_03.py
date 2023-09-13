#que mês estamos
n=int(input("何月: "))
if n>12 or n<=0:
    print("無効なデータ")

if n==1:
    print("一月")
else:
    if n==2:
        print("二月")
    else:
        if n==3:
            print("三月")
        else:
            if n==4:
                print("四月")
            else:
                if n==5:
                    print("五月")
                else:
                    if n==6:
                        print("六月")
                    else:
                        if n==7:
                            print("七月")
                        else:
                            if n==8:
                                print("八月")
                            else:
                                if n==9:
                                    print("九月")
                                else:
                                    if n==10:
                                        print("十月")
                                    else:
                                        if n==11:
                                            print("十一月")
                                        else:
                                            if n==12:
                                                print("十二月")