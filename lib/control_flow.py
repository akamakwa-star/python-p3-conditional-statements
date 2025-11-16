#!/usr/bin/env python3

def admin_login(username, password):
    # grant access when username is "admin" (case-insensitive) and password is "12345"
    if isinstance(username, str) and username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    # return different messages depending on the temperature
    if temperature < 40:
        return "It's brisk out there!"
    if temperature < 65:
        return "It's a little chilly out there!"
    if 65 <= temperature <= 85:
        return "It's perfect out there!"
    return "It's too dang hot out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    print("Invalid operation!")
    return None
