import requests
import certifi
from bs4 import BeautifulSoup

def extract_fields_from_url(url):
    response = requests.get(url, verify=certifi.where())

    soup = BeautifulSoup(response.text, "html.parser")
    inputs = soup.find_all("input")

    fields = []

    for inp in inputs:
        name = inp.get("name")
        field_type = inp.get("type")

        if name:
            fields.append({
                "name": name,
                "type": field_type
            })

    return fields