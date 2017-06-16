def multiply(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    length1 = len(num1)
    length2 = len(num2)
    temp = [0 for __ in range(length1 + length2)]
    
    for i in range(length1):
        for j in range(length2):
            temp[i+j] += int(num1[i]) * int(num2[j])
    
    carry =0
    digits = []
    
    for num in temp:
        s = carry + num
        carry = s//10
        digits.append(str(s%10))
    result = "".join(digits)[::-1]
    
    subindex = 0
    for i in range(length1+length2-1):
        if result[i] =="0":
            subindex +=1
        else:
            break
    
    result = result[subindex:]
    return result
