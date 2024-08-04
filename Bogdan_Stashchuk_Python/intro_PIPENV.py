# pipenv install requests
import requests
import pandas
my_request = requests.get('https://www.python.org')
print(my_request)
print(my_request.text)
print(my_request.status_code)
# pipenv graph
# change in setting in VS Code runner
#   "python": "python -u",
#   "python": "python/.venv/bin/python -u",
# "python": "D:/python/.venv/Scripts/python.exe -u",
