# Amazon Product Price Tracker using BeautifulSoup

## Overview

This Python script allows you to track the price of a product on Amazon and receive an email alert when the price falls below a specified threshold. 
It uses web scraping to extract the current price of the product and sends email notifications using the Gmail SMTP server.

## Features

- Web scraping to fetch the current price of an Amazon product.
- Email notification when the price drops below a specified threshold.
- Customizable target price for monitoring.

## Prerequisites

Before using this script, you need to:

1. Install Python: [Download Python](https://www.python.org/downloads/)

2. Install the required Python packages:

   ```bash
   pip install requests
   pip install lxml
   pip install beautifulsoup4
   ```

3. Configure your Gmail account to allow less secure apps: [Allow less secure apps](https://support.google.com/accounts/answer/185833)

## Usage

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/NoorMahammad-S/amazon-price-tracker.git
   ```

2. Install the required Python libraries.

   ```bash
   pip install requests lxml beautifulsoup4
   ```

3. Update the script with your email and password.

   - Replace `Your Email Id` with your Gmail email address.
   - Replace `Your Password` with your Gmail password (consider using an app-specific password for security).

4. Set your target price by changing the `BUY_PRICE` variable in the script.

5. Run the script:

   ```bash
   python amazon_price_tracker.py
   ```

6. The script will periodically check the price of the specified Amazon product and send you an email notification if it drops below your defined threshold.

## Configuration

You can customize the following variables in the script:

- `BUY_PRICE`: The target price at which you want to receive an email alert.
- `url`: The URL of the Amazon product you want to track.
- `my_email`: Your Gmail email address.
- `password`: Your Gmail password (consider using an app-specific password for security).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## Acknowledgments
- This project was inspired by the need to track prices of products on Amazon.

## Disclaimer

This script is provided for educational and personal use only. Use it responsibly and ensure compliance with Amazon's terms of service.

---
**Note:** Please be cautious when including sensitive information (such as email and password) directly in your code. Consider using environment variables or a more secure method to store and access sensitive information.
