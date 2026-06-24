# 🤖 AI Test Automation Platform

An AI-powered end-to-end test automation framework that allows users to write test cases in plain English and automatically executes them using browser automation.

Inspired by modern intelligent testing platforms like TestRigor, this project simplifies UI automation by converting human-readable test steps into executable automation workflows.

---

## 🚀 Features

### Natural Language Test Automation

Write test cases in simple English:

```text
Open URL
Click Account
Type user@example.com in Username
Click Login
Verify Dashboard is visible
```

The platform automatically converts these steps into executable browser automation actions.

### AI-Powered Parsing

* Converts plain English instructions into structured test actions
* Reduces scripting effort
* Makes automation accessible for non-technical users

### Browser Automation

Powered by Playwright for:

* Cross-browser support
* Fast execution
* Reliable element handling
* Modern web application testing

### Execution Evidence

* Captures execution screenshots
* Tracks step-by-step execution
* Maintains test evidence for reporting

### Automated Reporting

Generates detailed execution reports including:

* Test status
* Passed steps
* Failed steps
* Error messages
* Execution duration

---

# 📌 Project Architecture

```text
User Test Case (Plain English)
            │
            ▼
     AI Parser Engine
            │
            ▼
 Structured Test Actions
            │
            ▼
 Playwright Execution Engine
            │
            ▼
 Screenshot & Evidence Capture
            │
            ▼
     Execution Report
```

---

# 🛠 Technology Stack

| Technology    | Purpose                  |
| ------------- | ------------------------ |
| Python        | Backend Development      |
| Flask         | API Framework            |
| Playwright    | Browser Automation       |
| OpenAI API    | Natural Language Parsing |
| Pydantic      | Data Validation          |
| Requests      | API Communication        |
| Python Dotenv | Environment Management   |

---

# 📂 Project Structure

```text
AI-Test-Automation/
│
├── app.py
├── parser.py
├── executor.py
├── report_generator.py
├── requirements.txt
│
├── test_cases/
│   ├── INR.txt
│   ├── USD.txt
│   └── MYR.txt
│
├── screenshots/
│
├── reports/
│
├── static/
│
├── templates/
│
├── .env
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-test-automation.git
cd ai-test-automation
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Playwright Browsers

```bash
playwright install
```

Verify installation:

```bash
python -c "from playwright.sync_api import sync_playwright; print('OK')"
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
BASE_URL=https://your-application-url.com
```

---

# ▶ Running the Application

Start Flask Server:

```bash
python app.py
```

Application will start on:

```text
http://localhost:5000
```

---

# 📝 Sample Test Case

Example:

```text
Open URL

Click Account

Hover Account

Click Sign In

Type test@example.com in Username

Type Password123 in Password

Click Login

Wait until page is loaded
```

The AI parser converts the above instructions into Playwright automation commands and executes them automatically.

---

# 📊 Execution Flow

### Step 1

User enters test case in plain English.

### Step 2

AI parser interprets the test steps.

### Step 3

Playwright executes actions in browser.

### Step 4

Screenshots are captured.

### Step 5

Execution report is generated.

---

# 📷 Example Test Scenarios

### Account Module

* Account Navigation
* Hover Menu Validation
* Sign-In Flow
* Registration Flow
* Logout Validation

### Authentication Module

* Email Login
* Mobile Login
* WhatsApp Login
* OTP Verification
* Forgot Password

### Regional Testing

* INR Workflow
* USD Workflow
* MYR Workflow

### User Registration

* New User Signup
* Country Selection
* Email Verification
* OTP Validation

---

# 📈 Future Enhancements

* Parallel Test Execution
* Dashboard Analytics
* AI Self-Healing Locators
* Real-Time Execution Monitoring
* Cloud Execution Support
* Test Scheduling
* CI/CD Integration
* PDF & Excel Reporting
* Multi-Browser Parallel Runs

---

# 🎯 Benefits

* No coding knowledge required
* Faster automation creation
* Easy maintenance
* Human-readable test cases
* Reduced QA effort
* Scalable automation framework

---

# 📄 Example Workflow

```text
Write Test Case
        │
        ▼
AI Parser
        │
        ▼
Automation Script
        │
        ▼
Playwright Execution
        │
        ▼
Screenshots
        │
        ▼
HTML/PDF Report
```

---

# 👨‍💻 Author

Sri Vishnu

AI Engineer | Automation Engineer

Focused on AI-powered testing, browser automation, chatbot development, and workflow automation.

---

# 📜 License

This project is intended for educational, research, and automation purposes.
Feel free to fork, improve, and contribute.
