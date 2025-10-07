#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


class Person:
    def __init__(self, name="", job=""):
        # Always define attributes
        self.name = name
        self.job = job

        # Validate job first if provided
        if job and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return

        # Validate name
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return

        # Convert valid name to title case
        self.name = name.title()
