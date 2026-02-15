def happy_num(start, end):
    num_list = []
    for num in range(start,end+1): 
        history = []
        orignal = num
        while num != 1 and num not in history:
            history.append(num)

            dummy = num
            sum = 0
            while dummy>0:
                digit = dummy%10
                sum+= digit**2
                dummy //= 10
            
            num = sum
        if num == 1:
            num_list.append(orignal)
    return num_list

print(happy_num(0,100))