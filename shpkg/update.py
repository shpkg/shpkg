import click
import requests
import subprocess

BASE_URL = "https://raw.githubusercontent.com/shpkg/repo/refs/heads/main/install/"

@click.command()
@click.argument("package_name", required=True)
def update(package_name):
    """Update a package."""
    # Construct the URL
    package_url = f"{BASE_URL}{package_name}.sh"
    
    # Fetch the package script
    click.echo(f"Fetching the package installer from {package_url}...")
    response = requests.get(package_url)

    if response.status_code == 404:
        click.echo("Error: Package not found (404).", err=True)
        return 1

    # Save the script to a temporary file
    script_path = f"/tmp/shpkg/update/{package_name}.sh"
    with open(script_path, "w") as script_file:
        script_file.write(response.text)

    # Make the script executable
    subprocess.run(["chmod", "+x", script_path], check=True)

    # Execute the script
    click.echo(f"Updating {package_name}...")
    result = subprocess.run([script_path], capture_output=True)

    if result.returncode == 0:
        click.echo(f"Package {package_name} updated successfully.")
    else:
        click.echo(f"Error: Update of {package_name} failed.", err=True)
        return 1

    return 0
