# qr_app.py

from wiliot.cloud_apis.management.management import *
from wiliot.cloud_apis.traceability.traceability import *

# json.loads(json_data) -> dict
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")

wiliot = ManagementClient(os.environ.get('USER_NAME'),
                          os.environ.get('USER_PASSWORD'),
                          os.environ.get('OWNER_ID'))

# for adding assets etc
trace = TraceabilityClient(os.environ.get('USER_NAME'),
                          os.environ.get('USER_PASSWORD'),
                          os.environ.get('OWNER_ID'))

def collect_asset_data_qr(termination_char: str = "done",
                          max_tag_count: int = 2):

    # asset data to add
    asset_data_to_upload = []
    tag_count = 2
    # do while
    label = input("SCAN SKU").strip()
    while label != "done":
        # doing work in here to add assets to the server
        tags = set()
        for i in range(tag_count):
            tag = input("SCAN TAG").strip() # do while
            tags.add(tag)
        
        
        label = input("SCAN SKU").strip()
        
        asset_data_to_upload.append((label, tags))

    return asset_data_to_upload
    # batch adding tag data 
    
def upload_data(data: list):
    for label, tags in data:
        tags = list(tags)
        trace.create_asset(name=label,
                           asset_id=label,
                           tag_ids=tags,
                           poi_id="f0c734a3-a860-4de6-b007-b48e8587d60c")

data = collect_asset_data_qr()

upload_data(data)

print("done")
