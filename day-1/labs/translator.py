
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "b".upper()
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))