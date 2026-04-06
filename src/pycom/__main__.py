import sys
from pycom.server import serve


def main():
    arguments = sys.argv[1:]

    if "--serve" in arguments:
        print("starting server...")
        serve(5400)
    else:
        print("client")


if __name__ == "__main__":
    main()
