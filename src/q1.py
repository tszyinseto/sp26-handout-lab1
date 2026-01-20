"""
Please implement these stub functions to match the documentation.
Make sure to implement tests in the tests directory.
"""


def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """

    is_valid = True
    
    # Check requirement 1: at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        is_valid = False
    
    # Check requirement 2: at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        print("Password must contain at least one uppercase letter")
        is_valid = False
    
    # Check requirement 3: at least one lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        print("Password must contain at least one lowercase letter")
        is_valid = False
    
    # Check requirement 4: at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print("Password must contain at least one digit")
        is_valid = False
    
    # Check requirement 5: at least one special character
    special_chars = "!@#$%^&*"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if not has_special:
        print("Password must contain at least one special character (!@#$%^&*)")
        is_valid = False
    
    return is_valid
