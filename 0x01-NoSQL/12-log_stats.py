#!/usr/bin/env python3
"""
    Provides some stats about Nginx logs stored in MogoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    result = nginx_collection.find()
    doc_list = [doc for i in result]

    print(f"{len(doc_list)} logs")
    print(f"""
    Methods:
        method GET: {nginx_collection.count_documents({'method': 'GET'})}
        method POST: {nginx_collection.count_documents({'method': 'POST'})}
        method PUT: {nginx_collection.count_documents({'method': 'PUT'})}
        method PATCH: {nginx_collection.count_documents({'method': 'PATCH'})}
        method DELETE: {nginx_collection.count_documents({'method': 'DELETE'})}
    {nginx_collection.count_documents({'path': '/status'})} status check
    """)
    client.close()
