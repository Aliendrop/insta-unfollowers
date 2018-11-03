import fire

DEBUG = False

if DEBUG:
    from config_dev import *
else:
    from config import *

from utils import *


class Main(object):

    def test(self):
        return 'Test!'

    def save_following(self):
        followingToJSON(username, password)

    def save_followers(self):
        followersToJSON(username, password)

    def diff_follows(self):
        diffFollowsToCSV()

    def run(self):
        self.save_following()
        self.save_followers()
        self.diff_follows()

if __name__ == '__main__':
    fire.Fire(Main)
