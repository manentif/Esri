import sys

#
#  Update the Path to set the test area
sys.path.insert(0, r"C:\SVN\geosaurus_master\src")


#
# Prints all messages out to Debug Window
#
import logging
import datetime as _dt

root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter(' -  -  - ')
# handler.setFormatter(formatter)
root.addHandler(handler)

import arcgis
from arcgis.gis import GIS
import pandas as pd

print(arcgis.__file__)
print(arcgis.__version__)

import urllib.request


def handle_fiddler():
    proxies = urllib.request.getproxies()
    if proxies == {}:
        proxies = None
    else:
        proxies['https'] = proxies['https'].replace("https", "http")
    return proxies


proxies = handle_fiddler()

if __name__ == "__main__":
    gis = GIS(
        profile='your_online_profile', proxy=proxies, verify_cert=False
    )

    um = gis.users
    users = um.org_search("*", exclude=True)
    rows = []
    then = _dt.datetime.now() - _dt.timedelta(days=365)
    cols = ["USERNAME", "DISABLED", "LASTLOGIN", "OLDERTHANYEAR"]
    for user in users:
        if user.lastLogin == -1:
            rows.append(
                [
                    user.username,
                    user.disabled,
                    None,
                    True,
                ]
            )
        else:
            rows.append(
                [
                    user.username,
                    user.disabled,
                    _dt.datetime.fromtimestamp(user.lastLogin / 1000),
                    _dt.datetime.fromtimestamp(user.lastLogin / 1000)
                    <= then,
                ]
            )
    df = pd.DataFrame(data=rows, columns=cols)
    df.to_csv(r"./check_user_status.csv", index=False)
