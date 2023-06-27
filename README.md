# Decrypt Locally Stored Microsoft Edge Passwords
&#9888; CAUTION: PLEASE USE THIS CODE FOR EDUCATIONAL PURPOSES ONLY. EXPORTING OR VIEWING ANOTHER PERSON'S BROWSER PASSWORDS WITHOUT THEIR CONSENT IS ILLEGAL. DO NOT UTILIZE THIS CODE FOR MALICIOUS INTENT. IT IS YOUR SOLE RESPONSIBILITY TO BE MINDFUL OF YOUR ACTIONS.

---
This repository contains code that allows you to export passwords from Edge browser and save them as a CSV file. 

## Prerequisites

Before running the code, make sure you have the following:

- Python 3.8 or above installed on your machine
- [Microsoft Edge](https://www.microsoft.com/en-us/edge/download?form=MA13FJ&ch) installed
- Clone or download this repository to your local machine

## Installation

1. Create a new virtual environment (optional but recommended):
   ```bash
   conda env create -f conda-env.yml
   conda activate browser-decrypt
   ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory where you cloned or downloaded this repository.
3. Run the following command to execute the code:

    ```bash
    python main.py
    ```
4. After running the command, a CSV file named `passwords.csv` will be generated in the same directory. This file will contain the URLs, usernames, and passwords stored in your Microsoft Edge browser.

## Disclaimer
Please exercise utmost caution and use this code solely for educational purposes. Exporting or accessing another individual's browser passwords without their explicit consent is both illegal and unethical. You bear full responsibility for any actions performed using this code.

## Credits
This project was inspired by the work of John Hammond, a talented YouTuber. His dedication and informative content motivated the creation of this project.

## License
This project is licensed under the [MIT License](LICENSE).
