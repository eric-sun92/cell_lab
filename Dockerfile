# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update package lists and upgrade vulnerable packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libcurl4 \
    libcurl3-gnutls \
    curl \
    openssh-client \
    libde265-0 && \
    rm -rf /var/lib/apt/lists/*


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 443 available to the world outside this container
EXPOSE 443

# port 80
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "streamlit/streamlit_app.py", "--server.port", "443", "--server.sslCertFile=server.crt", "--server.sslKeyFile=server.key"]
# CMD ["streamlit run streamlit/streamlit_app.py --server.port 443 --server.sslCertFile=.streamlit/certchain.pem --server.sslKeyFile=.streamlit/private.key"]