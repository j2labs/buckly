#!/usr/bin/env python


import pymongo
from brubeck.models import User


###
### Database Connection Handling
###

def init_db_conn(**kwargs):
    dbc = pymongo.Connection(**kwargs)
    db_conn = dbc.linksurf
    return db_conn


def end_request(db_conn):
    return db_conn.end_request()


###
### Short ID generation
###

SHORTID_COLLECTION = 'shortids'

def gen_next_shortid(db):
    """Gets the latest id used from the database and returns the matching
    counter value
    """
    db_coll = db[SHORTID_COLLECTION]
    
    shortid = db_coll.find_and_modify(query={'counter_id': 'buckly'},
                                      update={'$inc': {'count': 1}},
                                      new=True, upsert=True)
    return shortid['count']


###
### ListItem Handling
###

SHORTLINK_COLLECTION = 'shortlinks'

def load_shortlink(db, short_id):
    """Loads a user document from MongoDB.
    """
    query_dict = dict(short_id=short_id)
    query_set = db[SHORTLINK_COLLECTION].find_one(query_dict)
    return query_set


def save_shortlink(db, shortlink):
    """Loads a user document from MongoDB.
    """
    db_coll = db[SHORTLINK_COLLECTION]
    
    shortlink_doc = shortlink.to_python()
    iid = db_coll.insert(shortlink_doc)
    shortlink.id = iid

    db_coll.ensure_index([('short_id', pymongo.ASCENDING)])

    return iid
