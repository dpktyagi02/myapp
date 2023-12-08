# backend/Dockerfile
FROM python:latest

WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application files
COPY app.py ./
COPY frontend.html ./

CMD ["python", "app.py"]
