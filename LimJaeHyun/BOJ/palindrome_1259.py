def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return 'yes'
    else:
        return 'no'
    
while True:
    number = int(input())
    if number:
        print(is_palindrome(number))
    else:
        break