import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",help="Specify your URL")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
	args = parse_args()
	url = args.url
	print(url)