# Question
You have captured a drone suspected of illegally delivering a package. You perform a side-channel analysis on the drone to obtain the encryption key. Given that the drone received an encrypted GPS location as `76 80 92 3E F4 F4 35 0F 90 FA 11 12 CE B9 7C FB` for its next delivery location, which GPS location should you investigate using the key?

Once the key is extraced, you need to submit

* The correct 16-byte key
* The decrypted GPS location 

## Procedure
1. Build a project file using the given traces, plaintext, and ciphertext.
2. Perform side-channel analysis to retrieve the key.
3. Verify the retrieved key with the plaintext and ciphertext to ensure it is correct.
4. Decrypt `76 80 92 3E F4 F4 35 0F 90 FA 11 12 CE B9 7C FB` using the key to obtain the GPS location.
5. Convert the decrypted GPS location from the plaintext to a human-readable format using UTF-8 encoding. The resulting GPS location should be in this format `2.1242, 106.6213`.


## Our Answers:
1. -
2. - 
3. - 
4. Correct 16-Byte key: 6F 2A 8E 39 1C D7 4B 90 A5 3E 6D 7A 8C 2F 91 04
5. 1.3586, 103.9899 