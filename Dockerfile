# Use the official Python slim image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /CRUD_Project  

# Copy only requirements first to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application inside the container
COPY . .

# Expose the Django port
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=CRUD_Project.settings
ENV PYTHONUNBUFFERED=1

# Run migrations and collect static files
RUN python manage.py migrate && python manage.py collectstatic --noinput

# Start Django application using Gunicorn
CMD ["gunicorn", "CRUD_Project.wsgi:application", "--bind", "0.0.0.0:8000"]
