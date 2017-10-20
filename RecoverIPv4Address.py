# Collections module has already been imported.
def is_valid_ipv4_section(input):
    '''
    features of a section as ipv4
    1. numbers in range of [0..255]
    the following format is acceptable,
        1,
        255
        03
        030
    '''
    #if more than one digit, the first digit cannot be zero
    #if len(input) > 1 and input[0] == '0':
    #    return False
    #every digit must be in [0..9]
    num_0 = ord('0')
    num_9 = ord('9')
    for ch in input:
        num = ord(ch)
        if num < num_0 or num > num_9:
            return False
    try:
        num = int(input)
        return num >= 0 and num <= 255
    except:
        return False

def generate_sub_sections(current_section, input):
    min_length = 4 - current_section
    if len(input) < min_length:
        return []
    max_length = min_length * 3
    if len(input) > max_length:
        return []

    #base case
    generated = []
    if current_section == 3 and is_valid_ipv4_section(input):
        generated.append(input)
        return generated

    part_len = 1
    length = len(input)
    while part_len <= 3:
        part = input[0:part_len]
        #there is enough for rest of parts
        if length - part_len >= (4 - current_section - 1) and is_valid_ipv4_section(part):
            sub_list = generate_sub_sections(current_section+1, input[part_len:])
            for item in sub_list:
                generated.append(part + "." + item)
        else:
            break
        part_len += 1

    return generated

def generate_ip_address(input):
    # Return type should be a List.
    return generate_sub_sections(0, input)

def generate_ip_address_v2(input):
    '''
    do it iteratively in stead of recursively
    '''
    import collections
    class IPV4AddressParser:
        def __init__(self, level, input_str, prefix):
            self.level = level
            self.input = input_str
            self.prefix = prefix

    if input is None:
        return []
    length = len(input)
    if length < 4 or length > 12:
        return []
    generated = []
    que = collections.deque()
    que.append(IPV4AddressParser(1, input, ""))
    while que:
        item = que.popleft()
        if item.level == 4 and is_valid_ipv4_section(item.input):
            generated.append(item.prefix + "." + item.input)
        else:
            sub_length = len(item.input)
            for i in range(1, 4):
                if i < sub_length:
                    part = item.input[0:i]
                    if is_valid_ipv4_section(part):
                        new_prefix = item.prefix + "." + part if item.prefix else part
                        que.append(IPV4AddressParser(item.level+1, item.input[i:], new_prefix))
    return generated

def test():
    test_inputs = ['19216801', '1921682040', '255255255255', '0000', '2551025510']
    for input in test_inputs:
        print("input:", input)
        print("results:", generate_ip_address(input))
        print("results v2:", generate_ip_address_v2(input))

test()