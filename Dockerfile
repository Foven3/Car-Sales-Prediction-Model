# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
