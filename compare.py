import json

def compare():
    with open('followers_old.json') as old:
        data_old = json.load(old)
    with open('followers.json') as current:
        data_current = json.load(current)


    for follower in data_old['followers']:
        if follower in data_current['followers']:
            print("user still following: ", follower['id'])
        else:
            print("**missing follower**: ", follower["id"], " name:", follower['name'], " @:", follower["screen_name"])

def main():
    compare()

if __name__ == "__main__":
    # calling main function
    main()