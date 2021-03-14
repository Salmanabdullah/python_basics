# String basics
# for multi line String we use triple quotes ''' '''
text = '''
Hi Nelly,

This is a test email to you.

Thank you
Salman'''

print(text)

# to find the index 
text = 'I wanna sleep. I\'m to tired' # \ backslash to avoid inverted comma
print(text)
print(text[0])
print(text[0:3])
print(text[1:-1])

first = 'John'
last = 'Smith'
msg = first +' ['+last+'] is a coder'
msg_formatted = f'{first} [{last}] is a coder'
# curly braces define the placeholders
print(msg)
# formatted string is very useful. Easy to visualize
print(msg_formatted)