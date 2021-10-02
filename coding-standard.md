# Coding Standards

## Variables 
- local variables must be lowercase and seperated with underscore (_).
- global variables must be uppercase and seperated with underscore (_).

##  Functions 
- functions should be lowercase with words seperated by underscores.
- mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility

## File structure
- keep packages and libraries seperated in the "modules" folder. 
- no wildcard (*) imports for security and performance reasons.
- use relative file paths for imports

## Comments
- comments on seperate lines in english only and one space followed by the comment 
