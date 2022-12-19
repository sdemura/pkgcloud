#!/usr/bin/env python3

import requests
import os
import json

PACKAGECLOUD_TOKEN = os.environ.get("PACKAGECLOUD_TOKEN")

r = requests.get(f"https://{PACKAGECLOUD_TOKEN}:@packagecloud.io/api/v1/distributions.json")
r.raise_for_status()

j = r.json()



try:
    for k in j.keys():
        package_type = j[k]

        for distros in package_type:
            distro_name = distros["index_name"]
            versions = distros["versions"]

            for version in versions:
                v = version["index_name"]
                id = version["id"]
                distro = f'"{distro_name}/{v}": {id},'
                print(distro)
except:
    pass



