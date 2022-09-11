from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def Create_Email(data):
    # set up the parameters that will compose the email
    subject = "Analyzed Data Alert"
    sender = "dominicandaddy_nyc@hotmail.com"
    receiver = "rabeldelcastillo23@gmail.com"

    # create the Email object
    msg = MIMEMultipart('alternative')

    # configure Email Headers
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    html = """\
    
        
        <body style="background-color:grey">
            <table align="center" border="0" cellpadding="0" cellspacing="0"
                width="550" bgcolor="white" style="border:2px solid black">
                <tbody>
                    <tr>
                        <td align="center">
                            <table align="center" border="0" cellpadding="0"
                                cellspacing="0" class="col-550" width="550">
                                <tbody>
                                    <tr>
                                        <td align="center" style="background-color: red;
                                                height: 50px;">
        
                                            <a href="#" style="text-decoration: none;">
                                                <p style="color:white;
                                                        font-weight:bold;">
                                                    Email Alert
                                                </p>
                                            </a>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                    <tr style="height: 300px;">
                        <td align="center" style="border: none;
                                border-bottom: 2px solid #4cb96b;
                                padding-right: 20px;padding-left:20px">
        
                            <p style="font-weight: bolder;font-size: 15px;
                                    letter-spacing: 0.025em;
                                    color:black;">
                                Hi
                                <br> This is the comparison between the KCNG database and the Threshold data
                            </p>
                        </td>
                    </tr>
        
                    <tr style="display: inline-block;">
                        <td style="height: 150px;
                                padding: 20px;
                                border: none;
                                border-bottom: 2px solid #361B0E;
                                background-color: white;">
                            
                            <h2 style="text-align: left;
                                    align-items: center;">
                            Other info: 
                        </h2>
                            <p class="data"
                            style="text-align: justify-all;
                                    align-items: center;
                                    font-size: 15px;
                                    padding-bottom: 12px;">
                                ID user:
                            </p>
                            <p>
      
                            </a>
                            </p>
                        </td>
                    </tr>
                </tbody>
            </table>
        </body>

    """

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    return msg
