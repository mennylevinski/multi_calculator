#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Menny Levinski
"""

import sys

# --- Utility Functions ---
def bin_to_decimal(binary_string: str) -> int:
    binary_string = binary_string.strip()
    negative = False
    if binary_string.startswith("-"):
        negative = True
        binary_string = binary_string[1:]
    if not all(c in "01" for c in binary_string):
        raise ValueError("Invalid binary number.")
    value = int(binary_string, 2)
    return -value if negative else value

def decimal_to_binary(num_str: str) -> str:
    if not num_str.lstrip("-").isdigit():
        raise ValueError("Input must be a decimal integer.")
    return bin(int(num_str))[2:]

def string_to_binary(text: str):
    return [format(ord(c), "08b") for c in text]

def letters_to_codes(text: str):
    if not text.isalpha():
        raise ValueError("Only alphabetic letters allowed.")
    return [ord(c) for c in text]

def codes_to_string(code_list: str):
    try:
        parts = code_list.split()
        chars = [chr(int(x)) for x in parts]
        return "".join(chars)
    except:
        raise ValueError("Enter numbers separated by spaces (e.g., '72 105').")

def bits_to_bytes(bits_str: str):
    if not bits_str.isdigit():
        raise ValueError("Bits must be numeric.")
    return int(bits_str) / 8

# --- Banner ---
def print_banner(title="Multi-Functional Calculator"):
    box_width = max(len(title) + 4, 40)
    print("\n" + "┌" + "─" * box_width + "┐")
    print("│" + title.center(box_width) + "│")
    print("└" + "─" * box_width + "┘\n")

# --- Helper for formatted messages ---
def print_error(msg):
    print("!!! ERROR: " + msg + " !!!")

def print_info(msg):
    print(">> " + msg)
    
# --- Main Menu ---
def main():
    print_banner()
    running = True

    while running:
        print("\n=== MENU ===")
        print("1. Binary → Decimal")
        print("2. Decimal → Binary")
        print("3. String → Binary")
        print("4. Letters (A-Z) → Numeric Codes")
        print("5. Numeric Codes (65–122) → String")
        print("6. Bits → Bytes")
        print("7. Exit\n")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            user = input("Enter binary: ")
            try:
                print_info("Decimal: " + str(bin_to_decimal(user)))
            except ValueError as e:
                print_error(str(e))

        elif choice == "2":
            num = input("Enter decimal: ")
            try:
                print_info("Binary: " + decimal_to_binary(num))
            except ValueError as e:
                print_error(str(e))

        elif choice == "3":
            text = input("Enter string: ")
            print_info("Binary: " + str(string_to_binary(text)))

        elif choice == "4":
            text = input("Enter letters only: ")
            try:
                print_info("Numeric codes: " + str(letters_to_codes(text)))
            except ValueError as e:
                print_error(str(e))

        elif choice == "5":
            nums = input("Enter codes separated by spaces: ")
            try:
                print_info("String: " + codes_to_string(nums))
            except ValueError as e:
                print_error(str(e))

        elif choice == "6":
            bits = input("Enter bits: ")
            try:
                print_info("Bytes: " + str(bits_to_bytes(bits)))
            except ValueError as e:
                print_error(str(e))

        elif choice == "7":
            print_info("Goodbye!")
            running = False

        else:
            print_error("Invalid choice, try again")

        if running:
            input("\nPress Enter to return to the menu...")

    sys.exit(0)

# --- Output ---
if __name__ == "__main__":
    main()
