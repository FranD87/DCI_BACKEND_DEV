from typing import Any, NoReturn


def age_range_validator(value: Any) -> NoReturn:
    if value < 18:
        raise ValueError("age cannot be below 18, You are too young")
    elif value > 60:
        raise ValueError("age cannot be older than 60, You are too old")

def age_type_validator(value: Any) -> NoReturn:
        if not isinstance(value, int):
            raise TypeError("age must be an integer")


if __name__ == '__main__':
    age = 70
    age_range_validator(age)
    print(f'Your age is {age}')

'''
The provided code includes two validator functions (`age_range_validator` and `age_type_validator`) and a small code 
snippet that demonstrates the usage of the `age_range_validator` function.

Function: age_range_validator(value: Any) -> NoReturn
- Validates the age value passed as an argument.
- If the value is less than 18, raises a ValueError with the message "age cannot be below 18, You are too young."
- If the value is greater than 60, raises a ValueError with the message "age cannot be older than 60, You are too old."

Function: age_type_validator(value: Any) -> NoReturn
- Validates that the age value passed as an argument is an integer.
- If the value is not an instance of an integer, raises a TypeError with the message "age must be an integer."

Code Snippet:
- Sets the `age` variable to 70.
- Calls the `age_range_validator` function with the `age` variable as an argument.
  - Since the `age` value exceeds the allowed range (60), a ValueError is raised.
- Prints the age value in the console if the validation passes.

This code snippet demonstrates the usage of the `age_range_validator` function by attempting to validate an age value 
of 70. As the value exceeds the allowed range, a ValueError is raised and the program execution stops.
'''