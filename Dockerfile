# Use the official stable Python slim image
FROM python:3.13-slim  

# Set the working directory inside the container
WORKDIR /CRUD_Project

# Copy only requirements first to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
pip install --no-cache-dir gunicorn

# Copy the entire project into the container
COPY . .

# Expose the Django port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=CRUD_Project.settings

# Start Django application using Gunicorn
CMD ["gunicorn", "CRUD_Project.wsgi:application", "--bind", "0.0.0.0:8000"]
