import argparse


class CommandLineParser:
    def __init__(self):
        self.file_path = None

    def parse(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", dest="file_path", required=True, help="Path to the file to be converted.")
        args = parser.parse_args()
        self.file_path = args.file_path
