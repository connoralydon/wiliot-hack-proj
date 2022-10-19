import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")

from wiliot.cloud_apis.management.management import *
from wiliot.cloud_apis.traceability.traceability import *


wiliot = ManagementClient(os.environ.get('USER_NAME'),
                          os.environ.get('USER_PASSWORD'),
                          os.environ.get('OWNER_ID'))

# for adding assets etc
trace = TraceabilityClient(os.environ.get('USER_NAME'),
                          os.environ.get('USER_PASSWORD'),
                          os.environ.get('OWNER_ID'))

def delete_all_assets():
    
    asset_data_raw = trace.get_assets()
    
    asset_ids = [a["id"] for a in asset_data_raw]
    
    for aid in asset_ids:
        trace.delete_asset(aid)
        