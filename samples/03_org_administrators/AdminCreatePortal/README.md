# Introduction
This folder Python and batch scripts that will help populate a fresh portal
with users, groups and content for each of the user accounts. You can find the
list of users and groups in the corresponding `users.csv` and `groups.csv`
files.

## Steps
 1. Run `populate_portal.bat` which execute the Python scripts in sequence
 and creates users, groups and content.
 2. Optionally run `clean_up.bat` to erase all users, groups and content

# Sample outputs below
## Running clean_up.py
`clean_up.py` accepts the credentials as command line args. Inquiring help
on the file returns the following:

```
E:\code>python cleanup.py --help
usage: cleanup.py [-h] [-u USER] [-p PASSWORD] url

positional arguments:
  url                   Portal url of the form:
                        https://portalname.domain.com/webadaptor

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Administrator username
  -p PASSWORD, --password PASSWORD
                        Administrator password
```

Running it with credentials returns the following
```
E:\code>python cleanup.py https://ESRIwebgis.webgistesting.net/portal -u admin -p xxxxxx
RUNNING CLEANUP
---------------

Deleting groups
---------------
Deleting  Featured Maps and Apps  ##  success

Deleting user content
---------------------
User :  admin # skipped
User :  esri_boundaries # skipped
User :  esri_demographics # skipped
User :  esri_livingatlas # skipped
User :  esri_nav # skipped

Deleting users
--------------
Deleting  system_publisher  ##  success

 All clean

```

## Running create_groups.py
Similar to `clean_up.py`, `create_groups.py` also accepts command line args.
Running it with valid credentials prints the following output:

```
E:\code>python create_groups.py https://ESRIwebgis.webgistesting.net/portal -u admin -p xxxxx
CREATING GROUPS
 Creating group:  Basemaps  ##  success
 Creating group:  Central Services  ##  success
 Creating group:  Compliance  ##  success
 Creating group:  Customer Service, Finance, Billing and Accounting  ##  success
 Creating group:  Demographic Content  ##  success

```

### Running create_users.py
`create_users.py` will create users on the portal and add them to appropriate
groups specified in the `users.csv` file. Running it with valid credentials
reports below, truncated for brevity:

```
E:\code>python create_users.py https://ESRIwebgis.webgistesting.net/portal -u admin -p xxxxxxx
CREATING USER ACCOUNTS
Creating user:  smith.collins ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  johnson.stewart ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  williams.sanchez ## success  ##
         Adding to groups:  # Basemaps #  Central Services #
...
```

### Running publish_content.py
This script will publish feature layers, web map with those layers and
assign it to each of the user. Running it will print the following output,
truncated for brevity:

```
E:\code>python publish_content.py https://ESRIwebgis.webgistesting.net/portal -u admin -p xxxxx
Publishing  .\user_content\KS.csv # webmaps ## success. Assigning to:   #  smith.collins
Publishing  .\user_content\NV.csv # webmaps ## success. Assigning to:   #  johnson.stewart
Publishing  .\user_content\IN.csv # webmaps ## success. Assigning to:   #  williams.sanchez
Publishing  .\user_content\NC.csv # webmaps ## success. Assigning to:   #  jones.morris
....
```