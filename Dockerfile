# Uses Python 3.9 base image
FROM python:3.9     
# Exposes port 5000 (for Flask app)
EXPOSE 5000              
# Sets the working directory to /app
WORKDIR /app                                       
# Copies requirements.txt to the container
COPY ./requirements.txt requirements.txt             
# Installs dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt  
# Copies all your application files to /app in the container
COPY . .                      
# Runs the Flask app using the "flask run" command on 0.0.0.0
CMD ["flask", "run", "--host", "0.0.0.0"]  