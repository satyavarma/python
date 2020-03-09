def merge_the_tools(mstr, fact):
    for i in range(0, len(mstr), fact):
        substr = mstr[i:i+fact]
        for p in range (fact):
            if (substr[p] not in substr[:p]) or (p == 0):
                print(substr[p],end='');
        print('')
              
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
'''the string is a string and k is the factor for the length of the string
then we have to divide the string of size k and print without duplicate values from last'''
