#str.swapcase() predefined method to do the same thing as def here

def swap_case(s):
    ress = ""
    for i in s:
        if(i.islower()):
            ress+=i.upper()
        else:
            ress+=i.lower()
    return ress

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
