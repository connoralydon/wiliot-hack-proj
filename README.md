# wiliot-test


### project ideas

1. **command line to utilize qr code scanner to easily add new pixels to an account**
    - by extension also adding bridges
    - measuring employee performance
1. tool to measure employee learning rate and how fast they add tags, measuring time to becoming efficient at adding new tags to a network. it should help add tangible values to how much it costs to add tags to the platform

### plan

I'm going to tackle the first idea there. Good way to start accessing the api and make a easily usable application. If I have time I'll build this into a flask app for taking input and uploading it to the wiliot cloud. 

#### tasks

1. see how API works in general and what routes i need to use
1. build command line interface
   1. add fixed number of assets and PIXELS
   1. add asset each time we scan something
      1. do except for duplicate assets
2. build flask front end



### terms
app === connection

asset (virtual representation of physical objkect)
- sku === label
- pixels === tags


### steps to duplicate
1. `python -m venv env`
2. `source env/bin/activate`
3. `pip install requirements.txt`
4. Have qr scanner connected.
5. Have SKU labels and PIXEL labels ready, as well as termination QR code 
6. `python qr_app.py`

