import re


def validate(cpf):
    j=0
    total=0
    for i in range(10, 1, -1):
        total += int(cpf[j]) * i
        j += 1
    first_digit = 11 - total % 11
    first_digit = 0 if first_digit > 9 else first_digit
    #print(first_digit)
    if first_digit != int(cpf[9]):
        return False
    j=0
    total=0
    for i in range(11, 1, -1):
        total += int(cpf[j]) * i
        j += 1
    second_digit = 11 - total % 11
    #print(second_digit)
    second_digit = 0 if second_digit > 9 else second_digit
    #print(second_digit)
    if second_digit != int(cpf[10]):
        return False

    return True

def find_cpfs():
    cpf = "XXX11111111"
    res = re.match("X+", cpf)

    idx_start = res.span()[0]
    idx_end = res.span()[1]
    size = idx_end - idx_start

    nums = pow(10, size) - 1
    for i in range(nums):
        curr = str(i).ljust(size, '0')
        start = cpf[:idx_start]
        end = cpf[idx_end:]

        curr_cpf = start + curr + end
        if validate(curr_cpf):
            print(curr_cpf)


if __name__ == '__main__':
    print(validate("01234567890"))
    find_cpfs()


