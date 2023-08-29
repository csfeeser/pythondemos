# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the local code to the container
COPY api.py .

# Install Flask library
RUN pip install flask

# Make the /data directory inside the container to store the SQLite3 database
RUN mkdir /data

# Run app.py when the container launches
CMD ["python", "api.py"]
