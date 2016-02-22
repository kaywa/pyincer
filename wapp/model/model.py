# -*- coding: utf-8 -*-

from pymongo import  MongoClient

class SocialData:

    def __init__(self):
        self._client = MongoClient("mongodb://localhost:27019")
        self._social = self._client['social']
        pass

    def add_buddy(self, id, name, age):
        self._social.buddy.insert_one('{}')
        pass

    def remove_buddy(self):
        pass

    def update_buddy(self):
        pass

    def get_buddies(self):
        coll = self._social['dataset']
        pass

    def get_dynamics(self):
        pass

    def get_dynamics(self, buddy_id_list):
        pass

    def add_dynamics(self):
        pass

if __name__ == '__main__':
    dao = SocialData()
    dao.get_buddies()