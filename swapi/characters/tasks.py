import os
import json
import math
import datetime
from typing import List, Dict
import petl
import requests
from django.conf import settings

from .models import CSVFile


def fetch_and_download_data_from_api():
    """
    Fetch and download starwars data from swapi
    """
    response = get_page()

    response = formatted_response(response)

    download_dir = settings.BASE_DIR / settings.CSV_ROOT_PATH
    if not os.path.isdir(download_dir):
        os.makedirs(download_dir)

    now = datetime.datetime.now()
    file_name = now.strftime('%b %d %Y, %H:%M:%S.csv')
    full_path = download_dir / file_name
    
    csv_header = response[0].keys()
    csv_table = [csv_header]

    for row in response:
        csv_row = [row[row_name] for row_name in csv_header]
        csv_table.append(csv_row)
    petl.tocsv(csv_table, full_path)
    csv_file = CSVFile(file_name=file_name, download_date=now, last_edited=now)
    csv_file.save()

    return response


def formatted_response(response: List[Dict]) -> List[Dict]:
    """
    Resolve the homeworld field into the homeworld's name
    """
    homeworld = {}
    formatted = []
    for elem in response:
        homeworld_url = elem["homeworld"]
        if homeworld_url not in homeworld:
            response = make_request(homeworld_url)
            homeworld[homeworld_url] = response["name"]
        elem["homeworld"] = homeworld.get(homeworld_url)
        formatted.append(elem)

    return formatted


def make_request(url: str) -> Dict:
    """
    Call api endpoint url and return a response.
    """
    r = requests.get(url)
    response_json = json.loads(r.content)

    return response_json


def get_page() -> List[Dict]:
    """
    Gets the raw results from the API.
    Combines multiple requests' responses into one dict().
    """
    SWAPI_URL = "https://swapi.dev/api/people"
    response_json = make_request(SWAPI_URL)

    next_url = response_json["next"]
    page_size = len(response_json["results"])
    count = response_json["count"]

    pending_requests_count = math.ceil(count / page_size) - 1

    base_next_url, next_url_index = next_url.split("=")
    pending_urls = (f"{base_next_url}={int(next_url_index) + offset}" for offset in range(pending_requests_count))

    responses = []
    responses.extend(response_json["results"])
    for url in pending_urls:
        response = make_request(url)
        results = response["results"]
        print(f"Get next {len(results)} values")
        responses.extend(results)
    return responses