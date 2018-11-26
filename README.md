# FSND Log Analysis Project


## Introduction

To build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The project requires students to create and use SQL queries that would fetch results from a large database of a news website.The objective of this project is to extend the student's SQL database skills. The code requirements suggest the use of only one single query to answer each request.


### What to report?

* What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

* Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

* On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.


### PreRequisites

* [Python](https://www.python.org/downloads/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)


### Database and Configuration file 

* Download the database used [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* You will need to unzip the database file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
* Download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.
* Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory


## Launching the Virtual Machine:

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
```
$ vagrant up
```

2. Log in
```
$ vagrant ssh
```

3. Change directory to /vagrant
```
vagrant@vagrant:~$ cd /vagrant
```

4. Load the data in local database
```
psql -d news -f newsdata.sql
```
5. Connect to the database 
```
psql -d news
```

6. Run the python file
```
python loganalysis.py
```


## Expected output 

--Log Analysis Report--

1.What are the most popular three articles of all time?

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views

2.Who are the most popular article authors of all time?

"Ursula La Multa" -- 507594 views
"Rudolf von Treppenwitz" -- 423457 views
"Anonymous Contributor" -- 170098 views
"Markoff Chaney" -- 84557 views

3.On which days did more than 1% of requests lead to errors?

July 17, 2016 -- 2.3% errors

-END-

#### Note-Now views were created for the project. 