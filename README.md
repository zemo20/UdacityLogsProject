# UdacityLogsProject

A Tutorial project for udacity fullstack course, the mission is to find to write 3 queries that find the most popular articles, and the
most popular authors, and finding the day that has the most failures in requests.


#How to run

1-clone the repository by running the command : git clone https://github.com/zemo20/UdacityLogsProject.git


2-extract the newsdata.zip file to the same directory


3-Install virtualbox to your computer


4-open a terminal at the cloned project location and run this command to install the ubuntu vm : vagrant up


5-run this command to login to your machine : vagrant ssh


6-run these commands to access the vagrant folder which is shared between your computer and your vm

-cd ..

-cd ..

-cd vagrant


7-Run this command to seed the database : psql -d news -f newsdata.sql


8-install pyscopg2 package By running these commands :


-sudo apt-get update


-sudo apt-get install libpq-dev python-dev


-sudo pip install psycopg2


9-run this command to get the final results of the queries: python connector.py
