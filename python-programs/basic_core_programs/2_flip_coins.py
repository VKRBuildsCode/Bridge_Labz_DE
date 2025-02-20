import random as rm

def  flip_coins():
    heads=0
    tails=0
    try:
        no_flips=int(input("Enter the number of times to flip coin 🪙 : "))
        if no_flips<1:
            print("Positive number is accepted, please try again......")
            flip_coins()
        else:
            for i in range(no_flips):
                if rm.random()<0.5:
                    tails+=1
                else:
                    heads+=1
            head_percentage=(heads/no_flips)*100
            tail_percentage=100-head_percentage
            print(f"Percentage of times, tail have appeared is : {tail_percentage:.2f}%")
            print(f"Percentage of times, head have appeared is : {head_percentage:.2f}%")
    except ValueError as e:
        print(e)
        print("Try again .....")
        flip_coins()
    pass
flip_coins()