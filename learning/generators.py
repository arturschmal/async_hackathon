def elements(my_list):
    for element in my_list:
        yield element

def infinite_list_of_even_numbers():
    i = 0
    while True:
        yield i * 2
        i += 1


a_list = [i for i in range(10)]
print(f"Total elements is {[element for element in elements(a_list)]}")

endless_numbers = infinite_list_of_even_numbers()
for _ in range(30):
    print(next(endless_numbers))

print(type(range(10)))