#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Proposed file that holds the backend state.
State should probably be a dict.
Anything that must be preserved between runtimes must be a member of this dict

On first load, the state will be read from DB. This makes it (sort of) a buffer
This could be useful because it saves a ton of DB queries. But on the flip-side
it means we will bloat memory usage on very large DBs. We'll see how it goes.
If a better solution arises, We'll use it.

for now, until work on a DB starts, state will read to and from a json file
The file will be on this path: backend/db.json
To avoid lots of conflicts, the file will NOT be versioned on git.
'''
import json



_state = {}

try:
    with open("db.json", "r") as db:
        _state = json.load(db)
except FileNotFoundError:
    print("db.json doesn't exist. Creating...")
    open("db.json", "w").close()

def write_state():
    with open("db.json", "w") as db:
    json.dump(_state, db)

