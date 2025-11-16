# Hotspot Autologin Scripts

A collection of Python scripts for automatically logging into hotspot networks.

## Features

*   **autologin.py**: Attempts to log in to a hotspot with a primary account. If the account is already in use, it will try to log in with randomly generated credentials from a wordlist.
*   **scrape_login.py**: Scrapes a website for a table of usernames and passwords and then attempts to log in to a target hotspot with the scraped credentials.

## Requirements

*   Python 3.x
*   `requests`
*   `selenium`
*   `beautifulsoup4`
*   Chromium WebDriver

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/hotspot_autologin.git
    cd hotspot_autologin
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install requests selenium beautifulsoup4
    ```

3.  **Download and install Chromium WebDriver:**
    *   Download the appropriate version of Chromium WebDriver for your system from the [official site](https://chromedriver.chromium.org/downloads).
    *   Place the executable in a directory that is in your system's `PATH` (e.g., `/usr/local/bin` on Linux/macOS or `C:\Windows` on Windows).

## Usage

### `autologin.py`

1.  **Open `autologin.py` in a text editor.**
2.  **Replace `<your_username>` and `<your_password>` with your primary hotspot credentials:**
    ```python
    USER = "your_actual_username"
    PASW = "your_actual_password"
    ```
3.  **Update the `url` in the `requests.post` call to the hotspot's login page URL.**
4.  **Ensure the `wl.txt` file is in the same directory and contains a list of usernames and passwords in the format `username:password`.**
5.  **Run the script:**
    ```bash
    python autologin.py
    ```

### `scrape_login.py`

1.  **Open `scrape_login.py` in a text editor.**
2.  **Update the URL in the `driver.get()` call to the website you want to scrape for credentials.**
3.  **Update the `URL` variable in the login loop to the hotspot's login page URL.**
4.  **Run the script:**
    ```bash
    python scrape_login.py
    ```

## Disclaimer

These scripts are intended for educational purposes only. Please use them responsibly and only on networks you are authorized to access. The author is not responsible for any misuse of these scripts.
