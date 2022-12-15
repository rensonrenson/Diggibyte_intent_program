def merge_the_tools(string, k):
    # your code goes here
    l = []
    while len(string) > 0:
        sub = string[0:k]
        l.append(sub)
        string = string[k:]

    for s in l:
        sub_str = ""
        for char in s:
            if char not in sub_str:
                sub_str += char
        print(sub_str)
        if __name__ == '__main__':
            string, k = input(), int(input())
            merge_the_tools(string, k)