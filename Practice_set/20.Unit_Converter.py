def dec_bin(num):
    ans1 = ""
    ans2 = ""
    whole_num = int(num)
    frac_num = num % 1
    if whole_num == 0:
        ans1 = "0"
    else:
        while whole_num>0:
            digit = whole_num%2
            ans1+= str(digit)
            whole_num//=2
        ans1 = ans1[::-1]
        for i in range(0, 4):
            dummy = frac_num*2
            ans2 += str(int(dummy))
            frac_num = dummy - int(dummy)
        return ans1 + "." + ans2

def dec_oct(num):
    ans1 = ""
    ans2 = ""
    whole_num = int(num)
    frac_num = num % 1
    if whole_num == 0:
        ans1 = "0"
    else:
        while whole_num>0:
            digit = whole_num%8
            ans1+= str(digit)
            whole_num//=8
        ans1 = ans1[::-1]
    for i in range(0, 4):
        dummy = frac_num*8
        ans2 += str(int(dummy))
        frac_num = dummy - int(dummy)
    return ans1 + "." + ans2

def dec_hex(num):
    ans1 = ""
    ans2 = ""
    whole_num = int(num)
    special_num = [10, 11, 12, 13, 14, 15]
    special_char = ['A', 'B', 'C', 'D', 'E', 'F']
    frac_num = num % 1
    if whole_num == 0:
        ans1 = "0"
    else:
        while whole_num>0:
            flag = 0
            digit = whole_num%16
            for i in range(0, 6):
                if digit == special_num[i]:
                    ans1+=special_char[i]
                    flag = 1
                    break
            if flag == 0:
                ans1+= str(digit)
            whole_num//=16
        ans1 = ans1[::-1]
    for i in range(0, 4):
        dummy = frac_num*16
        flag = 0
        for i in range(0, 6):
            if int(dummy) == special_num[i]:
                ans2+=special_char[i]
                flag = 1
                break
        if flag == 0:
            ans2 += str(int(dummy))
        frac_num = dummy - int(dummy)
    return ans1 + "." + ans2

print(dec_bin(18.625))
print(dec_hex(18.625))
print(dec_oct(18.625))