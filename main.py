# Date and time
from datetime import date
from datetime import timedelta
import json_extract, text_parser, os

# Get the current date
today = date.today()
print("Today is:", today)

# If Class JSON folder does not exist, create it
if not os.path.exists('Class JSON'):
    os.makedirs('Class JSON')

# If Class Recording folder does not exist, create it
if not os.path.exists('Class Recording'):
    os.makedirs('Class Recording')

"""
    Yesterday's date = 1
    2 days ago = 2
    3 days ago = 3
    ...
    30 days ago = 30
"""

# How many days ago?
days_ago = int(input("-> How many days ago? "))
json_extract.extract_json(days_ago)
text_parser.relocate()