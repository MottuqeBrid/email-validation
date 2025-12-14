# Email Validation Using Python

A Python project demonstrating two different approaches to email validation: manual rule-based validation and regex-based validation.

## Overview

This project provides two command-line email validation tools that check if email addresses meet specific formatting requirements. Both implementations run in an interactive loop, allowing users to validate multiple email addresses until they choose to exit.

## Project Structure

```
email-validation/
├── main.py                      # Manual rule-based email validation
├── regex_email_validation.py    # Regex-based email validation
└── README.md                    # Project documentation
```

## Features

- **Two Validation Approaches**: Compare manual validation vs regex-based validation
- **Interactive CLI**: Both programs run in continuous loops until user exits
- **Clear Feedback**: Provides validation results with appropriate messages
- **Educational Purpose**: Demonstrates different programming approaches to the same problem

## Implementation Details

### 1. Manual Validation (`main.py`)

This implementation uses a step-by-step manual validation approach with explicit rule checking.

#### Validation Rules

The `check_email()` function enforces the following rules in sequence:

1. **Minimum Length**: Email must be at least 6 characters long
2. **First Character**: Must be an alphabetic character (a-z)
3. **@ Symbol**: Must contain exactly one "@" symbol
4. **Domain Extension**: Must have a "." at the 4th or 3rd position from the end (e.g., `.com`, `.in`)
5. **No Spaces**: Email cannot contain any whitespace characters
6. **No Uppercase**: Email cannot contain uppercase letters (lowercase only)
7. **Allowed Characters**: Only alphanumeric characters, "@", ".", and "\_" are permitted

#### Code Analysis

- Uses flag variables (`k`, `j`, `d`) to track validation errors
- Implements nested if-else structure for sequential validation
- Provides specific error messages for different failure points
- Uses XOR operator (`^`) to check domain extension position

#### Error Messages

- `Wrong email format 1`: Email is too short (< 6 characters)
- `Wrong email format 2`: First character is not alphabetic
- `Wrong email format 3`: Invalid "@" symbol (missing or multiple)
- `Wrong email format 4`: Invalid domain extension (missing or incorrectly positioned ".")
- `Wrong email format 5`: Contains spaces or uppercase letters
- `Wrong email format 7`: Contains invalid characters or formatting issues

### 2. Regex-Based Validation (`regex_email_validation.py`)

This implementation uses Python's `re` module with a regular expression pattern for validation.

#### Validation Pattern

```python
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
```

#### Pattern Breakdown

- `^[a-z]+`: Starts with one or more lowercase letters
- `[\._]?`: Optionally contains a dot or underscore
- `[a-z 0-9]+`: Followed by lowercase letters, spaces, or digits
- `[@]`: Contains exactly one "@" symbol
- `\w+`: Domain name (word characters)
- `[.]`: Literal dot
- `\w{2,3}`: Domain extension (2-3 characters)
- `$`: End of string

#### Code Analysis

- Concise implementation using regex pattern matching
- Single validation check using `re.search()`
- Simpler code structure (fewer lines)
- Less detailed error messages (only "Valid email" or "Invalid email")

## Usage

### Running Manual Validation

```bash
python main.py
```

### Running Regex Validation

```bash
python regex_email_validation.py
```

### Example Session (Both Programs)

```
Enter 'exit' to exit the program
Enter your email: user@example.com
Valid email
Enter 'exit' to exit the program
Enter your email: User@example.com
Invalid email (or "Wrong email format 7" in main.py)
Enter 'exit' to exit the program
Enter your email: exit
```

## Comparison

| Feature             | Manual Validation (`main.py`)        | Regex Validation (`regex_email_validation.py`) |
| ------------------- | ------------------------------------ | ---------------------------------------------- |
| **Code Length**     | ~51 lines                            | ~23 lines                                      |
| **Complexity**      | Higher (nested conditionals)         | Lower (single regex pattern)                   |
| **Error Messages**  | Detailed (7 different messages)      | Simple (valid/invalid)                         |
| **Maintainability** | More verbose, easier to modify rules | Concise, harder to modify pattern              |
| **Performance**     | Multiple sequential checks           | Single pattern match                           |
| **Readability**     | More explicit logic                  | Requires regex knowledge                       |
| **Flexibility**     | Easy to add/remove rules             | Requires regex pattern modification            |

## How It Works

### Both Implementations Follow Similar Flow:

1. Program starts an infinite `while True` loop
2. Prompts user to enter an email address
3. If user enters "exit", program terminates
4. Otherwise, email is passed to `check_email()` function
5. Function performs validation checks
6. Prints validation result

### Key Differences:

- **main.py**: Performs multiple sequential checks with detailed error tracking
- **regex_email_validation.py**: Uses a single regex pattern match for validation

## Requirements

- Python 3.x
- `re` module (built-in, no installation needed)

## Code Analysis & Observations

### Strengths

**Manual Validation (`main.py`):**

- Explicit validation logic is easy to understand step-by-step
- Detailed error messages help identify specific issues
- Good for learning validation concepts

**Regex Validation (`regex_email_validation.py`):**

- Concise and efficient
- Industry-standard approach
- Less code to maintain

### Limitations

**Manual Validation:**

- More verbose code
- Potential for bugs in complex logic (e.g., line 14: `i == i.isspace()` should be `i.isspace()`)
- Harder to extend with new rules

**Regex Validation:**

- Pattern allows spaces in email (may not be desired)
- Less flexible for custom rule modifications
- Requires regex knowledge to understand or modify

### Potential Improvements

1. **main.py**: Fix the space check logic (`i.isspace()` instead of `i == i.isspace()`)
2. **main.py**: Fix the uppercase check logic (`i.isupper()` instead of `i == i.upper()`)
3. **regex_email_validation.py**: Remove space from pattern if spaces shouldn't be allowed
4. Both: Add email normalization (trim whitespace, convert to lowercase)
5. Both: Consider using `email-validator` library for production use

## Notes

- Both implementations are educational examples and may not match all RFC 5322 email standards
- Manual validation requires lowercase letters only
- Regex validation pattern allows spaces (which may not be standard)
- Domain extensions must be 2-3 characters long in both implementations
- For production applications, consider using established libraries like `email-validator` or `validate_email`

## License

This project is open source and available for educational purposes.
