import json
from InstagramAPI import InstagramAPI


def getTotalFollowers(api, user_id):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


def followersToJSON(username, password, json_file='followers.json'):
    api = InstagramAPI(username, password)
    api.login()
    user_id = api.username_id
    followers = getTotalFollowers(api, user_id)
    with open(json_file, 'w') as outfile:
        json.dump(followers, outfile)
    print('Number of followers:', len(followers))


def followingToJSON(username, password, json_file='following.json'):
    API = InstagramAPI(username, password)
    API.login()
    user_id = API.username_id
    following = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''
        _ = API.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(API.LastJson.get('users', []))
        next_max_id = API.LastJson.get('next_max_id', '')
    with open(json_file, 'w') as outfile:
        json.dump(following, outfile)
    print('Number of following:', len(following))


def createCSVfromJSON(json_file, csv_file):
    with open(json_file) as f:
        data = json.load(f)
    s = []
    num = 1
    for i in data:
        print(i['full_name'], i['username'])
        line = '{};{}\n'.format(i['full_name'], i['username'])
        s.append(line)
        num = num+1

    with open(csv_file, 'w') as f:
        for line in s:
            f.write(line)


def diffFollowsToCSV(following_json='following.json', followers_json='followers.json', out_diff_csv='diff-follow.csv'):
    with open(following_json) as f:
        following = json.load(f)
    with open(followers_json) as f:
        followers = json.load(f)
    
    followers_list = []
    for i in followers:
        line = '{};{}\n'.format(i['full_name'], i['username'])
        followers_list.append(line)
    print('Follow me: {}'.format(len(followers_list)))

    diff_list = []
    following_list = []
    for i in following:
        line = '{};{}\n'.format(i['full_name'], i['username'])
        following_list.append(line)
        if line not in followers_list:
            diff_list.append(line)
    print('I follow: {}'.format(len(following_list)))
    print('Diff: {}'.format(len(diff_list)))

    with open(out_diff_csv, 'w') as f:
        for line in diff_list:
            f.write(line)