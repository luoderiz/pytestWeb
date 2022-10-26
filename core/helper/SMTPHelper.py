from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib, ssl, time

"""
    File to handle email sending
    This file offers some methods to send emails using SMTP Protocol
    Also allows send the email with "From, To, Subject" headers format and allows parameterize
    the SMTP server.
"""
def sendEmail(data):
    """
        Method to send emails
        This method receives a dictionary as a parameter

        Dictionary format:
            server  -> Server mail name, e.g. 'gmail|office365'
            sender  -> Email address of sender
            receiver-> Email address of receiver
            msg     -> Message to send
            pass    -> Password of sender email account
            subject -> Subject of email
    """
    PORT = 587

    # Get data from parameter
    try:
        serverName = data['server']
        emailSender = data['sender']
        emailReceiver = data['receiver']
        message = data['msg']
        password = data['pass']
        subject = data['subject']
        attached = data.get('attached')
    except KeyError as ker:
        print("KeyError Exception:\n", ker.with_traceback)
        time.sleep(0.5)
        return None

    # Create message object instance
    msg = MIMEMultipart()

    # Setup the parameters of the message
    msg['From'] = emailSender
    msg['To'] = emailReceiver
    msg['Subject'] = subject

    # Add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # Add attached image to message body
    if (attached != None):
        file = open(attached, 'rb')
        msg.attach(MIMEImage(file.read()))

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Decode serverName
    serverName = __decodeServerName(serverName)

    # Try to log in to server and send email
    try:
        # Create server
        server = smtplib.SMTP(serverName, PORT)

        # Secure connection
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(emailSender, password)
        
        # Send the message via the server.
        server.sendmail(emailSender, emailReceiver, msg.as_string())
    except Exception as e:
        print("An Exception has occurred:\n", e)
        return None
    finally:
        server.quit()

    print("Successfully sent email to: %s" % (emailReceiver))
    return True


def __decodeServerName(serverName):
    """
        This method allows to abstract from the server address
        This method take valid parameters and returns his server address
        Valid paramateres: {'gmail'|'office365'}
    """
    if(serverName == "gmail"):
        return "smtp.gmail.com"
    elif(serverName == "office365"):
        return "smtp.office365.com"
    elif(serverName == "practia"):
        return "c1960497.ferozo.com"
    else:
        return None