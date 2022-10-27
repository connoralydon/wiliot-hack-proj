# wiliot-hack


### files here

1. app.py 
   1. web app to bulk add items
2. qr_app.py
   1. command line tool to add tags with set number of tags



### building docs on traceability 
`pdoc env/lib/python3.9/site-packages/wiliot/cloud_apis/traceability/traceability.py`


### terminology
app === connection

asset (virtual representation of physical objkect)
- sku === label
- pixels === tags



### steps to deploy
*I am a socker novice, so this deployment may be buggy, ideally I want to have an environment to develop on, not just build*
This docker container runs the app.py (web app). I'm not totally sure how to get the command line program working.
1. have docker installed
2. `docker image build -t wiliot-hack .`
3. `docker run -p 80:80 --name wiliot-hack wiliot-hack`
4. `docker start wiliot-hack`
5. `docker stop wiliot-hack`

### steps to duplicate dev environment
1. python 3.9+
1. `python -m venv env`
2. `source env/bin/activate`
3. `pip install requirements.txt`
4. Have qr scanner connected.
5. Have SKU labels and PIXEL labels ready, as well as termination QR code 
6. `python qr_app.py` or `python app.py`
