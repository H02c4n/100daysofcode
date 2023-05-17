from logo import logo, vs
from data import data
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}")


