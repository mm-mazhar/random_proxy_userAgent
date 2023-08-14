### Random Proxy and User Agent
<br>
The provided Python script demonstrates an object-oriented approach to managing a Chrome WebDriver using the Selenium library for automated web testing. It allows you to easily initialize a WebDriver, perform actions on a web page, and then properly close the WebDriver when done.

The WebDriverManager class encapsulates the WebDriver-related functionality:

Initialization: In the initialize_driver method, a random User-Agent and a randomly selected proxy are generated using the fake_useragent and fp.fp libraries, respectively. These are added to the ChromeOptions to configure the WebDriver. Various options such as disabling security features, maximizing the browser window, and setting experimental options are configured. The WebDriver is then initialized and navigated to a test URL (https://www.amazon.com). The title of the page is printed, and a wait of 10 seconds is added to allow for manual inspection.

Closing the Driver: The close_driver method checks if the driver instance exists and, if so, quits the WebDriver to release system resources.

The script also provides a main block where an instance of WebDriverManager is created. Inside the try-except-finally block, the initialize_driver method is called to set up the WebDriver. This is where you can perform your desired web actions using the initialized driver instance. If an exception occurs during execution, it is caught and an error message is printed. The finally block ensures that the WebDriver is closed gracefully even if an error occurs.

This script provides a basic framework for managing WebDriver instances using an object-oriented approach, promoting code reusability and maintainability.
<br>
<br>

Before starting download the `chrome` and `chromedriver` and unzip the folders. 

- `https://googlechromelabs.github.io/chrome-for-testing/`

- Chrom: `https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/win64/chrome-win64.zip`

- chromedriver: `https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/win64/chromedriver-win64.zip`

- COPY the path of `chromedriver.exe` and
- SET the CHROME_DRIVER_PATH = "CHANGE ME" in `random_proxy_userAgent.py` file
