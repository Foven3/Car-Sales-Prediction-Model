# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py", "--server.port", "7860", "--server.name", "0.0.0.0"]
