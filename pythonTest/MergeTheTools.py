def merge_the_tools(string, k):
    # your code goes herea
    
    for i in range(0,len(string),k):
        seen = set()
        chunk = string[i:i+k]
        unique = []
        for x in chunk:
            if x not in seen:
                seen.add(x)
                unique.append(x)
        
        print(''.join(unique))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)