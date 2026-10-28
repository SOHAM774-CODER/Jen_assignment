FROM python:3.11-slim
WORKDIR /app
COPY build_task.py .
CMD ["python", "build_task.py"]
