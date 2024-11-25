import click
import json
import os
import subprocess

PACKAGES_FILE = os.path.expanduser("~/.shpkg/packages.json")

@click.command()
def update_all():
    """Update all installed packages."""
    if os.path.exists(PACKAGES_FILE):
        with open(PACKAGES_FILE, "r") as f:
            packages = json.load(f)
        
        if packages:
            click.echo("Updating all installed packages...")
            for package in packages:
                click.echo(f"Updating {package}...")
                result = subprocess.run(["python", "-m", "shpkg", "u", package], capture_output=True)
                if result.returncode == 0:
                    click.echo(f"Package {package} updated successfully.")
                else:
                    click.echo(f"Error: Update of {package} failed.", err=True)
        else:
            click.echo("No packages installed.")
    else:
        click.echo("No packages installed.")