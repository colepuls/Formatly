FROM python:3.11-slim

# Install system dependencies including ImageMagick
RUN apt-get update && apt-get install -y \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads outputs

# Expose port
EXPOSE 8000

# Set environment variables
ENV PORT=8000

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"] 