import click
import json
import os

PACKAGES_FILE = os.path.expanduser("~/.shpkg/packages.json")

@click.command()
def list_pkg():
    """List installed packages."""
    if os.path.exists(PACKAGES_FILE):
        with open(PACKAGES_FILE, "r") as f:
            packages = json.load(f)
        if packages:
            click.echo("Installed packages:")
            for package in packages:
                click.echo(f"- {package}")
        else:
            click.echo("No packages installed.")
    else:
        click.echo("No packages installed.")