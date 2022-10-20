# app.py

from wiliot_helpers import delete_all_assets
delete_all_assets()

# home for the flask app

from flask import (Flask, 
                   render_template,
                   url_for,
                   request,
                   redirect)


from datetime import datetime

from wiliot.cloud_apis.traceability.traceability import *

import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
USER_NAME = os.getenv("USER_NAME")
USER_PASSWORD = os.getenv("USER_PASSWORD")

app = Flask(__name__)

trace = TraceabilityClient(os.environ.get('USER_NAME'),
                          os.environ.get('USER_PASSWORD'),
                          os.environ.get('OWNER_ID'))


# sku_item
class SkuAssets: # to access db
    sku: str =  None 
    item_name: str = None
    date_modified: datetime = None
    asset_id_stack: list = []
    asset_len = None
    
    def __init__(self, sku: str = "a", item_name: str = 'a') -> None:
        self.sku = sku
        self.item_name = item_name
        self.date_modified = datetime.utcnow()
        self.asset_len = 0
    
    def add_asset(self, name, asset_id, tags: list):
        self.date_modified = datetime.utcnow() # update time
        self.asset_id_stack.append(asset_id)
        # add with trace
        trace.create_asset(name=name, asset_id=asset_id, tag_ids=tags)
        self.asset_len += 1
        
        
    def pop_asset(self):
        if self.asset_id_stack:
            self.update_time()
            popped_asset_id = self.asset_id_stack.pop() # remove most recently added 
            trace.delete_asset(popped_asset_id)
            # removing from wiliot
            self.asset_len -= 1
            
        else:
            print("asset id stack empty")
        
        
    def update_time(self):
        self.date_modified = datetime.utcnow()
        
    def is_empty(self) -> bool:
        return (True if not self.asset_id_stack else False)

    def get_count(self) -> int:
        return self.asset_len
        
    # def remove_asset(self, asset_id):
    #     self.update_time()
    #     try:
    #         self.asset_id_stack.remove(asset_id)
    #     except ValueError:
    #         print("asset id doesn't exist in list")

    def __repr__(self):
        return '<SKU %r>' %  self.sku


num_tags_per_asset = 2
# assets: dict[str,SkuAssets] =  {'a': SkuAssets()} # list of 
# SkuAssets objects
# sku, skuassets object
assets: dict[str,SkuAssets] =  {} # this keeps resetting the 

@app.route("/", methods = ["POST","GET"])
def index():
    global assets
    asset_vals = assets.values()
    
    
    return render_template("index.html", 
                           rendered_assets = asset_vals,
                           num_tags = num_tags_per_asset) 

@app.route("/update_tag_count/", methods=["POST"])
def update_tag_count():
    global num_tags_per_asset
    
    num_tags_per_asset = request.form['tag_count']
    return redirect("/")
    


@app.route("/decriment/<string:sku>")
def decriment_sku(sku):
    global assets
    
    assets[sku].pop_asset()
    
    # try integrating this intop the object
    if assets[sku].get_count() <= 0:
        del assets[sku]
    
    return redirect("/")

@app.route("/incriment/", methods=["GET","POST"])
def incriment():
    if request.method == "POST":
        global assets
        
        sku_to_add = request.form['sku'].strip() # idk how to grab multiple items
        tags_to_add = request.form['tags'].split()
        
        if sku_to_add not in assets.keys():
            assets[sku_to_add] = SkuAssets(sku_to_add,sku_to_add)
        
        # see if any new tags are in the old tags
        # if tags_to_add in assets[sku_to_add].asset_id_stack:
        #     print("duplicate asset_id")
        # else:
        assets[sku_to_add].add_asset(sku_to_add, hash(tags_to_add[0]), tags_to_add)
        
        return redirect("/")
    else:
        return 'incriment'


# change this for real deployment
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)