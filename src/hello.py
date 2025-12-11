#!/usr/bin/env python3
"""
A simple Hello World application for Git demonstration.
This file demonstrates basic Python code in a Git repository.
"""

def greet(name="World"):
    """
    Greet someone by name.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main function to run the greeting program."""
    print(greet())
    print(greet("Git Demo"))
    print(greet("Spring 2022"))


if __name__ == "__main__":
    main()
