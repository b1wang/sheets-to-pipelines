# Base image
FROM python:3.11-slim

WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY app.py .

EXPOSE 8501


CMD ["streamlit", "run", "app.py", "--server.runOnSave", "true", "--server.fileWatcherType", "poll", "--server.port=8501", "--server.address=0.0.0.0"]