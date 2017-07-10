from collections import defaultdict

animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print(animal['Nick'])
# Monkey

print(animal)
# defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})
