#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

example:
What is your name:Dwayne Johnson
What is your email:rock@aol.com

Your name is Dwayne Johnson, and your email is rock@aol.com

What is your name:Jackie Chan
What is your email:crazyAsian@qq.com

Your name is Jackie Chan, and your email is crazyAsian@qq.com

"""

name = ("What is your name? ")
email = ("What is your email? ")
name_answer = input(name)
email_answer = input(email)
print(f"You have entered the following information\nName: {name_answer}\nEmail: {email_answer}")