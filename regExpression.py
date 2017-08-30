"""
How to create regular expression and using it
"""
"""

* Zero or more
? Zero or one / if put at the end of patterns will do nongreedy search
+ One or more
[] defining your own classes
{} for a specific number of times
{start,Limit} for a range of number of times
^ should start with that string/pattern
$ should end with the string/pattern
.  will match any character except for a newline.
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S Any character that is not a space, tab, or newline.
"""

import re

""" Search will return a matching object if found otherwise will return None """
regNumExp = re.compile(r'(\d){4}-(\d){3}-(\d){7}')
mo = regNumExp.search("Call me on 0092-315-9780625") # Searching for one instance/data/item
print(mo.group()) # for getting the matched object

""" Findall will return a list of data found"""
regExp = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d\d\d\d\d)')
match = regExp.findall("Call me on 0092-315-9780625 or you can call on the other number 0092-315-9780624")
print(match)

""" Sub method to replace a certain pattern"""

namesRegex = re.compile(r'Agent \w+')
result = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

agentRegEx = re.compile(r'Agent (\w)\w*')
stars = agentRegEx.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(stars)

""" 
re.IGNORECASE for ignoring the case of the pattern
re.DOTALL for having  newlines to match the dot character
re.VERBOSE for writing comments in your regex
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


"""