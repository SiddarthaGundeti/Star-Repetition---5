# Star-Repetition---5

Explanation:

The task is to write a program that takes two words as input, W1 and W2, where W1 is composed of two parts: the first part is exactly W2, and the second part is the remaining characters in W1. The program should print W1 with the first part (which is W2) replaced by stars (*).

Logical Approach:

Read Inputs:
Read the word W1 and the word W2 from the input.

Determine Length of W2:
Calculate the length of W2. This will be the number of stars to be printed in place of W2 in W1.

Create the Output String:
Replace the first part of W1 (which is exactly W2) with stars. The number of stars should be equal to the length of W2.
Append the remaining part of W1 (after the W2 part) to these stars.

Print the Result:
Output the modified string.

Example for Clarity:

For the input W1 = "Subway" and W2 = "Sub", the first part of W1 is exactly W2 which is "Sub". The length of "Sub" is 3.
The program replaces "Sub" in "Subway" with three stars: "*".
The remaining part of "Subway" is "way", which is appended to "*".
Therefore, the output should be "*way".
