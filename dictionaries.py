
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
# Key: Value pairs above

numMonthConversions = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}
# Key: Val

print(monthConversions['Dec'])
print(monthConversions.get('Oct'))

print(numMonthConversions.get(1))
print(numMonthConversions.get(7))
print(numMonthConversions[3])

print(monthConversions.get('Lux', "Lux: is not a valid key"))
