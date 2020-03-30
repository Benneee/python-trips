# Find and replace
# Find
msg = 'Hello everyone, I love python and python';
check = msg.find('python');
# Returns the starting position/index of the string python
# print(check);

# Replace
msg2 = msg.replace('python', 'angular', 1)
# print(msg2);


# String Formatting
name = 'Benneee';
color = 'black';

msg3 = f'{name} loves the color {color}'
print(msg3)
