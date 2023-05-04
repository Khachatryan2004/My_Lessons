# Define a function that takes a message and a shift value as inputs
def caesar_cipher(message, shift):
    # Create an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Get the ASCII code for the character
            char_code = ord(char)
            # Shift the code by the specified amount
            shifted_code = char_code + shift
            # Check if the shifted code is outside the range of letters (65-90 for uppercase, 97-122 for lowercase)
            if char.isupper() and shifted_code > 90 or char.islower() and shifted_code > 122:
                # If so, wrap around to the other end of the alphabet
                shifted_code -= 26
            # Convert the shifted code back to a character and add it to the encrypted message
            encrypted_message += chr(shifted_code)
        else:
            # If the character is not a letter, just add it to the encrypted message
            encrypted_message += char

    # Return the encrypted message
    return encrypted_message


# Get the message and shift value from the user
message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(message, shift)

# Print the encrypted message
print("Encrypted message:", encrypted_message)

# Decrypt the message using the opposite shift value
decrypted_message = caesar_cipher(encrypted_message, -shift)

# Print the decrypted message
print("Decrypted message:", decrypted_message)