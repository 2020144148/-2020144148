Exercise 5: Take the following Python code that stores a string: str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the colon characterand then use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence:0.8475'
moral_str = str.split(':')[1]
result = float(moral_str)
print(result)