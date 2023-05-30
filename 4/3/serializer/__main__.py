from serializer.factory import Factory
import argparse
import configparser


def parse_config_file(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    if "config" in config:
        config_section = config["config"]
        if all(param in config_section for param in ["source", "source_format", "destination", "destination_format"]):
            return (
                config_section["source"],
                config_section["source_format"],
                config_section["destination"],
                config_section["destination_format"],
            )

    return None


def parse_cli():
    parser = argparse.ArgumentParser(description="JSON / XML serializer")
    parser.add_argument("source", type=str, help="Path to source file")
    parser.add_argument("source_format", type=str, choices=["json", "xml"], help="Format of source file")
    parser.add_argument("destination", type=str, help="Path to destination file")
    parser.add_argument("destination_format", type=str, choices=["json", "xml"], help="Format of destination file")
    args = parser.parse_args()

    return args.source, args.source_format, args.destination, args.destination_format


def main():
    config = "config.ini"
    config_values = parse_config_file(config)

    source, source_format, destination, destination_format = config_values if config_values else parse_cli()

    source_serializer = Factory.get_parser(source_format)
    destination_serializer = Factory.get_parser(destination_format)

    with open(source, "r", encoding="utf8") as file:
        obj = source_serializer.load(file)

    with open(destination, "w", encoding="utf8") as file:
        destination_serializer.dump(obj, file)


if __name__ == "__main__":
    main()
