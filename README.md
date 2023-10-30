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

1. Replace `"Your Email Id"` and `"Your Password"` with your Gmail email address and password in the script.

2. Set your target price in the `BUY_PRICE` variable.

3. Run the script:

   ```bash
   python amazon_price_tracker.py
   ```

4. The script will check the price of the Amazon product and send an email notification if the price drops below your target.

## Contributing

If you'd like to contribute to this project or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is provided for educational and personal use only. Use it responsibly and ensure compliance with Amazon's terms of service.

---

**Note:** Please be cautious when including sensitive information (such as email and password) directly in your code. Consider using environment variables or a more secure method to store and access sensitive information.
```
