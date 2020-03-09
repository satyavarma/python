#len([i for i in range(len(s)) if s[i:i+len(b)] == b])

def count_substring(string, sub_string):
    c, f = 0, 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i] == sub_string[0]):
            f = 0
            for j in range(len(sub_string)):
                if (string[i+j] != sub_string[j]):
                    f = 1
                    break
            if(f!=1):
                c+=1
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
