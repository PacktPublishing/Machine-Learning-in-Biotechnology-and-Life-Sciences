# Set base image (host OS)
FROM python:3.8

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
COPY models/ch10_scaler.pickle /models/ch10_scaler.pickle
COPY models/ch10_scaler.pickle /models/ch10_rfc_clf.pickle
COPY styles /app/styles
COPY models /app/models
COPY templates /app/templates

ENV IN_DOCKER_CONTAINER Yes

# Check Pip Version
RUN echo pip --version

# Upgrade pip
RUN pip install --upgrade pip

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
# CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
