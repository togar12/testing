import tty
import sys
import termios

def getpass(prompt="Password: "):
    """
    Prompt for a password and return it as a string.

    This will disable terminal echoing while the user types the password.
    """
    # Save original terminal settings
    fd = sys.stdin.fileno()
    original_settings = termios.tcgetattr(fd)

    try:
        # Switch terminal to "raw" mode to prevent echoing
        tty.setraw(sys.stdin.fileno())

        # Print prompt
        sys.stdout.write(prompt)
        sys.stdout.flush()

        # Read input and return as a string
        password = ""
        while True:
            char = sys.stdin.read(1)
            if char == "\n":
                break
            password += char
        return password

    finally:
        # Restore original terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, original_settings)
