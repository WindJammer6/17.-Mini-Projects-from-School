# Task
You are performing a side-channel analysis of an encrypted device. Based on the analysis, you are uncertain about one of the 16 key bytes. How will you approach obtaining all the correct key bytes?

Once the key is extracted, you need to submit:

* The correct 16-byte key
* The Power Model and Target used to obtain the correct key
* A description of the approach to obtain the key in bullet points (no more than 5 points)
* Any Python scripts used for the above approach

## Procedure
1. Build a project file using the given traces, plaintext, and ciphertext.
2. Perform side-channel analysis to retrieve the key.
3. Verify the retrieved key with the plaintext and ciphertext to ensure it is correct.


## Our Answers:
* The correct 16-byte key: 

* The Power Model and Target used to obtain the correct key: Model: Hamming Distance |Target: (PT^KEY) ^ (SB(PT^KEY))

* A description of the approach to obtain the key in bullet points (no more than 5 points): 
a. Collect Traces and Data:
Obtain side-channel traces (e.g., power consumption measurements) from the encryption device. Ensure you have corresponding plaintexts and ciphertexts for each trace.

b. Model the Power Leakage:
Use the Hamming Distance model, as specified, to model the power consumption. The Hamming Distance model calculates the number of differing bits between intermediate values during encryption (such as PT^KEY and SB(PT^KEY)).

c. Focus on a Specific Target:
Your target is: (PT^KEY) ^ (SB(PT^KEY)). This means you are analyzing the XOR between the plaintext XORed with the key and the output of the substitution box (S-Box) during encryption.

d. Perform Correlation Power Analysis (CPA):
For each possible key byte guess, calculate the hypothetical power consumption based on the Hamming Distance model. Compute the correlation between the hypothetical power consumption and the actual power traces for each key guess. Identify the key byte guess with the highest correlation for each byte.

e. Verify and Reassemble the Key:
Verify the retrieved key by comparing the output of the encryption algorithm using the found key with the actual ciphertext. If the ciphertext matches, you have successfully retrieved the correct key.

* Any Python scripts used for the above approach: See the 'challenge2_2.py' Python file