import click

from .install import install
from .remove import remove
from .update import update
from .update_all import update_all
from .list_pkg import list_pkg

VERSION = "0.2.0"

@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the version and exit.")
@click.pass_context
def main(ctx, version):
    """shpkg - packaging made fun and easy."""
    if version:
        click.echo(f"shpkg version {VERSION}")
        ctx.exit(0)

    if ctx.invoked_subcommand is None:
        click.echo("Error: Missing command. Use --help to see available options.", err=True)
        ctx.exit(1)

# Subcommand: install
@main.command()
@click.argument("package_name", required=True)
def i(package_name):
    install(package_name)

# Subcommand: uninstall
@main.command()
@click.argument("package_name", required=True)
def x(package_name):
    remove(package_name)

# Subcommand: list
@main.command()
def l():
    list_pkg()

# Subcommand: update
@main.command()
@click.argument("package_name", required=True)
def u(package_name):
    update(package_name)

# Subcommand: update all
@main.command()
def ua():
    update_all()

if __name__ == "__main__":
    main()
