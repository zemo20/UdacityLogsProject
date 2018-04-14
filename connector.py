#!/usr/bin/env python3

import datetime
import psycopg2

DB_NAME = 'news'


def print_all():

    print("articles:")
    print_articles()
    print("\n\n")
    print('authors:')
    print_authors()
    print("\n\n")
    print("errors :")
    print_errors()


def print_articles():
    """prints the 3 most viewed articles"""
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select articles.lead , count(log) as views from articles,log "
              "where log.path like concat('%',articles.slug,'%') group by "
              "articles.lead order by views desc limit 3 ;")
    articles = c.fetchall()
    for article in articles:
        print(" \"%s\" -- %s Views" % (article[0], article[1]))
    db.close()


def print_authors():
    """prints the authors sorted by the most popular"""
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select authors.name, sum(articles.views) from"
              "(select articles.author, count(log) as views "
              "from articles,log where log.path like concat"
              "('%',articles.slug,'%') group by articles.author ) as articles"
              ", authors where articles.author = authors.id group by "
              "authors.name order by sum desc ;")
    authors = c.fetchall()
    for author in authors:
        print(" \"%s\" -- %s Views" % (author[0], author[1]))
    db.close()


def print_errors():
    """prints days with most errors"""
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute("select day, perc from (select day, round((sum(requests)/"
              "(select count(*) from log where substring(cast(log.time as"
              " text), 0, 11) = day) * 100), 2) as perc from (select "
              "substring(cast(log.time as text), 0, 11) as "
              "day, count(*) as requests "
              "from log where status = '404 NOT FOUND' group by day ) as"
              " log_percentage "
              "group by day order by perc desc) as final_query "
              "where perc >= 1 ;")
    errors = c.fetchall()
    for error in errors:
        print(" \"%s\" -- %s%s" % (error[0], error[1], '%'))
    db.close()


print_all()
