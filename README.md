# 🧪 SauceDemo Login Automation

A beginner-friendly **Python + Selenium + pytest** automation project for testing the login functionality of **SauceDemo**.

This project demonstrates browser automation, test cases, assertions, pytest fixtures, and a simple **Page Object Model (POM)** structure.

> 📱 The project is configured to run on Android using **Termux + Termux:X11 + Openbox + Chromium + ChromeDriver**.

---

## 📌 Project Overview

The purpose of this project is to automate and verify different login scenarios on SauceDemo.

### Test Scenarios

| # | Test | Expected Result |
|---|---|---|
| 1 | ✅ Valid Login | User reaches the Inventory page |
| 2 | ⚠️ Blank Login | `Username is required` error is displayed |
| 3 | 🚪 Login + Logout | User logs in and successfully logs out |
| 4 | ❌ Invalid Password | `Username and password do not match` error is displayed |

---

## 🛠️ Tech Stack

- 🐍 **Python**
- 🌐 **Selenium WebDriver**
- 🧪 **pytest**
- 🌍 **Chromium**
- 🚗 **ChromeDriver**
- 📱 **Termux**
- 🖥️ **Termux:X11**
- 🪟 **Openbox**
- 📦 **Git**
- ☁️ **GitHub**

---

## 📁 Project Structure

    Case/
    │
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    ├── conftest.py
    │
    ├── pages/
    │   └── login_page.py
    │
    └── tests/
        └── test_login.py

### 📄 File Description

| File / Folder | Purpose |
|---|---|
| `README.md` | Project documentation |
| `requirements.txt` | Python dependencies |
| `conftest.py` | Selenium WebDriver fixture and browser configuration |
| `pages/login_page.py` | Login page locators and actions |
| `tests/test_login.py` | Login test cases |
| `.gitignore` | Files ignored by Git |

---

# 🧩 Page Object Model

This project uses a simple **Page Object Model (POM)** approach.

The `LoginPage` class contains:

- 🔗 SauceDemo URL
- 👤 Username locator
- 🔑 Password locator
- 🔘 Login button locator
- ⚠️ Error message locator
- ☰ Menu button locator
- 🚪 Logout link locator
- 🔐 Login action
- 🚪 Logout action
- 💬 Error message retrieval

This keeps Selenium page-related code separate from the actual test cases.

---

# 🧪 Test Cases

## 1️⃣ Valid Login

Uses valid SauceDemo credentials and verifies that the user reaches the Inventory page.

**Expected Result:**

    Login successful
    Inventory page is opened

---

## 2️⃣ Blank Login

Attempts to log in without entering credentials.

**Expected Error:**

    Username is required

---

## 3️⃣ Valid Login + Logout

Verifies the complete login and logout flow.

**Flow:**

    Login
      ↓
    Inventory Page
      ↓
    Open Menu
      ↓
    Logout
      ↓
    Login Page

---

## 4️⃣ Invalid Password

Uses a valid username with an incorrect password.

**Expected Error:**

    Username and password do not match

---

# 📦 Requirements

Python dependencies are listed in:

    requirements.txt

The project requires:

    selenium
    pytest

Install the Python dependencies in Termux:

    pip install -r requirements.txt

> ℹ️ Termux, Termux:X11, Openbox, Chromium and ChromeDriver are environment components, not Python packages.

---

# 📱 Android / Termux Environment

This project runs Selenium with a **visible Chromium browser on Android**.

The graphical environment works like this:

    Termux
       ↓
    Termux:X11
       ↓
    Openbox
       ↓
    Chromium
       ↓
    Selenium + pytest

---

# 🔧 First-Time Environment Setup

These steps are required only when setting up the Android environment for the first time.

## 1️⃣ Update Termux

In Termux, run:

    pkg update
    pkg upgrade

---

## 2️⃣ Install Required Components

In Termux, install Python and Git:

    pkg install python git

Install the X11 repository:

    pkg install x11-repo

Install Termux:X11:

    pkg install termux-x11-nightly

Install Openbox:

    pkg install openbox

Install Chromium:

    pkg install chromium

Install ChromeDriver:

    pkg install chromedriver

Install the project's Python dependencies:

    pip install -r requirements.txt

Check the important installations in Termux:

    python --version
    pytest --version
    chromium-browser --version
    chromedriver --version

---

# 🖥️ First-Time X11 Setup

## 1️⃣ Start Termux:X11

In Termux, run:

    export DISPLAY=:0

    termux-x11 :0 &

Now open the **Termux:X11 Android application**.

A black screen may appear.

> ⚠️ This is normal. At this point X11 is running, but no window manager or application has been started yet.

---

## 2️⃣ Start Openbox

Go back to Termux and run:

    openbox &

Openbox manages application windows inside the X11 display.

---

## 3️⃣ Test the Graphical Display

In Termux, run:

    export DISPLAY=:0

    chromium-browser --no-sandbox

Now open the **Termux:X11 Android application** if it is not already open.

If Chromium appears inside the Termux:X11 screen and the display is properly visible/full-screen:

    ✅ Termux:X11 is working
    ✅ DISPLAY=:0 is working
    ✅ Openbox is working
    ✅ Chromium is visible
    ✅ Graphical setup is complete

Close the manually opened Chromium window.

The graphical environment is now ready for running the tests.

---

# ▶️ Run the Tests

After the graphical setup has been successfully completed, there is no need to repeat the complete X11 setup before every test run.

In Termux, go to the project directory:

    cd <project-directory>

In Termux, set the display:

    export DISPLAY=:0

In Termux, run the tests:

    pytest -v

Example:

    ================================ test session starts ================================

    tests/test_login.py::test_valid_login PASSED
    tests/test_login.py::test_blank_login PASSED
    tests/test_login.py::test_valid_login_and_logout PASSED
    tests/test_login.py::test_invalid_password PASSED

    ================================ 4 passed ================================

---

# ❌ If the Chromium Display Does Not Work

Only use this section if the Chromium graphical test does **not** work.

For example:

- Chromium does not open
- X11 remains blank
- Chromium is not visible
- The display is not working correctly

## 1️⃣ Stop the Graphical Processes

In Termux, run:

    pkill -f chromium
    pkill -f chromium-browser
    pkill -f chromedriver
    pkill -f openbox
    pkill -f termux-x11

---

## 2️⃣ Restart Termux:X11

In Termux, run:

    export DISPLAY=:0

    termux-x11 :0 &

Open the **Termux:X11 Android application**.

---

## 3️⃣ Start Openbox

Go back to Termux and run:

    openbox &

---

## 4️⃣ Test Chromium Again

In Termux, run:

    export DISPLAY=:0

    chromium-browser --no-sandbox

Check the **Termux:X11 Android application**.

If Chromium is visible and the display is working correctly:

    ✅ X11 is ready
    ✅ Openbox is ready
    ✅ Chromium is ready

Close the manually opened Chromium window.

Then run the tests:

    cd <project-directory>
    export DISPLAY=:0
    pytest -v

There is no need to reinstall the packages during this reset.

---

# ⚙️ Selenium Configuration

The Selenium WebDriver configuration is located in:

    conftest.py

The configuration includes:

- Chromium browser
- ChromeDriver
- X11 display `:0`
- `--no-sandbox`
- `--disable-dev-shm-usage`
- Separate Selenium browser profile

The browser runs **visibly through Termux:X11**.

The project does **not** use headless mode or `--start-maximized`.

---

# 🎯 Run a Specific Test File

In Termux, from the project directory, run:

    pytest -v tests/test_login.py

---

# ⚠️ Important Notes

- 🖥️ X11 must be running before Selenium tests.
- `DISPLAY=:0` is required for the graphical browser.
- A black screen when X11 first opens is normal.
- Openbox must be started before Chromium.
- Chromium is used as the visual test to confirm that the graphical environment is ready.
- Once Chromium opens correctly, there is no need to repeat the complete X11 setup before every test run.
- If the graphical environment stops working, use the reset section above.
- Chromium runs visibly so Selenium actions can be observed.
- The project does not use `--start-maximized`.
- The project directory can be different for every user.

---

# 🔐 Security

Never commit sensitive information to GitHub.

### ❌ Never upload:

- Passwords
- Personal Access Tokens
- SSH private keys
- API keys
- `.env` files
- Other confidential credentials

The `.gitignore` file helps prevent unwanted files from being committed.

---

# 🌱 Git Workflow

After making changes, check the repository status.

In Termux, run:

    git status

Stage changes:

    git add .

Create a commit:

    git commit -m "Describe your changes"

Push changes to GitHub:

    git push

Get the latest changes:

    git pull

---

# 🎯 Learning Goals

This project is being used to practice:

- 🐍 Python
- 🌐 Selenium WebDriver
- 🧪 pytest
- 📝 Test cases
- ✅ Assertions
- 🔧 Fixtures
- 🧩 Page Object Model
- 🤖 Browser automation
- 📦 Git
- ☁️ GitHub
- 📚 Project documentation
- 📋 Python dependency management

---

# ☁️ GitHub Repository

**Hecticshinu/saucedemo-login-automation**

---

# 👨‍💻 Author

**Shinu**

This project was created for learning and practicing **Python + Selenium test automation**.