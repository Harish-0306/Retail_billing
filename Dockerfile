FROM ubuntu

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    tzdata

# Set working directory
WORKDIR /app

# Copy your application code
ADD . /app

# Set up virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app
CMD ["/bin/bash", "-c", ". venv/bin/activate && flask run"]
