import click
import requests
import subprocess
import json
import os

BASE_URL = "https://raw.githubusercontent.com/shpkg/repo/refs/heads/main/uninstall/"
PACKAGES_FILE = os.path.expanduser("~/.shpkg/packages.json")

def remove(package_name):
    """Remove a package."""
    # Construct the URL
    package_url = f"{BASE_URL}{package_name}.sh"
    
    # Fetch the package script
    click.echo(f"Fetching the package uninstaller from {package_url}...")
    response = requests.get(package_url)

    if response.status_code == 404:
        click.echo("Error: Package not found (404).", err=True)
        return 1

    # Save the script to a temporary file
    script_path = f"/tmp/shpkg/uninstaller/{package_name}.sh"
    os.makedirs(os.path.dirname(script_path), exist_ok=True)
    with open(script_path, "w") as script_file:
        script_file.write(response.text)

    # Make the script executable
    subprocess.run(["chmod", "+x", script_path], check=True)

    # Execute the script
    click.echo(f"Removing {package_name}...")
    result = subprocess.run([script_path], capture_output=True)

    if result.returncode == 0:
        click.echo(f"Package {package_name} removed successfully.")
        # Update the packages JSON file
        if os.path.exists(PACKAGES_FILE):
            with open(PACKAGES_FILE, "r") as f:
                packages = json.load(f)
        else:
            packages = []

        if package_name in packages:
            packages.remove(package_name)
            with open(PACKAGES_FILE, "w") as f:
                json.dump(packages, f, indent=4)
    else:
        click.echo(f"Error: Removal of {package_name} failed.", err=True)
        return 1

    return 0