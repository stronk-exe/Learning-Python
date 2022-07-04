import sys

def defangin(address):
    address = address.split(".")
    return "[.]".join(address)

def main():
    if len(sys.argv) != 2:
        print('Invalid input')
        exit(1)
    print(defangin(sys.argv[1]))

main()
