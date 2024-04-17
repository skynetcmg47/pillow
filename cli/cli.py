import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Pillow CLI")
    subparsers = parser.add_subparsers(dest="main_operation", help="Main Operation")
    action_get = subparsers.add_parser("get", help="Get configuration")
    action_get.add_argument(
        "action_get_type", help="Entity to get", choices=["config", "instance"]
    )

    subparsers.add_parser("start", help="Connect to instance")
    subparsers.add_parser("stop", help="Disconnect to instance")

    return parser.parse_args()
