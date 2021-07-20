# Regular Expression

import re

pattern = '^p.*s$'
test_string = 'parents'
result = re.match(pattern, test_string)

if result:
    print("Found pattern.")
else:
    print("Pattern not found.")



