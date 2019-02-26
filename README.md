# CodeChallenge

This project requires Python2.7+ , PHP and MySQL. The API is in python, UI is Web and database is MySQL

Tested on linux ( Ubuntu ) machine

## Dependencies

mysql-config is in a different package, which can be installed from (again, assuming debian / ubuntu):

``` sudo apt-get install libmysqlclient-dev ```


### Sample Command Curl
``` curl -F 'csv_file=@/home/kim/Desktop/interviews/tulaa/sample_csv.csv' http://localhost:8086/upload ```

### Sample Response
``` {"status": "200", "message": "Uploaded"} ```


### App is Web Based

Install MySQL and import the database on the database folder
Install Apache
Install php 7.0+
Python should be there by default on Linux

### Enable mod proxy on apache

sudo a2enmod proxy proxy_http proxy_balancer lbmethod_byrequests 

### Setup  a proxy pass on apache sites available 
ProxyPass /uploader http://localhost:8086/upload                                                           
ProxyPassReverse /uploader http://localhost:8086/upload

systemctl restart apache2 


### Install Web Folder

``` cp -r csv_app /var/www/html ```

Open your browser and visit, http://localhost/csv_app

### Run the API service
Ensure dependencies are installed, you can run setup.sh, using command ./setup.sh
If installed successfully run run_service.sh using command ./rus_service.sh ( as root )

### Logs
Available logs should be under /var/log/tulaa/*.log
