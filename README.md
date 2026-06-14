# ⌨️ Simple Keylogger — PRODIGY_CS_04

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![pynput](https://img.shields.io/badge/pynput-Library-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Internship](https://img.shields.io/badge/Prodigy-InfoTech-purple?style=for-the-badge)

> **Task 04** — Prodigy InfoTech Cyber Security Internship

---

## ⚠️ Ethical Disclaimer

> This keylogger is developed **strictly for educational purposes** as part of a cybersecurity internship.
>
> - ✅ Use ONLY on your **own system**
> - ✅ Use ONLY with **full consent**
> - ❌ **NEVER** use on someone else's computer without permission
> - ❌ Unauthorized keylogging is **ILLEGAL** and punishable by law
>
> The purpose of this project is to **understand how keyloggers work** so cybersecurity professionals can better **detect and defend** against them.

---

## 📌 Task Description

Create a basic keylogger program that **records and logs keystrokes**. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

---

## ✨ Features

- ✅ Records all keystrokes in real-time
- ✅ Logs **timestamps** for each key press
- ✅ Handles **special keys** (Enter, Space, Backspace, Tab etc.)
- ✅ Saves all logs to `keylog.txt`
- ✅ Stop with **ESC key** or **Ctrl+C** — both handled gracefully
- ✅ Session **summary** (total keys + duration)
- ✅ View & Clear log from menu

---

## 🛠️ Requirements

```bash
pip install pynput
```

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/Prasadsarkate/PRODIGY_CS_04.git

# Navigate to folder
cd PRODIGY_CS_04

# Install dependencies
pip install pynput

# Run the program
python keylogger.py
```

---

## 💻 Usage Example

```
==================================================
   ⌨️  Simple Keylogger — Task 04
   Prodigy Infotech Internship
==================================================

  ⚠️  ETHICAL NOTICE:
  This tool is for EDUCATIONAL purposes only.

  Options:
  1. Start Keylogger
  2. View Log File
  3. Clear Log File
  4. Exit

  Enter choice: 1

  🟢 Keylogger started! Press ESC to stop.
  📄 Logging to: /path/to/keylog.txt

  Key #0001 [13:45:23] → 'H'
  Key #0002 [13:45:23] → 'e'
  Key #0003 [13:45:23] → 'l'
  Key #0004 [13:45:24] → 'l'
  Key #0005 [13:45:24] → 'o'

  🔴 Keylogger stopped.
  📊 Total keys logged : 5
```

### 📄 Log File (`keylog.txt`)

```
==================================================
  Keylogger Session Started
  Date/Time : 2026-06-14 13:45:20
==================================================

Hello World
This is a test

==================================================
  Session Ended
  Total Keys Pressed : 23
  Duration           : 0:00:18
==================================================
```

---

## 🔑 Key Mappings

| Key Pressed | Logged As |
|-------------|-----------|
| A–Z, a–z, 0–9 | Character itself |
| Space | ` ` (space) |
| Enter | `\n` (new line) |
| Backspace | `[BACKSPACE]` |
| Tab | `[TAB]` |
| Delete | `[DELETE]` |
| Caps Lock | `[CAPS_LOCK]` |
| ESC | Stops the logger |

---

## 📂 Project Structure

```
PRODIGY_CS_04/
│
├── keylogger.py    # Main program
├── keylog.txt      # Generated log file (after running)
└── README.md       # Project documentation
```

---

## 📚 What I Learned

- How **keyloggers work** at the OS level
- Using **pynput** library for keyboard listening
- Importance of **ethical hacking** principles
- **Event-driven programming** in Python
- How to build defensive awareness against such tools

---

## 👨‍💻 Author

**Prasad** — Cyber Security Intern @ Prodigy InfoTech

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/prasadsarkate)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Prasadsarkate)

---

## 🏢 Internship

This project was completed as part of the **Prodigy InfoTech Cyber Security Internship**.

`#ProdigyInfoTech` `#Internship` `#CyberSecurity` `#Python` `#EthicalHacking` `#Keylogger`
