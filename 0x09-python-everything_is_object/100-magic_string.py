#!/usr/bin/python3
def magic_string(n):
    result = "BestSchool"
    for i in range(2, n + 1):
        result += ", " + "BestSchool" * i
    return result + "$"
