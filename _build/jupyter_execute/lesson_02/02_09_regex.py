#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions
# 
# Regex, short for regular expression, is a sequence of characters that forms a search pattern. It's a powerful tool used in computer science and programming for matching and manipulating text strings.
# 
# Regex allows you to define a pattern using a combination of special characters and literals. These patterns can be used to search, match, and replace strings in a flexible and efficient manner.
# 
# Here are a few common use cases of regex:
# 
#    1. Pattern matching: Regex can be used to check if a string matches a specific pattern. For example, you can use regex to verify if an email address is valid or if a phone number is in the correct format.
#    2. Search and extraction: Regex enables you to search for specific patterns within a larger text and extract the matching portions. For instance, you can extract all URLs from a webpage or find all occurrences of a particular word in a document.
#    3. Validation and data cleaning: Regex is often employed to validate user input or to clean up data. It allows you to enforce specific rules on the format or structure of input data. For example, you can use regex to ensure that a password meets certain complexity requirements or remove unwanted characters from a text file.
#    4. Text manipulation: Regex provides powerful tools for modifying and transforming text. You can use it to find and replace specific patterns, add or remove certain elements, or reformat text according to your needs.
# 
# Regex syntax may vary slightly depending on the programming language or tool you are using, but the basic concepts and most commonly used symbols are generally consistent. Regex can be a complex topic, but mastering it can greatly enhance your ability to work with text in various programming and data processing tasks.
# 
# ## Examples
# Here are some examples of how regular expressions (regex) can be used with a novel:
# 
# Find All Occurrences of a Character:
# 
#     [Aa]lice
# 
# This regex pattern will match both "Alice" and "alice" in the text. You can use it to find all instances of the character name "Alice" regardless of the capitalization.
# 
# Match Dialogue:
# 
#     "[^"]+"
# 
# This regex pattern can be used to match dialogue within quotation marks. It will capture any text enclosed in double quotation marks, which is commonly used to represent spoken words in a novel.
# 
# Replace All Instances of a Word:
# 
#     \bcat\b
# 
# This regex pattern will match the word "cat" as a whole word and not as part of another word. You can use it to replace all instances of the word "cat" with another word or phrase.
# 
# Find Sentences Ending with an Exclamation Mark:
# 
#     [^.!?]*!
# 
# This regex pattern will match sentences that end with an exclamation mark. It captures all text before the exclamation mark, allowing you to identify and analyze instances of exclamation in the novel.
# 
# Match Character Descriptions:
# 
#     [A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+
# 
# This regex pattern can be used to match character names in title case. It assumes that character names consist of two words, with the first letter capitalized for each word. You can use it to identify character introductions and analyze their presence in the novel.
# 
# These examples demonstrate how regex can be used to search for and manipulate text patterns within a novel. The specific patterns you use will depend on the context and requirements of your analysis.
# 
# Mocktext created by ChatGPT
