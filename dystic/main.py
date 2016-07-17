import sys
import os
import yaml
import argparse
import builder

config = {
    'ROOT_DIR_PATH': os.path.abspath(os.path.dirname(sys.argv[1]))
}

def build(folder):
    builder.Builder().build_dir(folder)

def cli():
    parser = argparse.ArgumentParser(
    description='Simple dynamically static blog generator.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b', '--build', dest='folder', help="build the specified folder.")
    args = parser.parse_args()
    if args.folder:
    	build(args.folder)
    else:
    	raise SystemExit('Please specify a directory.')

def main():
    # with open('_config.yml', 'r') as f:
    #     config.update(yaml.load(f))
    cli()


if __name__ == '__main__':
    main()
