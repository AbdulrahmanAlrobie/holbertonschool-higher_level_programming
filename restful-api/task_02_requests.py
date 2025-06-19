#!/usr/bin/env python3
"""Module for fetching and processing posts from an API using requests."""

import csv
import requests


API_URL = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Fetch all posts and print HTTP status and each post title."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for post in response.json():
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetch all posts, structure data, and save to posts.csv."""
    response = requests.get(API_URL)
    if response.status_code != 200:
        return False

    posts = response.json()
    rows = [
        {'id': p.get('id'), 'title': p.get('title'), 'body': p.get('body')}
        for p in posts
    ]

    fieldnames = ['id', 'title', 'body']
    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return True
