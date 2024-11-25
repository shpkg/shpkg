import click
import requests
import subprocess
import json
import os

BASE_URL = "https://raw.githubusercontent.com/shpkg/repo/refs/heads/main/install/"
PACKAGES_FILE = os.path.expanduser("~/.shpkg/packages.json")

def install(package_name):
    """Install a package."""
    package_url = f"{BASE_URL}{package_name}.sh"
    click.echo(f"Fetching the package installer from {package_url}...")
    
    response = requests.get(package_url)
    if response.status_code == 404:
        click.echo("Error: Package not found (404).", err=True)
        return 1

    script_path = f"/tmp/shpkg/installer/{package_name}.sh"
    os.makedirs(os.path.dirname(script_path), exist_ok=True)
    with open(script_path, "w") as script_file:
        script_file.write(response.text)

    subprocess.run(["chmod", "+x", script_path], check=True)
    click.echo(f"Installing {package_name}...")
    result = subprocess.run([script_path], capture_output=True)

    if result.returncode == 0:
        click.echo(f"Package {package_name} installed successfully.")
        if os.path.exists(PACKAGES_FILE):
            with open(PACKAGES_FILE, "r") as f:
                packages = json.load(f)
        else:
            packages = []

        if package_name not in packages:
            packages.append(package_name)
            with open(PACKAGES_FILE, "w") as f:
                json.dump(packages, f, indent=4)
    else:
        click.echo(f"Error: Installation of {package_name} failed.", err=True)
        return 1

    return 0
