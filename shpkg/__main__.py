import click

from .install import install
from .remove import remove
from .update import update
from .update_all import update_all
from .list_pkg import list_pkg

VERSION = "0.1.2"

@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the version and exit.")
@click.pass_context # i have no idea what this is
def main(ctx, version):
    """shpkg - packaging made fun and easy"""
    if version:
        click.echo(f"shpkg version {VERSION}")
        ctx.exit(0)

    if ctx.invoked_subcommand is None:
        click.echo("Error: Missing command. Use --help to see available options.")
        ctx.exit(1)

# Subcommand: install
@main.command()
def i():
    install()

# Subcommand: uninstall
@main.command()
def x():
    remove()

# Subcommand: list
@main.command()
def l():
    list_pkg()

# Subcommand: update
@main.command()
def u():
    update()

# Subcommand: update all
@main.command()
def ua():
    update_all()

if __name__ == "__main__":
    main()