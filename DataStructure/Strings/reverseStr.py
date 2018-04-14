def reverseStr(input):
    # First reverse the string
    first_str = input[::-1]
    str_list = first_str.split(' ')
    final_str = ''
    for _str in str_list:
        if final_str:
            final_str = final_str + ' ' + _str[::-1]
        else:
            final_str = _str[::-1]

    print final_str

reverseStr('abc')
reverseStr('abc def')
reverseStr('My name is ramendra')
