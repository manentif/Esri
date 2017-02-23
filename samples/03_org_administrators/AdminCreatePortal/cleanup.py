# Script to clean up the users, content and groups created for demo

from arcgis.gis import *
import argparse

#region read cmd line args
parser = argparse.ArgumentParser()
parser.add_argument('url', help='Portal url of the form: https://portalname.domain.com/webadaptor')
parser.add_argument('-u','--user', help='Administrator username', default='admin')
parser.add_argument('-p','--password', help='Administrator password', default='x]984<ngb3!')

args = parser.parse_args()
#endregion

print("RUNNING CLEANUP")
print("---------------")

gis = GIS(args.url, args.user, args.password)

# region remove groups
group_list = gis.groups.search("owner:" + args.user)
print("")
print("Deleting groups")
print("---------------")

for group in group_list:
    try:
        print("Deleting ", group.title, end= "  ##  ")
        group.delete()
        print("success")
    except Exception as group_del_ex:
        print("Error deleting : " , str(group_del_ex))
# endregion

#region remove content for each user
print("")
print("Deleting user content")
print("---------------------")
user_list = gis.users.search("")
try:
    for user in user_list:
        print('User : ', user.username, end=" # ")
        if user.fullName in ['Administrator', 'Esri', 'Esri Navigation']:
            print('skipped')
            continue

        user_content = gis.content.search('owner:{0}'.format(user.username))
        for item in user_content:
            print('Deleting : ', item.title, end = " # ")
            delete_status = item.delete()
            print(str(delete_status), end = " | ")
        print('empty')

except Exception as content_del_ex:
    print(str('content_del_ex'))
#endregion

# region remove users
user_list = gis.users.search()
print("")
print("Deleting users")
print("--------------")

for user in user_list:
    if user.username == "admin" or user.username.startswith("esri_") or user.username.startswith("AVWORLD"):
        continue
    else:
        print("Deleting ", user.username, end = "  ##  ")
        user.delete()
        print("success")
# endregion
print("\n All clean")
