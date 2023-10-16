import re

# Sample text
text = "Hello, my email addresses are john@example.com and jane123@gmail.com. Please contact me."

# Define a regular expression pattern to match email addresses
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'

# Use re.findall() to find all email addresses in the text
email_addresses = re.findall(email_pattern, text)

# Use re.search() to find the first occurrence of an email address in the text
first_email = re.search(email_pattern, text)

# Print the results
print("All email addresses found:", email_addresses)
if first_email:
    print("First email address found:", first_email.group())
else:
    print("No email address found.")
