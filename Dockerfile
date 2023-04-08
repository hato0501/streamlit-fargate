# Set the base image to Python 3.9
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the app files to the container
COPY /app .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run the command to start the app when the container starts up
CMD ["streamlit", "run", "app.py"]