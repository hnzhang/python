def decode_string(msg):
    if not msg:
        return 0
    ret_val = 0
    #for single digit
    num = int(msg[0:1])
    if num > 0 and num < 27:
        sub_str = msg[1:]
        if sub_str:
            ret_val += decode_string(sub_str)
        else:
            ret_val += 1
    if len(msg) > 1 and msg[0] != '0':
        num = int(msg[0:2])
        if num > 0 and num < 27:
            sub_str = msg[2:]
            if sub_str:
                ret_val += decode_string(sub_str)
            else:
                ret_val += 1

    return ret_val

def test():
    test_cases = ['2202', '29', '21234', '113021', '521']
    for test_str in test_cases:
        print(test_str, decode_string(test_str))

test()