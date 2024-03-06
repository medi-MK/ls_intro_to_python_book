info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# method 1

new_info = info.split(':')
print('+'.join(new_info))

# method 2

new_info2 = info.replace(':', '+')
print(new_info2)

