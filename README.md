# IEC Viewer Automation

This project automates the process of extracting data from the IEC Viewer website using Selenium WebDriver. The script navigates to the website, fills in the required fields, and retrieves the data, which is then saved as a JSON file.


## Features
- Automated web interaction using Selenium.
- Headless browser option for faster execution.
- Data extraction and saving in JSON format.
- Screenshot capture of the output page.

## Requirements
- Python 3.x
- Selenium
- WebDriver Manager (optional for automatic ChromeDriver management)

## Installation
1. Clone the repository:
   
   git clone https://github.com/yourusername/IECViewerAutomation.git
   cd IECViewerAutomation
Configuration
Before running the script, update the config.py file with your specific details:

BASE_URL: The URL of the IEC Viewer website.
IEC_CODE: The IEC code to search for.
NAME_THREE_CHARACTERS: Your name or any three-character name.
SECURITY_CODE: The security code required by the website.
OUTPUT_JSON: Path to save the extracted JSON data.
SCREENSHOT_PATH: Path to save the screenshot.
SERVICE_PATH: Path to the ChromeDriver executable.
Example config.py:

python

BASE_URL = "http://example.com/iec_viewer"
IEC_CODE = "ABC1234567"
NAME_THREE_CHARACTERS = "John"
SECURITY_CODE = "your_security_code"
OUTPUT_JSON = "output/extracted_data.json"
SCREENSHOT_PATH = "output/screenshot.png"
SERVICE_PATH = "C:/path/to/chromedriver.exe"
Usage
Run the extraction script using the following command:


python src/extractor.py

Upon successful execution, the extracted data will be saved in output/extracted_data.json. An optional screenshot of the output page will be saved as output/screenshot.png.

Sample Output (extracted_data.json)
json

{
    "extracted_data": {
        "iec_code": "ABC1234567",
        "name": "John Doe",
        "captcha_verification": "Please verify that you are not a robot."
    }
}


## Output

Upon successful execution of the IEC Viewer Automation script, the following outputs will be generated:

1. **Extracted Data**: 
   - The script will retrieve information based on the provided IEC code and other input fields. This data will be saved in a JSON format within the `output` directory. The JSON file will have the name `extracted_data.json` and will contain the relevant details extracted from the webpage.
   - **Sample Structure of `extracted_data.json`**:
     ```json
     {
         "extracted_data": {
             "iec_code": "12345678",
             "company_name": "Sample Company",
             "status": "Active"
         }
     }
     ```


3. **Error Handling**:
   - If there are issues such as an incorrect IEC code or a CAPTCHA prompt that needs to be solved, the script will terminate with an error message in the console. Ensure that the required CAPTCHA is manually solved to proceed with the data extraction.
