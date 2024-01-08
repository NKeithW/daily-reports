# Daily Reports
This is a basic script in python to send email reports as an automated task. 

# Before running the script, make sure to allow access to your Google account by enabling "Less secure app access." You can do this by going to your Google Account settings, then Security, and turn on "Less secure app access." Please be aware that this may pose a security risk, and it's recommended to use an application-specific password or OAuth for a more secure approach.

## Replace placeholder values:
Replace "your_email@email.com", "recipient_email@example.com", and "your_email_password" with your Gmail email, recipient email, and Gmail password.

## Required Libraries
--
  pip install schedule
--


## The script will run indefinitely, checking for scheduled tasks every second. 
It will send the daily email report at the specified time. Remember to keep your email and password secure. Avoid hardcoding sensitive information directly in your script, especially if you plan to share or publish the code. Consider using environment variables or configuration files for better security practices.
