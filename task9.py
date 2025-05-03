import datetime

def log_login_attempt(username, success):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Determine whether the login was successful or failed
    status = "Success" if success else "Failure"
    
    # Create a log message
    log_message = f"{timestamp} - Username: {username} - Login {status}\n"
    
    # Append the log message to the log file
    with open("login_attempts.log", "a") as log_file:
        log_file.write(log_message)

# Example usage:
log_login_attempt("user1", True)  # Successful login attempt
log_login_attempt("user2", False)  # Failed login attempt
