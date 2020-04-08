# GDU 2019 encoding an integer list into a shorter string
import math

# global_alphabet =
# '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-=+[]{}<>/?'
# abcdefghijklmnopqrstuvwxyz!@#$%^&*()-=+[]{}<>/?'
global_alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_stacking = '0123456789-/'
alphabet_5 = '01234'


def log(x):
    return math.log(x) / math.log(10)


def inter_decompress_string(string, bit_string):
    dec_bit_string = base_decode(bit_string, global_alphabet)
    bit_string = base_encode(dec_bit_string, alphabet_5)
    string = str(base_decode(string, global_alphabet))
    result = []
    number = int(string[0])
    current_bit = bit_string[0]
    for i in range(1, len(string)):
        # print(string[i], bit_string[i], number, current_bit)
        if bit_string[i] == "2":
            number = number * (10**int(string[i]))
        elif current_bit == bit_string[i]:
            number = number * 10 + int(string[i])
        elif int(current_bit) < 2:
            result.append(number)
            last_number = number
            current_bit = bit_string[i]
            number = int(string[i])
        elif int(current_bit) > 2:
            result.append(last_number - number)
            last_number = last_number - number
            current_bit = bit_string[i]
            number = int(string[i])
    if int(current_bit) < 2:
        result.append(number)
    elif int(current_bit) > 2:
        result.append(last_number - number)
    return result


def inter_compress_string(number_list):
    main_frame_bit = ["0", "0", "1"]
    main_frame_bit_position = 1
    diff_frame_bit = ["3", "3", "4"]
    diff_frame_bit_position = 1
    result, bit_string = del_zero(number_list[0], "1")
    for i in range(1, len(number_list)):
        difference = number_list[i - 1] - number_list[i]
        rm, bm = del_zero(number_list[i], main_frame_bit[
                          main_frame_bit_position])
        if difference < 0:
            result += rm
            bit_string += bm
            main_frame_bit_position = main_frame_bit_position * -1
        else:
            rd, bd = del_zero(difference, diff_frame_bit[
                              diff_frame_bit_position])
            if len(rd) > len(rm):
                result += rm
                bit_string += bm
                main_frame_bit_position = main_frame_bit_position * -1
            else:
                result += rd
                bit_string += bd
                diff_frame_bit_position = diff_frame_bit_position * -1
    dec_bit_string = base_decode(bit_string, alphabet_5)
    bit_string = base_encode(dec_bit_string, global_alphabet)
    result = base_encode(int(result), global_alphabet)
    return result, bit_string


def del_zero(number, bit_zero_or_one):
    number_in_string = str(number)
    result = number_in_string[0]
    bit_string = bit_zero_or_one
    zero_count = 0
    for i in range(1, len(number_in_string)):
        if number_in_string[i] == "0":
            zero_count += 1
        else:
            if zero_count > 0:
                result += str(zero_count)
                bit_string += "2"
                zero_count = 0
            result += str(number_in_string[i])
            bit_string += bit_zero_or_one
    if zero_count > 0:
        result += str(zero_count)
        bit_string += "2"
    return result, bit_string


def add_zero_back(number_string, bit_string):
    result = ''
    for i in range(len(number_string)):
        if bit_string[i] == "2":
            result += "0" * int(number_string[i])
        else:
            result += number_string[i]
    return int(result)


def parameter_to_string(parameter_list, max_list):
    # Both parameter list and max list should be positive integers
    result = parameter_list[0]
    for i in range(1, len(max_list)):
        result = result * max_list[i] + parameter_list[i]
    result = base_encode(result)
    # string = number_to_stacking_string(parameter_list)
    # dec_num = base_decode(string, alphabet=alphabet_stacking)
    # result = base_encode(dec_num, alphabet=global_alphabet)
    return result


def string_backto_parameter(input_key, max_list):
    input_key = base_decode(input_key)
    result = max_list
    for i in range(len(max_list) - 1, 0, -1):
        input_key, result[i] = divmod(input_key, max_list[i])
    result[0] = input_key
    # dec_num = base_decode(input_key, alphabet=global_alphabet)
    # string = base_encode(dec_num, alphabet=alphabet_stacking)
    # result = stacking_string_to_number_list(string)
    return result


def number_to_stacking_string(input_list):
    # the input list should only be integers
    result = ''
    for i in input_list:
        result += str(i) + '/'
    return result[:-1]


def stacking_string_to_number_list(input_string):
    return [int(_) for _ in input_string.split('/')]


def base_encode(number, alphabet=global_alphabet):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int)):
        raise TypeError('number must be an integer')
    base36 = ''
    sign = ''
    if number < 0:
        sign = '-'
        number = -number
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
    return sign + base36


def base_decode(number_string, alphabet=global_alphabet):
    result = 0
    number_string = number_string.upper()
    for i in range(len(number_string)):
        result += len(alphabet)**(len(number_string) - i - 1) * \
            alphabet.find(number_string[i])
    return result  # int(number, 36)


def page_key_compress(parameter_list, max_list):
    # [first_num_min, first_num_max, second_num_min,
    #      second_num_max, result_max, operator_in_number, randseed]
    operator_seed_string = parameter_to_string(
        parameter_list[-2:], max_list[-2:])
    #print(parameter_list[-2:], max_list[-2:])
    [first_num_min, first_num_max, second_num_min,
     second_num_max, result_max] = parameter_list[:-2]
    string1, bit_string = inter_compress_string(
        [first_num_min, second_num_min, first_num_max, second_num_max, result_max])
    return string1 + '-' + bit_string + '-' + operator_seed_string


def page_key_decompress(input_key, max_list):
    [string1, bit_string, operator_seed_string] = input_key.split('-')
    [operator_in_number, randseed] = string_backto_parameter(
        operator_seed_string, max_list[-2:])
    [first_num_min, second_num_min, first_num_max, second_num_max,
        result_max] = inter_decompress_string(string1, bit_string)
    return [first_num_min, first_num_max, second_num_min,
            second_num_max, result_max, operator_in_number, randseed]


def main():
    print(base_encode(1412823931503067241))
    print(base_decode('AQF8AA0006EH'))
    max_list = [  # 20000,  # problem list max 20k
        2000,  # num min and max both have -1000 to 1000 range thus 0-1999
        2000,
        2000,
        2000,
        1000001,  # result max in 1M
        5,  # operator 1-4
        65535  # max of rand seed
    ]
    page_key = parameter_to_string([
        2 + 100, 100 + 999, 2 + 100,
        100 + 999, 1000, 1, 23423], max_list)
    print(page_key)
    print(string_backto_parameter(page_key, max_list))
    print(number_to_stacking_string(max_list))
    print(stacking_string_to_number_list(number_to_stacking_string(max_list)))
    print(string_backto_parameter('page_key@#$!@#!$', max_list))

    print(del_zero(10000, "1"))
    s1, s2 = del_zero(1234000, "1")
    print(add_zero_back(s1, s2))
    s1, s2 = inter_compress_string([
        2 + 1000,  2 + 1000, 100 + 999,
        100 + 999, 10000])
    print(s1, s2)
    print(inter_decompress_string(s1, s2))
    max_list = [  # 20000,  # problem list max 20k
        2000,  # num min and max both have -1000 to 1000 range thus 0-1999
        2000,
        2000,
        2000,
        1000001,  # result max in 1M
        5,  # operator 1-4
        65535  # max of rand seed
    ]
    print(max_list)
    s = page_key_compress([
        2 + 10000, 1999 + 999, 2 + 10000,
        1000 + 999, 150, 1, 23423], max_list)
    print(s)
    print(page_key_decompress(s, max_list))
    print(max_list)

if __name__ == "__main__":
    # execute only if run as a script
    main()
