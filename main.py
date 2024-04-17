import json

from cli.cli import parse_args
from module.config.config import Config
from module.instance.instance import Instance


def instance():
    config = Config()
    instance_id = config.get_config().instance.id
    instance = Instance(instance_id)
    return instance


if __name__ == "__main__":
    args = parse_args()
    if args.main_operation == "get":
        if args.action_get_type == "config":
            config = Config()
            print(config.get_pretty_config())
        if args.action_get_type == "instance":
            rsp = instance().describe()
            json_formatted_str = json.dumps(rsp, indent=2)
            print(json_formatted_str)
    if args.main_operation == "start":
        rsp = instance().start()
        print(rsp)
        ip = instance().instance_ip()
        print(f"Instance IP: {ip}")

    if args.main_operation == "stop":
        rsp = instance().stop()
        print(rsp)
