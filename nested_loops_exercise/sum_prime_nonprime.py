data = input()

prime_sum = 0
non_prime_sum = 0


while data != 'stop':
    number = int(data)
    is_prime = True

    if number >= 0:
        for i in range(2, number):

            if (number % i) == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += number
        else:
            non_prime_sum += number

    else:
        print('Number is negative.')

    data = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
