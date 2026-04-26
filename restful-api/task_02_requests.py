#!/usr/bin/python3
"""Requests tasks"""

import requests
import csv


def fetch_and_print_posts():
    """fetchs and prints the posts"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {stc}".format(stc=r.status_code))
    if r.status_code == 200:
        datas = r.json()
        for data in datas:
            print(data['title'])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    list_of_datas = []
    if r.status_code == 200:
        datas = r.json()
        for data in datas:
            list_of_datas.append({"id":data['id'], "title":data['title'], "body":data['body']})
    with open("posts.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(list_of_datas)
