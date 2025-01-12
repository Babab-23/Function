import os
import sys

def shutdown(option=None):
    """
    Simulates or performs a system shutdown based on the operating system.
    
    Args:
        option (str): 'restart' to restart the system, 'shutdown' to turn it off.
                      If None, it simulates a shutdown process without actual action.
    """
    if option not in [None, 'shutdown', 'restart']:
        print("Invalid option. Use 'shutdown', 'restart', or None.")
        return

    # Simulate a confirmation process
    print("Are you sure you want to proceed? (yes/no)")
    confirm = input("> ").strip().lower()

    if confirm not in ['yes', 'y']:
        print("Action canceled.")
        return

    # Perform the actual shutdown or restart
    if option == 'shutdown':
        print("Shutting down the system...")
        if sys.platform == "win32":
            os.system("shutdown /s /t 0")
        elif sys.platform == "linux" or sys.platform == "darwin":
            os.system("sudo shutdown -h now")
    elif option == 'restart':
        print("Restarting the system...")
        if sys.platform == "win32":
            os.system("shutdown /r /t 0")
        elif sys.platform == "linux" or sys.platform == "darwin":
            os.system("sudo shutdown -r now")
    else:
        print("Simulating system shutdown. No actual action performed.")

# Example usage
print("Options: shutdown, restart, or None (simulation)")
action = input("Enter your choice: ").strip().lower()
shutdown(action)
