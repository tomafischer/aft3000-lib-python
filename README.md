# Office365-aft-Python
Welcome to my utility functions to access Office 365 applications.

Currently implemented:
 - Sharepoint365 with MFA enabled 

## Sharepoint 365 
Sharepoint can be tricky to access via code when you have MFA enabled. Here is a list of links which helped me:

- [office365.sharepoint libraries](
https://github.com/vgrem/Office365-REST-Python-Client)
- [fitler query demo](
https://github.com/vgrem/Office365-REST-Python-Client/issues/100)
- https://social.technet.microsoft.com/wiki/contents/articles/35796.sharepoint-2013-using-rest-api-for-selecting-filtering-sorting-and-pagination-in-sharepoint-list.aspx
## Accessing Sharepoint native
https://martinnoah.com/sharepoint-rest-api-with-python.html#.Yji51JrMKj8

endpoint: 

/_api/web/lists/GetByTitle('BigLis')/items?$filter=(ProjectNo eq '123' or ProjectNo eq '141' or ProjectNo eq '154')

https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service?tabs=csom

### Service Prinicipal Authentication
https://code2care.org/sharepoint/how-to-access-sharepoint-online-data-using-postman-rest-graph-api-oauth


# Tests
The folder `tests` has Unit and Integration Tests.
Originally the tests where under examples, but after while I realized that switching the examples to unit tests adds more values.


## Run Tests
```bash
# shows all makers
pytest --markers 

# run sharepint tests only
# to be able to run the sharepoint test you have to 
# - set site_url
# - set your secret key in conftest.py
# - create a test list on sharepoint called "Unittests"

# _app_principal = {    
#    'client_id': '',
#    'client_secret': '',
#    }
# _site_url = 'https://my.sharepoint.com/teams/test'

pytest -m sp

# run integration tests 
# you might have to unqoute the skip marker to active them. Be aware they actually write/delete test records.
pytest -m integration
```