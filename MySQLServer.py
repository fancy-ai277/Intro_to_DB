#!/usr/bin/python3
"""
A script that creates a MySQL database 'alx_book_store'
"""

import MySQLdb
from MySQLdb import Error

def create_database():
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",      # or your host (e.g., "127.0.0.1")
            user="root",           # replace with your MySQL username
            passwd="your_password" # replace with your MySQL password
        )

        cursor = db.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    create_database()
