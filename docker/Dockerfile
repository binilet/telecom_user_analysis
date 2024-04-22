# use the official python image from docker hub
FROM python:3.11.7

#set working directory inside the container
WORKDIR /telecom_user_analysis

#copy the contents of this current directory in to the container

COPY . /telecom_user_analysis

#install dependancies specified in req.txt
RUN pip install --no-cache-dir -r requirements.txt

#command to run the application; in our case the streamlit app
CMD [ "streamlit", "run", "app/app.py" ]