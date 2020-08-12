x = input('Input Lamrop Code: \n')

def lamrop(inp):
    arr = []
    zpl = 0
    s = 1
    i = 0
    arrout = ''
    while i < len(inp):
        if inp[i] == 'l':
            if zpl > 0:
                zpl -= 1
        elif inp[i] == 'a':
            arr[zpl] += s
        elif inp[i] == 'm':
            arr[zpl] -= s
        elif inp[i] == 'r':
            zpl += 1
        elif inp[i] == 'o':
            print(arrout)
        elif inp[i] == 'p':
            arr.append(0)
        elif inp[i] == 's':
            s = arr[zpl]
        elif inp[i] == '+':
            if inp[i+1] == 'c':
                arrout = arrout + chr(arr[zpl])
            else:
                arrout = arrout + str(arr[zpl])
        elif inp[i] == '.':
            arrout = ''
        elif inp[i] == 'i':
            s = float(input(arrout))
        i += 1

lamrop(x)
