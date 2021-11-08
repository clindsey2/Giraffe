
lucky_numbers = [42, 4, 8, 15, 16, 23]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)

print(friends.index("Oscar"))
# print(friends.index("Mike"))

print(friends.count("Karen"))

lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()

lucky_numbers.reverse()
print(lucky_numbers)

friends.clear()
print(friends)

print(friends2)

