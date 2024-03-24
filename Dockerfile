# Load python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container  
COPY requirements.txt .

# Install app dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY minilink/ .

# Make port 8000 available for links and publishing
EXPOSE 8000 

# Run the command to start the app
CMD ["python", "manage.py", "runserver"]
