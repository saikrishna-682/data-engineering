# Use an official Python runtime as a parent image
FROM

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run your Flask application
CMD ["python", "postgresflask.py"]

# command to run to build a docker image  :::::::::   docker build -t flask-postgres-app .
# Tag the image                           :::::::::   docker tag your-image-name your-repository/your-image-name
# Login to Docker Hub (or your registry)  :::::::::   docker login -u your-username -p your-password your-repository
# Push the image to the repository        :::::::::   docker push your-repository/your-image-name

