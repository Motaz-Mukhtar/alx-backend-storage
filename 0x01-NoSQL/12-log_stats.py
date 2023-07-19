#!/usr/bin/env python3
"""
    Provides some stats about Nginx logs stored in MogoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_document()} logs")
    print(f"""
    Methods:
        method GET: {nginx_collection.count_document({'method': 'GET'})}
        method POST: {nginx_collection.count_document({'method': 'POST'})}
        method PUT: {nginx_collection.count_document({'method': 'PUT'})}
        method PATCH: {nginx_collection.count_document({'method': 'PATCH'})}
        method DELETE: {nginx_collection.count_document({'method': 'DELETE'})}
    {nginx_collection.count_document({'path': '/status'})} status check
    """)
