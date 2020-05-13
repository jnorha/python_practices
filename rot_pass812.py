#takes an input sting and rotation integer and returns the rotated string

def rotate_string(string, rotate):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    lower_string = string.lower()
    new_string = ''
    new_string_ls = []
    for i in lower_string:
        z = alph.find(i)
        if rotate >= 0:
            step = z + rotate
        elif rotate < 0:
            step = z + rotate
        if step <= 26:
            new_string_ls.append(alph[step])
        else:
            new_string_ls.append(alph[step - 27])
    x = new_string.join(new_string_ls)
    print x
    return x

d = str(raw_input('Password: '))
p = int(raw_input('Encription integer: '))

print rotate_string(d, p)
