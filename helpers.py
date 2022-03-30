import re

def validate_uprn(value):
  result = re.search("^\d{1,12}$", value)
  return not result == None
