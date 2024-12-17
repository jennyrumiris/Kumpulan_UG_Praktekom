import sqlite3 
from flask import Flask, redirect, request, url_for, render_template_string

app = Flask(__name__) 

@app.route("/login", methods=['POST'])   
def login(): 
    # Get username and password from form
    username = request.form['username']
    password = request.form['password']
    
    # Check login credentials
    user = userLogin(username, password)
    
    if user:
        # Successful login
        return render_template_string("""
            <h1>Welcome back {{ username }}!</h1>
            <a href="javascript:history.back()">Back to Login</a>
        """, username=username)
    else:
        # Failed login
        return render_template_string("""
            <h1>Login Failed! Please check your username & password!</h1>
            <a href="javascript:history.back()">Try Again</a>
        """)
 
def userLogin(username, password): 
    # Open database connection 
    connection = sqlite3.connect("user.db") 
    cursor = connection.cursor() 
    
    # Execute the query 
    cursor.execute("SELECT username, password FROM user WHERE username = ? AND password = ?;",  
                   (username, password))     
    count = cursor.fetchone() 
    
    # Close the connection 
    connection.close() 
    return count 

# Initialize the database before running the app
def init_db():
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    
    # Insert predefined users
    users = [
        ('Admin', 'qwe123'),
        ('Ivan', 'r0ku83'),
        ('Kenzie', 'foca')
    ]
    
    # Insert users if they don't exist
    for username, password in users:
        cursor.execute("INSERT OR IGNORE INTO user (username, password) VALUES (?, ?)", 
                       (username, password))
    
    connection.commit()
    connection.close()

if __name__ == '__main__': 
    # Initialize the database
    init_db()
    
    print("This is flask Program!") 
    app.run(debug=True)