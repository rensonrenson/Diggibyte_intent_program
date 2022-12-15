
def print_formatted(number):
    num = 17


for i in range(1, 18):
    c = format(i, "b")
    d = format(i, "o")
    e = format(i, "x")
    print(int(c, 2), int(d), e, c)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)