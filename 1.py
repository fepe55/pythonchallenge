# http://www.pythonchallenge.com/pc/def/map.html


def option_1(s):
    '''We use a simple translation table'''
    import string

    original_alphabet = string.ascii_lowercase
    new_alphabet = original_alphabet[2:] + original_alphabet[:2]
    translation_table = str.maketrans(original_alphabet, new_alphabet)
    new_s = str.translate(s, translation_table)
    print(new_s)


def option_2(s):
    '''
    We take each character, and if it's a letter we add two to its ord
    Special cases y and z, where we have to wrap around
    '''

    first_code = ord('a')
    last_code = ord('z')
    difference = last_code - first_code

    new_s = ''

    for char in s:
        code = ord(char)
        if code not in range(first_code, last_code + 1):
            new_s += char
        else:
            new_code = first_code + (code - first_code + 2) % (difference + 1)
            new_s += chr(new_code)
    print(new_s)


def option_3(s):
    '''The most basic and clear one. Pretty straight-forward'''
    new_s = ''
    for char in s:
        char_ord = ord(char)
        if char_ord not in range(ord('a'), ord('z') + 1):
            new_s += char
        elif char == 'y':
            new_s += 'a'
        elif char == 'z':
            new_s += 'b'
        else:
            new_char = chr(char_ord + 2)
            new_s += new_char

    print(new_s)


if __name__ == '__main__':
    s = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc "
         "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr "
         "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. "
         "lmu ynnjw ml rfc spj.")

    url = 'map'

    option_1(s)
    option_2(s)
    option_3(s)

    option_1(url)
    option_2(url)
    option_3(url)
