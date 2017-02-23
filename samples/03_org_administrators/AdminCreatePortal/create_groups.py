# Script to read list of groups from a csv and create them on the portal.
from arcgis.gis import *
import argparse
import csv

#region read cmd line args
parser = argparse.ArgumentParser()
parser.add_argument('url', help='Portal url of the form: https://portalname.domain.com/webadaptor')
parser.add_argument('-u','--user', help='Administrator username', default='admin')
parser.add_argument('-p','--password', help='Administrator password', default='x]984<ngb3!')

args = parser.parse_args()
#endregion

print("CREATING GROUPS")

# connect to gis
gis = GIS(args.url, args.user, args.password)

with open("groups.csv", 'r') as groups_csv:
    groups = csv.DictReader(groups_csv)
    for group in groups:
        try:
            print(" Creating group: ", group['title'], end="  ##  ")
            result = gis.groups.create_from_dict(group)
            if result:
                print("success")

        except Exception as create_ex:
            print("Error... ", str(create_ex))
