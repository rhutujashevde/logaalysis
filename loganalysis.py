#!/usr/bin/env python

import psycopg2

# assign database name to DBNAME
DBNAME = "news"


# get three most popular articles of all time
def articles_query():
    # connect to the database
    db = psycopg2.connect('dbname=' + DBNAME)
    # create a cursor
    c = db.cursor()
    # assign sql query to variable called 'query'
    query = """select title, views from\n
    (select substr(path, 10), count(*) as views from log\n
    where path != '/' group by path ) as log_query,
    articles where slug = substr order by views desc limit 3;"""
    # execute the query
    c.execute(query)
    # fetch the results from cursor
    articles = c.fetchall()
    # close the database
    db.close()

    print('1.What are the most popular three articles of all time?\n')
    # create a for..in loop to print the fetched values
    for article in articles:
        print('"'+article[0] + '" -- ' + str(article[1]) + " views")


# get three most authors of all time
def authors_query():
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    query = """select name, sum(views) as author_views from
    (select name, slug, views from\n
    (select substr(path, 10), count(*) as views from log\n
    where path !='/' group by path) as log_query,\n
    articles, authors\n
    where authors.id = articles.author and substr = articles.slug\n
    order by views desc) as views_query\n
    group by name order by author_views desc;"""
    c.execute(query)
    authors = c.fetchall()
    db.close()

    print('\n2.Who are the most popular article authors of all time?\n')
    for author in authors:
        print('"'+author[0] + '" -- ' + str(author[1]) + " views")


# get the days on which more than 1% error occurred
def logs_query():
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    query = """select total_requests.day,\n
    round(((total_errors.errors*1.0) / total_requests.requests), 3)\n
    as percent from\n
    (select date_trunc('day', time) as date, count(*) as errors from log\n
    where status = '404 NOT FOUND' group by date) as total_errors\n
    join ( select date_trunc('day', time) as day, count(*) as requests\n
    from log group by day) as total_requests\n
    on total_requests.day = total_errors.date\n
    where\n
    (round(((total_errors.errors*1.0) / total_requests.requests), 3) > 0.01)\n
    order by percent desc;"""
    c.execute(query)
    logs = c.fetchall()
    db.close()

    print('\n3.On which days did more than 1% of requests lead to errors?\n')
    for log in logs:
        percent = str(round(log[1]*100, 1))
        print(log[0].strftime('%B %d, %Y') + " -- " + percent + "% errors")


print('\n--Log Analysis Report--\n')
articles_query()
authors_query()
logs_query()
print('\n-END-\n')
