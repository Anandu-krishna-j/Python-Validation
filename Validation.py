import re

email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

phone = r'([0-9]{11}$)|(^[7-9][0-9]{9}$)'

def Validate(patternOfData,stringData):
    if(patternOfData=='email'):
        if(re.fullmatch(email, stringData)):
            return "success"
        return "failure"
    elif patternOfData=='phone':
        if re.fullmatch(phone,stringData):
            return "success"
        return "failure"


print(Validate('email','anandhugmail.com'))