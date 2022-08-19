from zipfile import ZipFile
import argparse

# parsing arguments
parser = argparse.ArgumentParser(
    description='\nZIP Brute Force \n Usage: python3 zipbruteforcer.py -z <zipfile.zip> -p <passwordfile.txt>')
parser.add_argument('-z', '--zipfile',
                    help='ZIP file to be cracked', required=True)
parser.add_argument('-p', '--passwordfile',
                    help='Password file', required=True)
args = parser.parse_args()

try:
    zipfile = ZipFile(args.zipfile)
    passwordfile = args.passwordfile
    foundpass = ''
except Exception as e:
    print(e)
    print(parser.print_help())
    exit(1)

with open(passwordfile, 'r') as f:
    for line in f:
        password = line.strip('\n')
        password = password.encode('utf-8')
        try:
            zipfile.extractall(pwd=password)
            foundpass = password
            break
        except Exception as e:
            pass
    if foundpass:
        print('Password found: {}'.format(foundpass))
    else:
        print('Password not found \n Try another password file')
    zipfile.close()