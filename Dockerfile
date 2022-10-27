FROM python:3.9.12 
# start by pulling the python image

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "bash" ]

CMD ["app.py" ]

# docker image build -t wiliot-hack .

# docker run -p 80:80 --name wiliot-hack wiliot-hack

# docker start wiliot-hack

# docker stop wiliot-hack