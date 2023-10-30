import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

# Replace these with your actual email and password
my_email = "Your Email Id"
password = "Your Password"

# The URL of the Amazon product page you want to monitor
url = "https://www.amazon.com/SAMSUNG-Inch-Internal-MZ-77E1T0B-AM/dp/B08QBJ2YMG/ref=sr_1_7?qid=1678273152&s=computers-intl-ship&sr=1-7"

# HTTP headers to mimic a web browser request
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Send an HTTP GET request to the Amazon page
response = requests.get(url, headers=header)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")

    # Find the price element on the page
    price_element = soup.find(name="span", class_="a-offscreen")

    # Check if the price element was found
    if price_element:
        price = price_element.get_text()

        # Extract the price as a floating-point number
        price_without_currency = price.split("$")[1]
        price_as_float = float(price_without_currency)

        # Print the current price
        print(price_as_float)

        # Define the target price at which you want to receive an alert
        BUY_PRICE = 68

        # Check if the current price is below your target price
        if price_as_float < BUY_PRICE:
            message = f"SAMSUNG 870 EVO SATA III SSD 1TB 2.5 ${price_as_float} is now {price}"

            # Set up an SMTP connection to your email provider (in this case, Gmail)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # Start a secure connection
                connection.login(user=my_email, password=password)

                # Send an email alert
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="recipient's email address",  # Replace with the recipient's email address
                    msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}")
    else:
        print("Price element not found on the page.")
else:
    print(f"Failed to retrieve the Amazon page. Status code: {response.status_code}")
