def decimalBinary(h):
    intger_number = int(input('Please input an integer'))

result = ''  

for x in range(8):

    r = integer_number % 2 
    integer_number = integer_number//2
    result += str(r)

result = result[::-1]

print(result)
