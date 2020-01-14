#reads name.txt into a variable my_name
with open('name.txt') as f:
    my_name = f.read()

print(my_name)

#writes new file named hello.txt with greeting
with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + my_name)
    f.write('\n')

