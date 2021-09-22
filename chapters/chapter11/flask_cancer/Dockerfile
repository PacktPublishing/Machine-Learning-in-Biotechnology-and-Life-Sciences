# Set base image (host OS)
FROM python:3.8

# By default, listen on port 5000
EXPOSE 5000/tcp
# EXPOSE 80
# EXPOSE 5000

# Set the working directory in the container
WORKDIR /app

# RUN ls

# Copy the dependencies file to the working directory
COPY requirements.txt .
COPY models/ch10_scaler.pickle /models/ch10_scaler.pickle
COPY models/ch10_scaler.pickle /models/ch10_rfc_clf.pickle

COPY styles /app/styles
COPY models /app/models
COPY templates /app/templates
COPY templates/index.html .
COPY templates/index.html /templates
COPY templates/index.html app/templates

COPY app.py /app
COPY requirements.txt /app

ENV IN_DOCKER_CONTAINER Yes

# Upgrade Cython
# RUN pip install --upgrade cython

# Check Pip Version
RUN echo pip --version

# Upgrade pip
RUN pip install --upgrade pip

# Install any dependencies
RUN pip3 install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

RUN ls

# Specify the command to run on container start
CMD [ "python", "./app.py" ]
# CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app"]
