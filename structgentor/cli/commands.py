import argparse
import sys

from structgentor.core import save_structure, generate_from_layout
from structgentor.utils import print, cli_help

# from structgentor.utils.utils import cli_help
# from structgentor.utils.printer import print

def main():
    parser = argparse.ArgumentParser(
        description="Structgentor - Project Structure Generator",
        add_help=False  # Disable default help for better error handling
    )

    parser.add_argument(
        "command",
        nargs="?",
        help="Available commands: init, freeze, help"
    )
    parser.add_argument(
        "project_name",
        nargs="?",
        default=".",
        help="(Optional) Name of the project directory. Defaults to current directory."
    )

    args = parser.parse_args()

    if not args.command:
        print("No command provided! Use 'structgentor help' for available commands.\n", category="warning")
        return

    if args.command == "init":
        generate_from_layout(output_dir=args.project_name)
    elif args.command == "freeze":
        save_structure()
    elif args.command == "help":
        cli_help()
    else:
        print(f"Unknown command '{args.command}'. Use 'structgentor help' for a list of available commands.\n", category="error")

if __name__ == "__main__":
    main()
