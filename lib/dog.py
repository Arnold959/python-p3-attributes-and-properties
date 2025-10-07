#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        # Always define attributes first to avoid AttributeError
        self.name = name
        self.breed = breed

        # Check if breed is provided and valid
        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return

        # Check name validity only if name is provided (not None)
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
