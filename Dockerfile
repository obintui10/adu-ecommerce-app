FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Add non-root user for security
RUN useradd -m appuser
USER appuser

# Expose port
EXPOSE 80

# Use Gunicorn for production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]
