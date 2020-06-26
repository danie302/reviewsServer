# Server for the reviews page

Documentation of the server for the reviews REST API in Django

> To run the project you have to install docker-compose and python 3.7

### Steps to start the server

1. Clone the repo
2. Open the folder conf and in the file `config_file.json` replace the database host with your private IP
3. Open the terminal in the project folder
4. run --> `docker-compose up --build -d`

### Steps to develop the API

1. Download and run postgresql docker image
2. Create virtual environment for the django project
3. Activate the virtual environment and copy the trial project
4. Install pip dependencies
5. Write the models and make the migrations
6. Write the serializers
7. Write the views
8. Write the url for the endpoints
9. Write the tests with pytest
10. Upload the data to the database with django admin page
11. Test the main endpoint with Postman
12. Write the dockerfile to the build the API image
13. Write the docker-compose to start postgres and the API

## Contributors

- Daniel Daza <danydaza9@gmail.com>
