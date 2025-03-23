#togggle each characters in a string
def toggle_string(s):
    toggled=""
    for char in s:
        if char.isupper():
            toggled +=char.lower()
        else:
            toggled += char.upper()
    return toggled
text="Toggle ME"
print("Toggled string:", toggle_string(text))