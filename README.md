# AI Email Writer

AI Email Writer is a Python-based application that generates professional emails using Google's Gemini AI model. The user provides a brief description of the email they want to write, and the application automatically generates a clear, structured, and professional email in seconds.

## Features

* Generate emails using AI
* Simple command-line interface
* Powered by Google Gemini API
* Secure API key management with environment variables
* Clean and modular Python implementation
* Easy to customize and extend

## Technologies Used

* Python 3
* Google Gemini API
* python-dotenv
* Virtual Environments (venv)

## Project Structure

```text
ai-email-writer/
│
├── email_writer.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abdou-dev-cs/AI-Email-Writer.git
cd AI-Email-Writer
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GENAI_API_KEY=YOUR_API_KEY_HERE
```

## Usage

Run the application:

```bash
python email_writer.py
```

Enter a prompt describing the email you want to generate.

### Example Prompt

```text
Write a professional email requesting a software engineering internship.
```

The AI will generate a complete professional email based on your request.

## Example Output

```text
Subject: Internship Application

Dear Hiring Manager,

I hope this message finds you well...

Kind regards,
John Doe
```

## Learning Objectives

This project was created to practice:

* Working with external APIs
* Environment variable management
* Python project organization
* Dependency management
* Git and GitHub workflows
* AI application development

## Future Improvements

* GUI version using Tkinter or PyQt
* Email tone selection
* Multi-language support
* Email templates
* Export generated emails to PDF
* Integration with email providers

## Author

**Abderrahmane Abdou**

Software Engineering Student | Flutter Developer | Python & AI Enthusiast
