import pprint

message = 'It was a bright cold day in Aprile, and the clocks were striking two'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(pprint.pformat(count))
