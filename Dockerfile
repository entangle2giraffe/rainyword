# Base image
FROM python:3.10.8-alpine3.16

# Copy Files
WORKDIR src/
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

CMD [ "python3", "app.py"]
