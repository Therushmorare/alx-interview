#!/usr/bin/python3
"""
Write a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ validate utf8 """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
