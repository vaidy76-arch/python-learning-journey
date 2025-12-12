# Day 2 Notes

## What I Learned
- Data types: str, int, float, bool
- F-strings are the best way to format strings
- // is different from / for division


# Day 5 Notes

## Key Learnings

### Dictionaries are Flexible!
- Can add new keys anytime: `student["average"] = 84.5`
- Don't need to predefine structure (unlike C structs)
- Can check if key exists: `if "key" in dict:`

### Lambda Functions
- `lambda x: x[1]` - anonymous function for quick operations
- Used with max(), min(), sorted() for custom comparisons

### My Questions
- Q: Why not add average to same dictionary?
- A: You CAN! Just do `student["average"] = avg`


## Exception Hierarchy for Files
```
BaseException
 └── Exception
      └── OSError (base for most file errors)
           ├── FileNotFoundError
           ├── PermissionError
           ├── FileExistsError
           ├── IsADirectoryError
           ├── NotADirectoryError
           └── IOError (alias for OSError in Python 3+)