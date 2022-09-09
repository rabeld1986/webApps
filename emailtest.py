from email.message import EmailMessage

def Create_Email():

    #set up the parameters that will compose the email
    subject = "Analyzed Data Alert"
    sender = ""
    reciever = ""
    
    #create the Email object
    msg = EmailMessage()
    
    #configure Email Headers
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever

    msg.set_content("""\
            <html>
              <body>
                <p><b>Python Mail Test</b>
                <br>
                   These are the results of the Threshold & Database comparison.<br>
                   

                </p>
              </body>
            </html>
            """
     )

    return msg
