# Step-by-Step Procedure for Hackathon Participants

## Objective

In this task, you will use a Python script to collect plaintext and ciphertext data from an Arduino device running AES encryption.

## Hardware Requirements

* Arduino board
* USB cable
* Oscilloscope

## Connection to Oscilloscope

The pin 13 of Arduino board will be used for the trigger pin (must be connect to a oscilloscope via a probe). 

## Setps:

* Port `COMX` (change the port name accordingly)
* Call `sleep(10)` (wait for 10 seconds to ensure that the Arduino is ready)
* Call `sleep(1)` to wait for 1 second after the encryption (to ensure traces are collected correctly at the oscilloscope)
  

# Verification

## Plaintext and Ciphertext
After the script completes, check the following files in the same directory:

* plaintext.npy: This file should contain a NumPy binary file with the collected plaintext data.
* ciphertext.npy: This file should contain a NumPy binary file with the collected ciphertext data.

## Oscilloscope
The number of traces collected from the oscilloscope should match the number of plaintext and ciphertext entries above.



## Our Answer:
Unfortunately we werent able to do this Challenge within the time limit of the NiCE Hack Hackathon in time so we do not have any answers for this final challenge... 