import string

ASCII_LOWERCASE = string.ascii_lowercase


def encode(plain_text):
    new_text = ""        # Variable to store the encoded text
    new_index = -1       # Variable to store the new index
    substring_list = []  # List to store substrings

    for ch in plain_text:
        if ch.isalpha():    # Check if the character is an alphabet
            new_index = 25 - ASCII_LOWERCASE.index(ch.lower()) # Calculate the new index
            new_text += ASCII_LOWERCASE[new_index] # Add the encoded character to the new text
        else:
            if ch.isnumeric():    # Check if the character is a number
                new_text += ch    # Add the number to the new text
    # Split the string at every five characters
    substring_list = [new_text[ch:ch+5] for ch in range(0, len(new_text), 5)]

    return " ".join(substring_list) # Join the substrings with spaces and return the encoded text


def decode(ciphered_text):
    joined_text = ciphered_text.replace(" ", "") # Remove spaces from the ciphered text
    # Create a translation table to map each character to its decoded counterpart
    translation_table = str.maketrans(ASCII_LOWERCASE[::-1], ASCII_LOWERCASE)

    # Use the translate() method to decode the text
    new_text = joined_text.translate(translation_table)

    return new_text # Return the decoded text
