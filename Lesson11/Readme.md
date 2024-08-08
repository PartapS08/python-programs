### Index ###

    Regex Patterns

#### Description ####

Regular Expressions are sequences of characters that define a search pattern.

Metacharacters: Special characters with specific meanings in regex, such as:
- . : Matches any single character except a newline.
- ^ : Matches the start of a string.
- $ : Matches the end of a string.
- \* : Matches 0 or more repetitions of the preceding element.
- \+ : Matches 1 or more repetitions of the preceding element.
- ? : Matches 0 or 1 repetition of the preceding element.
- [] : A character class that matches any one character inside the brackets.
- | : Acts as an OR operator between expressions.
- \ : Escapes special characters or signals a special sequence.
- [a-zA-Z0-9] : This pattern matches any single alphanumeric character.
    - a-z : Matches any lowercase letter.
    - A-Z : Matches any uppercase letter.
    - 0-9 : Matches any digit.
- [a-zA-Z0-9]+ : matches sequences of 1 or more alphanumeric characters.

#### Example ####

Regex for matching email addresses like: support@example.com or sales@company.org

Ans: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

- [a-zA-Z0-9._%+-]+ : Matches one or more alphanumeric characters, dots (.), underscores (_), percent signs (%), plus signs (+), or hyphens (-). This part corresponds to the local part of the email (before the @ symbol)
- @ : Matches the @ symbol
- [a-zA-Z0-9.-]+ : Matches one or more alphanumeric characters, dots (.), or hyphens (-). This part corresponds to the domain name.
- \\. : Escapes the dot, ensuring it matches a literal dot (.).
- [a-zA-Z]{2,}: Matches two or more alphabetic characters, corresponding to the top-level domain (TLD), like .com, .org, etc.
- $ : Asserts the end of the string