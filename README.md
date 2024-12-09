# Passport Data Extraction with LLAMA 3.2 Vision

A Streamlit application for extracting structured data from passport images, supporting both **Romanian** and **Pakistani** passports. This project uses **LLAMA 3.2 Vision** for Optical Character Recognition (OCR) to ensure accurate data extraction.

---

## Features

- **Passport Type Selection**:
  - Extract data from **Romanian** or **Pakistani** passports.
  - Switch between passport types via a user-friendly interface.

- **Accurate Data Extraction**:
  - Reads and structures data from the passport fields precisely.
  - Ensures essential details are captured, including names, passport numbers, and issuance details.

- **Streamlit Interface**:
  - Easy-to-use web-based interface for uploading passport images.
  - Real-time data extraction with a clear display of results.

---

## Setup Instructions

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.11 or higher installed.
- Basic knowledge of Git.
- Access to the GitHub repository.





### Installation and Running the Application

1. **Clone the Repository**:
   Open your terminal and clone the repository:
   ```bash
   git clone https://github.com/FaizAhmeddd/Passport-Data-Extraction-with-LLAMA-3.2-Vision.git
   cd Passport-Data-Extraction-with-LLAMA-3.2-Vision

2. **Make Virtual Environment**:

    python -m venv env
    source env/bin/activate  # On Windows, use 'env\Scripts\activate'

3. **Install Dependencies**:

    pip install -r requirements.txt

4. **Run Streamlit App**:

    streamlit run app.py


### Project Structure

📦 Passport-Data-Extraction-with-LLAMA-3.2-Vision
├── app.py                     # Main Streamlit application
├── README.md                  # Project documentation
├── requirements.txt           # Required Python libraries
└── images/                    # (Optional) Store sample passport images





### **What’s Included in This README:**
- Comprehensive setup instructions, including Python version, virtual environment setup, and dependencies.
- Clear steps for using the application with screenshots if needed later.
- Detailed list of fields for both supported passport types.
- Contribution guidelines with suggestions for extending the project.

Feel free to copy and customize this `README.md` as needed!
