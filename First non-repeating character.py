def first_non_repeating_letter(string):
    #your code here
    lst=[]
    for x in string:
        if x in 'abcdefghijlmnoprstuvwxyzqABCDEFGHIJKLMONPRSUVWXYZQ':   
            if (string.lower()).count(x.lower())==1:
                return x
        elif string.count(x)==1:
            return x
        
        lst.append(x)
    if 1 not in lst:
        return ""
        