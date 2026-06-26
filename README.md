# TweeBot: Smart Twitter (X) Management and Automation System

**TweeBot** is a powerful and modular Python-based automation tool designed for simultaneous management of multiple Twitter (X) accounts, scheduling, and automatic posting of tweets (text and images).

This software is equipped with a modern user interface (Dark Mode UI) developed with Tkinter, and its architecture is implemented in a two-part structure (management dashboard + independent execution core) to provide a high level of stability and prevent the user interface from freezing during tweet sending processes.

## System Architecture and Workflow

The architecture of TweeBot is built on the Separation of Concerns and consists of two main parts:

1. **Management Dashboard (TweeBot.exe):** Responsible for managing processes, registering account information, composing tweets, previewing media images, managing the sending queue, and displaying reports.

2. **Twitter Execution Core (Client.exe):** A separate and independent module responsible for communicating with the Twitter API (v2.0) through the Tweepy library, uploading images, and sending tweets.

### Tweet Sending Cycle in the Bot:

- **Preparation of the sending cycle:** With the start of the sending process in twee.py, for each account in turn, the send directory is cleared, and the necessary information (Tweet_information.txt and pic.jpeg) is copied into it.

- **Calling the Subprocess:** The twee.py file calls the executable file Client.exe.

The user layer waits for a response while showing a loading animation.

- **Core Execution and Authentication:** The Client.exe program reads information from the exchange layer folder, performs Twitter validation, and sends the tweet.

- **Status Feedback (IPC):** After finishing the task, Client.exe writes the word Tweeted (or the error text) in the result.txt file.

- **User Layer Update:** The twee.py file reads this file and changes the live account status in the listbox to ✔ or ❌, and finally saves the final report in the report directory.

## ✨ Key Features

- **Multimedia Account Management:** Possibility of adding unlimited Twitter accounts along with dedicated API keys.

- **Process Separation (Multi-processing):** No freezing of the program's graphical layer during tweet sending due to offloading the network processing load to Client.exe.

- **Support for Image Tweets:** Possibility of attaching images in .jpeg format to each account separately with preview capability within the program environment.

- **Smart Reporting System (Reporting):** Automatic generation of the final report file after the bot finishes working on all accounts.

- **Modern Dark UI (Modern Dark UI):** Designed with standard colors for less eye fatigue during long-term monitoring.

## 📂 Project Folder Structure

After the first execution of the program, the following directory structure is automatically created:

```text
TweeBot/
│
├── TweeBot.exe                     # Main management dashboard and bot user interface
├── Client.py                   # Twitter sending core source code (Twitter API Worker)
├── Client.exe                  # Compiled version of Client.py (must be alongside twee.py)
│
├── Account/                    # Location for storing tweet texts and sensitive account information (txt files)
├── picture/                    # Attached images of tweets with naming matching the account number (jpeg)
├── send/                       # Temporary folder for data exchange between the dashboard and the execution core
├── report/                     # Location for storing the bot's final performance report (report.txt)
│
├── Configuration/              # Directory for maintaining icons and program styles
│   ├── DesignboltsHandStitchedTwitter.ico
│   └── BlackvariantButtonUiSystemFoldersDrivesSystem.ico
└── result.txt                  # Interface file for success status or operation sending error
```

---

## 🛠 Prerequisites and Setup

To run the Python source code, you need Python version 3.8 or higher and the following libraries:

```bash
pip install tweepy pillow
```

### Compiling

Since twee.py calls the output file as Client.exe, you must compile the core source using pyinstaller:

```bash
pip install pyinstaller

pyinstaller --noconfirm --onefile --windowed --icon "<Path to folder>\Configuration\BlackvariantButtonUiSystemFoldersDrivesSystem.ico" "<path to folder>\Client.py"
```

- *Note: After building the exe file in the dist folder, move it to the main project directory (alongside TweeBot.exe) and change its name to Client.exe.*

---

## User Guide for the Program

> You have to open the TweeBot.exe. Never don't open Client.exe

### 1. Registering User Accounts (Account Management)

- Enter the **⚙ Account Management** section.

- Enter account information including username, password, and the 5 Twitter API tokens:

  - API Key / API Secret Key

  - Access Token / Access Token Secret

  - Bearer Token

- Click the **Register Account** button.

  Accounts are automatically saved with numerical naming (such as 1.txt, 2.txt).

> To access these account tokens, you must enter the website [developer.twitter.com](https://developer.twitter.com/en/portal/projects-and-apps) and access these tokens after entering the username and password.

### 2. Composing Text and Selecting Tweet Image

- Enter the **Write Tweet Text** section.

- From the left column, select your desired account.

- Write the tweet text in the text box.

- If desired, click the **Browse** button and select an image with .jpeg format.

- Press the **Register Tweet** button.

### 3. Running the Bot and Sending Automation

- From the main menu, enter the **Run Bot** section.

- The system starts automatically and sequentially from account number 1, transfers the information to the sending core, and executes Client.exe.

- After starting the sending process for each account, two windows open.

  The first window is countdown, which is built-in for limitations.

  The second window, which opens with a slight delay relative to the first window, displays the result of sending the tweet or, if it is not sent, the error text.

- The status of each account is displayed live with ✔ (successful) or ❌ (unsuccessful) signs along with a preview of the image and text.

---

## Data Structure of Account Files

Each user account file in the Account folder is stored line by line in a standard format.

The structure of the lines is as follows and manual modification is not recommended:

- **Line 1:** Username

- **Line 2:** Password

- **Line 3:** Empty output (padding)

- **Line 4:** API_KEY

- **Line 5:** API_SECRET_KEY

- **Line 6:** Bearer_Token

- **Line 7:** ACCESS_TOKEN

- **Line 8:** ACCESS_TOKEN_SECRET

- **Line 9 onwards:** Tweet Text

> After the end of the tweet sending process, it writes their information and results for each account in the report.txt file located in the report folder

---

## TweeBot Limitations:

Twitter (X) API limitations that must be taken into consideration are as follows:

## 1. Tweet Sending Limitations

The type of limitations is divided into two categories: **User-level** and **App-level**:

- **Time limit of each account's user** (dedicated Access Token) in standard/Basic packages is allowed to send a maximum of **100 tweets in each 15-minute interval**.

- **App Rate Limit:** **If you use a shared API Key for all accounts:** Your entire bot will be allowed to send a maximum of 10,000 tweets (in the Basic plan) among all accounts over 24 hours.

- **If each account has its own dedicated API Key:** This app limitation is practically bypassed and each account will have its own independent limit.

- The platform limitation for Twitter's own free accounts applies a strict limitation of **50 posts per day** for regular and unverified accounts (without a blue checkmark) to prevent spam.

## 2. Image Upload Limitations

- **Daily upload count:** Each account is allowed to upload a maximum of **500 images in 24 hours**.

- **File size and format:** The selected format for attaching photos for each account is .jpeg.

  The size of the images must not exceed **5 MB** for regular accounts.

### 🔴 A Dangerous Threat in Sending Tweets:

If the user lines up a large number of accounts, the bot immediately clicks the execution button of the second account after the first Client.exe finishes its task.

Torrential posting on different accounts from a single IP will quickly confront your process with the **HTTP 429 (Too Many Requests)** error.

## Solution for Error 429

- **Load Distribution:** Since the sending process for each account is executed one by one and the previous process is closed, the risk of simultaneous sending (Concurrent Requests) and Twitter becoming suspicious of robotic behavior is significantly reduced.

- **Closing Sessions:** The structure of Client.exe is designed such that after a few seconds, it completely closes via `window.destroy()` or an exit method.

  This causes the Connection headers to reset and reduces the probability of a temporary IP block.

- Since the twee.py file opens Client.exe windows sequentially, it does not move on to the next account until the previous window is closed.

- This 15-second countdown acts as an **enforced delay (Delay)** between switching from one account to the next.

- This move prevents consecutive spammy sending and makes the bot's behavior appear more natural to Twitter.
