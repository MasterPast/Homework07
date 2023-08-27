data = ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
     #   0   1   2   3   4

def decode(encoded_list):
    # print(type(encoded_list[0]))
    # print(type(encoded_list[1]))
    # print(isinstance(encoded_list[0], int))
    # print(isinstance(encoded_list[1], int))

    
    if not encoded_list:
        return []

    head = encoded_list[0]
    print(f'head>>> {head}')
    if isinstance(head, int):
        print(head)
        print(type(head))
        if len(encoded_list) >= 2:
            value = encoded_list[1]
            rest_of_list = encoded_list[2:]
            decoded_part = [value] * head
            print(decoded_part)
            return decoded_part + decode(rest_of_list)
        else:
            return []
    else:
        rest_of_list = encoded_list[1:]
        return [head] + decode(rest_of_list)
re = decode(data)
print(re)