import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-if", "--iface", help="Net interface")
    parser.add_argument("-lg", "--log_file", help="Log file")
    parser.add_argument("-from", "--path_folder", help="Folder with path files")
    return parser.parse_args()