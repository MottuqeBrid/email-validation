# Email Validation Using Python

A simple Python program that validates email addresses based on custom validation rules.

## Overview

This project provides a command-line email validation tool that checks if an email address meets specific formatting requirements. The program runs in an interactive loop, allowing users to validate multiple email addresses until they choose to exit.

## Features

- Validates email addresses according to custom rules
- Interactive command-line interface
- Continuous validation loop until user exits
- Clear error messages indicating validation failures

## Validation Rules

The email validation function (`check_email`) enforces the following rules:

1. **Minimum Length**: Email must be at least 6 characters long
2. **First Character**: Must be an alphabetic character (a-z)
3. **@ Symbol**: Must contain exactly one "@" symbol
4. **Domain Extension**: Must have a "." at the 4th or 3rd position from the end (e.g., `.com`, `.in`)
5. **No Spaces**: Email cannot contain any whitespace characters
6. **No Uppercase**: Email cannot contain uppercase letters (lowercase only)
7. **Allowed Characters**: Only alphanumeric characters, "@", ".", and "\_" are permitted

## Usage

### Running the Program

```bash
python main.py
```

### Example Session

```
Enter 'exit' to exit the program
Enter your email: user@example.com
Valid email
Enter 'exit' to exit the program
Enter your email: User@example.com
Wrong email format 7
Enter 'exit' to exit the program
Enter your email: exit
```

## How It Works

1. The program starts an infinite loop
2. Prompts the user to enter an email address
3. If the user enters "exit", the program terminates
4. Otherwise, the email is passed to the `check_email()` function
5. The function performs multiple validation checks in sequence
6. Prints either "Valid email" or an error message indicating which validation rule failed

## Error Messages

The program provides different error messages for different validation failures:

- `Wrong email format 1`: Email is too short (< 6 characters)
- `Wrong email format 2`: First character is not alphabetic
- `Wrong email format 3`: Invalid "@" symbol (missing or multiple)
- `Wrong email format 4`: Invalid domain extension (missing or incorrectly positioned ".")
- `Wrong email format 5`: Contains spaces or uppercase letters
- `Wrong email format 7`: Contains invalid characters or formatting issues

## Requirements

- Python 3.x

## Project Structure

```
email-validation/
├── main.py          # Main program file containing validation logic
└── README.md        # Project documentation
```

## Notes

- This is a custom email validation implementation and may not match all RFC 5322 email standards
- The validation is case-sensitive and requires lowercase letters only
- Domain extensions must be 2-3 characters long (e.g., `.com`, `.in`, `.org`)

## License

This project is open source and available for educational purposes.
