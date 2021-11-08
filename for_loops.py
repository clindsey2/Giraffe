
friends = ["Jim", "Karen", "Kevin"]

for letter in "Giraffe Academy":
    print(letter)

for friend in friends:
    print(friend)

for index in range(10):
    print(index)

print("==================")

for index in range(3, 10):
    print(index)

print("-------------------")

# range starts with zero and goes to length of friends - minus 1
for index in range(len(friends)):
    print(friends[index])

print("####################")

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")
