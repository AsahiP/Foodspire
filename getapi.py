import requests

response = requests.get("https://www.kaggle.com/hugodarwood/epirecipes?select=full_format_recipes.json")


print (response["categories"])