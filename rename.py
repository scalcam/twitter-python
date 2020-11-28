import json
import os
from datetime import datetime

def rename():

    try:
        with open('followers_old.json') as old:
            data_old = json.load(old)
    
        date_str = data_old['date']
        print("datestr:", date_str)
    except:
        print("followers_old.json[\'date\'] does not exist")

    try:
        os.rename(r'followers_old.json',r'followers_' + str(date_str) + '.json')
    except Exception as e:
        print("followers_old.json does not exist", e)

    try:
        os.rename(r'followers.json',r'followers_old.json')
    except Exception as e:
        print("followers.json does not exist", e)


def main():
    rename()

if __name__ == "__main__":
    # calling main function
    main()