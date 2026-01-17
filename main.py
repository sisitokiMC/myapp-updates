# main.py (updated)
import tkinter as tk
import subprocess
import sys

def main():
    # Run updater first
    try:
        subprocess.run([sys.executable, "updater.py"], check=True)
    except Exception as e:
        print(f"[WARNING] Updater failed: {e}")

    # Then continue with app
    root = tk.Tk()
    root.title(f"My Awesome App v{get_current_version()}")
    root.geometry("400x200")

    label = tk.Label(root, text=f"Hello from version {get_current_version()}! (Updated!)", font=("Arial", 16))
    label.pack(pady=50)

    root.mainloop()

def get_current_version():
    try:
        with open("version.txt", "r") as f:
            return f.read().strip()
    except:
        return "Unknown"

if __name__ == "__main__":
    main()
