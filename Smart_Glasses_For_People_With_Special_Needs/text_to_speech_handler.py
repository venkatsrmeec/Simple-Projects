# Mook Mitra - Text-to-Speech Handler
# FINAL VERSION: Adds a 'wait_for_completion' parameter for full control over speech behavior.

import sys
import subprocess

def speak(text, wait_for_completion=False):
    """
    Speaks text using the OS's native voice.
    - By default (wait_for_completion=False), it speaks in the background (non-blocking).
    - When wait_for_completion=True, the program will pause until the speech is finished (blocking).
    """
    if not text or not isinstance(text, str):
        return

    command = ''
    # --- Windows-specific command ---
    if sys.platform == 'win32':
        command = f'powershell -ExecutionPolicy Bypass -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\');"'
        print(f"Speaking (Windows): {text}")
    # --- macOS-specific command ---
    elif sys.platform == 'darwin':
        command = ['say', text]
        print(f"Speaking (macOS): {text}")
    # --- Linux-specific command ---
    else:
        command = ['espeak', text]
        print(f"Speaking (Linux): {text}")

    if wait_for_completion:
        # subprocess.run() waits for the command to complete. Ideal for sequential messages.
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # subprocess.Popen() runs it in the background. Ideal for real-time feedback.
        subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# --- You can run this file directly to test if your OS speech is working ---
if __name__ == '__main__':
    print("Testing the OS-native text-to-speech handler...")
    speak("This is the first message.", wait_for_completion=True)
    speak("This is the second message, spoken after the first one finished.", wait_for_completion=True)
    print("Test complete.")

