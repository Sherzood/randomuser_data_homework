import get_data
import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    l=[]
    a=data['results']
    for i in a:
        l.append(i['email'])
   

    return l
f=open('randomuser_data.json').read()
data=json.loads(f)
print(get_email(data))