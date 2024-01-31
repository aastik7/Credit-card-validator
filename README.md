# Credit Card Validator - Luhn Algorithm

## Overview
This Python script validates credit card numbers using the Luhn Algorithm, a widely used checksum formula for identifying errors in identification numbers such as credit card numbers.

## Usage
1. Run the script by executing the Python file.
2. Enter a credit card number when prompted.
3. The script will apply the Luhn Algorithm to determine if the entered credit card number is valid or invalid.
4. It will output "VALID" for a valid credit card number and "INVALID" otherwise.

## How it Works
The script performs the following steps:

1. **Input and Formatting:**
   - Removes spaces and hyphens from the entered credit card number.
   - Reverses the order of the digits for processing.

2. **Summing Odd Digits:**
   - Iterates over the digits at odd positions and adds them.

3. **Summing Even Digits:**
   - Iterates over the digits at even positions.
   - Doubles each even-positioned digit, adjusting for digits greater than or equal to 10.
   - Adds the modified digits to the sum.

4. **Calculating Total:**
   - Sums both the odd and even digit sums.

5. **Checking Validity:**
   - Checks if the total sum is divisible by 10.
   - Outputs "VALID" if valid, and "INVALID" if not.

## Example
For example, if you enter the credit card number `4532-7163-7586-8985`, the script will output "VALID."

## Note
This script is a basic implementation and assumes a valid input format. It does not verify the length or other aspects of credit card numbers.

Feel free to use and modify this script for your needs!

