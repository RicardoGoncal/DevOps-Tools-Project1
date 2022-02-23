# Image base in Python 3.8.2
FROM python:3.8.2

# Create dir code
WORKDIR /code

# Copy folders to base path
COPY ./env /code/env
COPY ./src /code/src

# Copy file to base path
COPY __main__.py /code/__main__.py
COPY requirements.txt /code/requirements.txt

# Install Requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Port 5001
EXPOSE 5001

# Run code
CMD ["python","."]