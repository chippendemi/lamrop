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
            if inp[i+1] == 'f':
                s = input(arrout)
                ls = 0
                try:
                    s = float(s)
                except ValueError:
                    ls = 0
                while ls == 0:
                    try:
                        s = float(s)
                        ls = 1
                    except ValueError:
                        ls = 0
                i += 1
            elif inp[i+1] == 'i':
                s = input(arrout)
                ls = 0
                try:
                    s = int(s)
                except ValueError:
                    ls = 0
                while ls == 0:
                    try:
                        s = int(s)
                        ls = 1
                    except ValueError:
                        ls = 0
                i += 1
            elif inp[i+1] == 'c':
                s = input(arrout)
                if zpl < len(s):
                    s = ord(s[zpl])
                i += 1
        i += 1

lamrop(x)
