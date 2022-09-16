# Package application into container img

# inherit from pre-existing image
FROM python:3.5

# copy files in working directory into a directory called app, inside image
COPY . /app

# specifies working directory for instructions files and where the application will run
WORKDIR /app

# run pip and have it install the required libraries listed in txt file 
RUN pip install -r requirements.txt

# tell docker what commands should be running when container img is started
CMD ["python", "-u", "server.py"]