import os
import platform
import psutil
import socket
import subprocess
import random
import string

# Utility functions
def clear_terminal():
    """Clear the terminal screen."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def generate_password(length=12):
    """Generate a random secure password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# File operations
def list_files(path="."):
    """List files in a directory."""
    try:
        return os.listdir(path)
    except Exception as e:
        return f"Error: {e}"

def rename_file(old_name, new_name):
    """Rename a file."""
    try:
        os.rename(old_name, new_name)
        return f"Renamed '{old_name}' to '{new_name}'."
    except Exception as e:
        return f"Error: {e}"

def delete_file(file_name):
    """Delete a file."""
    try:
        os.remove(file_name)
        return f"Deleted file '{file_name}'."
    except Exception as e:
        return f"Error: {e}"

# System operations
def system_stats():
    """Show basic system stats."""
    stats = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
    }
    return stats

def list_processes():
    """List running processes."""
    try:
        processes = [(p.pid, p.name()) for p in psutil.process_iter()]
        return processes[:10]  # Limit to 10 processes for brevity
    except Exception as e:
        return f"Error: {e}"

# Network operations
def ping_host(host):
    """Ping a host."""
    try:
        result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

def resolve_domain(domain):
    """Resolve a domain to an IP address."""
    try:
        return socket.gethostbyname(domain)
    except Exception as e:
        return f"Error: {e}"

# Python package management
def install_python_package(package):
    """Install a Python package."""
    try:
        subprocess.check_call(["pip", "install", package])
        return f"Python package '{package}' installed successfully."
    except Exception as e:
        return f"Error installing Python package '{package}': {e}"

def update_python_package(package):
    """Update a Python package."""
    try:
        subprocess.check_call(["pip", "install", "--upgrade", package])
        return f"Python package '{package}' updated successfully."
    except Exception as e:
        return f"Error updating Python package '{package}': {e}"

def remove_python_package(package):
    """Uninstall a Python package."""
    try:
        subprocess.check_call(["pip", "uninstall", "-y", package])
        return f"Python package '{package}' removed successfully."
    except Exception as e:
        return f"Error removing Python package '{package}': {e}"

# Node package management
def install_node_package(package):
    """Install a Node package."""
    try:
        subprocess.check_call(["npm", "install", package])
        return f"Node package '{package}' installed successfully."
    except Exception as e:
        return f"Error installing Node package '{package}': {e}"

def update_node_package(package):
    """Update a Node package."""
    try:
        subprocess.check_call(["npm", "update", package])
        return f"Node package '{package}' updated successfully."
    except Exception as e:
        return f"Error updating Node package '{package}': {e}"

def remove_node_package(package):
    """Remove a Node package."""
    try:
        subprocess.check_call(["npm", "uninstall", package])
        return f"Node package '{package}' removed successfully."
    except Exception as e:
        return f"Error removing Node package '{package}': {e}"

# Help text
def help_text():
    """Display available commands."""
    return """
Welcome to your custom terminal! Here are the commands you can use:

File Operations:
- see [path]           : List files in a directory
- name-it [old] [new]  : Rename a file
- clean [file]         : Delete a file

System Operations:
- watch                : Show system stats
- apps                 : List running processes

Network Operations:
- check [host]         : Ping a host
- find-ip [domain]     : Resolve a domain to IP

Password Management:
- secure-me [length]   : Generate a random password

Python Package Management:
- get-it [package]     : Install a Python package
- update-it [package]  : Update a Python package
- drop-it [package]    : Remove a Python package

Node Package Management:
- add-it [package]     : Install a Node package
- upgrade-it [package] : Update a Node package
- rm-it [package]      : Remove a Node package

Miscellaneous:
- clear                : Clear the terminal screen
- quit                 : Exit the terminal
"""

# Main REPL loop
def main():
    print("Starting Custom Terminal (type 'help' for commands)...")
    while True:
        command = input(">> ").strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "quit":
            print("Exiting Custom Terminal. Goodbye!")
            break
        elif cmd == "help":
            print(help_text())
        elif cmd == "clear":
            clear_terminal()
        elif cmd == "secure-me":
            try:
                length = int(args[0]) if args else 12
                print(generate_password(length))
            except (ValueError, IndexError):
                print("Error: Please provide a valid numeric length for the password.")
        elif cmd == "see":
            path = args[0] if args else "."
            print(list_files(path))
        elif cmd == "name-it":
            if len(args) != 2:
                print("Usage: name-it [old] [new]")
            else:
                print(rename_file(args[0], args[1]))
        elif cmd == "clean":
            if len(args) != 1:
                print("Usage: clean [file]")
            else:
                print(delete_file(args[0]))
        elif cmd == "watch":
            print(system_stats())
        elif cmd == "apps":
            print(list_processes())
        elif cmd == "check":
            if len(args) != 1:
                print("Usage: check [host]")
            else:
                print(ping_host(args[0]))
        elif cmd == "find-ip":
            if len(args) != 1:
                print("Usage: find-ip [domain]")
            else:
                print(resolve_domain(args[0]))
        elif cmd == "get-it":
            if len(args) != 1:
                print("Usage: get-it [package]")
            else:
                print(install_python_package(args[0]))
        elif cmd == "update-it":
            if len(args) != 1:
                print("Usage: update-it [package]")
            else:
                print(update_python_package(args[0]))
        elif cmd == "drop-it":
            if len(args) != 1:
                print("Usage: drop-it [package]")
            else:
                print(remove_python_package(args[0]))
        elif cmd == "add-it":
            if len(args) != 1:
                print("Usage: add-it [package]")
            else:
                print(install_node_package(args[0]))
        elif cmd == "upgrade-it":
            if len(args) != 1:
                print("Usage: upgrade-it [package]")
            else:
                print(update_node_package(args[0]))
        elif cmd == "rm-it":
            if len(args) != 1:
                print("Usage: rm-it [package]")
            else:
                print(remove_node_package(args[0]))
        else:
            print(f"Unknown command: {cmd}. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
