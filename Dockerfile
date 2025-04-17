FROM ubuntu

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Install timezone package (optional like your friend)
RUN apt-get install -y tzdata

# Set working directory
WORKDIR /app

# Copy all files to container
ADD . /app

# Install Python dependencies
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Expose the Flask default port
EXPOSE 5000

# Environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the Flask app
ENTRYPOINT ["flask", "run"]
