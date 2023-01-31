The bug in fastapi 6 does occur when a body, in particular a form, uses a python types `list`, `set`, or `tuple` to 
describe the fields. Since the field has not the correct shape and the python types are ignored the api response
with the http code 422.