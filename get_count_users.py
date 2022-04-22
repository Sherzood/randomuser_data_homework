import json
import re

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    a=data['results']
    c=0
    for i in a:
        c+=1
        print(c)
    
    return 
    
    
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_count_users(data))