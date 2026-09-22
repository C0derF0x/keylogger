# ⌨️ Python Keylogger

A simple **Python keyboard-monitoring project** built with [`pynput`](https://pypi.org/project/pynput/).

This project was created as a **Python learning/cybersecurity experiment** to demonstrate how keyboard events can be detected and recorded to a local text file.

> ⚠️ **Responsible Use**
>
> This software can capture keyboard input and potentially record sensitive information such as passwords, messages, and other private data.
>
> 🔒 **Only run it on systems you own or where you have explicit permission to monitor.**
>
> ❌ Do not use this software to secretly monitor other people or collect their credentials/data.

---

## ✨ Features

* ⌨️ Detects keyboard press events using `pynput`
* 📝 Records normal character input
* ␣ Handles common special keys:

  * ␠ Space
  * ↵ Enter
  * ⌫ Backspace
  * 🛑 Escape
* 💾 Saves recorded input to a user-specified local text file
* 🕐 Adds timestamps when the program starts and stops
* 🛑 Pressing `Esc` stops the program

---

## 🛠️ Requirements

* 🐍 Python 3.x
* 📦 `pynput`

Install the dependency with:

```bash
pip install pynput
```

---

## ⚙️ Configuration

Before running the program, replace:

```python
log_file = "YOUR_LOG_FILE_PATH_HERE"
```

with the path where you want the output file to be stored.

For example:

```python
log_file = "C:\\Users\\Username\\Desktop\\keylog.txt"
```

💡 You can also use a raw string to make Windows paths easier to read:

```python
log_file = r"C:\Users\Username\Desktop\keylog.txt"
```

---

## 🚀 Running the Program

Run the Python file from a terminal:

```bash
python keylogger.py
```

The program will begin listening for keyboard events and write them to the configured local file.

🛑 Press **Esc** to stop the program.

---

## 🧠 How It Works

The program creates a `pynput.keyboard.Listener`:

```python
keyboard.Listener(on_press=on_press, on_release=on_release)
```

Whenever a key is pressed, `on_press()` is called.

Normal character keys are handled using:

```python
key.char
```

Special keys such as **Space**, **Enter**, **Backspace**, and **Escape** are handled separately.

The program uses a file handle to write the captured input directly to the configured output file.

---

## 📁 Project Structure

```text
.
├── 🐍 keylogger.py
├── 📖 README.md
└── 📝 keylog.txt
```

---

## ⚠️ Limitations

This is a basic educational implementation. It does **not** attempt to provide:

* 🚫 Persistence
* 🌐 Remote data transmission
* 🥷 Stealth mechanisms
* 🔑 Credential extraction
* 📤 Data exfiltration
* 🔐 Encryption
* ⚙️ Startup persistence

The project is intentionally limited to **local keyboard-event logging**.

---

## 🎓 Purpose

The project demonstrates several Python concepts, including:

* 🐍 Python functions
* 📦 External packages
* ⌨️ Keyboard event listeners
* 📂 File handling
* 🕐 Date and time handling
* ⚡ Event-driven programming
* 🧩 Exception handling

---

## ⚖️ Disclaimer

This repository is provided for **educational and authorized cybersecurity testing purposes only**.

The author does not encourage or endorse unauthorized monitoring, credential collection, privacy violations, or deployment of keyloggers on systems without the owner's explicit permission.

🔒 **Use responsibly. Stay ethical.**
