import string

def detect_digits(input_string):

    #list of digits from 0-9
    digit_list = list(string.digits)

    flag = False
    #checking every string characters if it is present in digits list or not
    for i in input_string:
        if i in digit_list:
            flag = True
            break
    
    #printing out the result
    if flag == True :
        print("String contains digits")
    else:
        print("String does not contains digit")

            
