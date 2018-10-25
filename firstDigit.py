def firstDigit(inputString):

    ### iterate through each character in string
    for char in inputString:
    
        ### determine if char is a digit using str.isdigit()
        ### if True, return char
        if str.isdigit(char):
            return char
        ### otherwise continue
        else:
            continue
