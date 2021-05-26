import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "Your Gmail | Other Email Address"
password = "Your Gmail Password"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be comitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be comitted
    server.login(sender_email, password)
    # TODO: Send email here
    # print message for showing you are successfully login
    print("Successfully login") 
    # Create Subject what ever you want
    subject="Sending email using python"
    # Create Body message what ever you want or write
    body="This is 2nd mail from python sended by Raheel"
    # Finally combine body & subject using string formating
    message="Subject: {}\n\n{}".format(subject,body)
    # Create List for user mail ID's
    address=['mraheel.naseem@gmail.com','mrahilnasim@gmail.com']
    # Then combine all the message & mail ID's just for sending
    server.sendmail("johnmalton734",address,message) # it's take 3 argument (1.)sender mail id, 2.)receiver id's, 3.)message)
    # Simply show message for successfully send
    print('Mail send successfully')
except Exception:
    # Print any error messages
    # Showing error if password is wrong
    print("Login Failed")
    print("Try to enter correct password")
finally:
    # for completly close SMTP server
    print('Server Has Been Successfully Close')
    server.quit() 
