# Dictionaries(topic11)

phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
# your code goes here
del phonebook["Jill"]
print(phonebook)
phonebook["Jake"] = 987636523

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
