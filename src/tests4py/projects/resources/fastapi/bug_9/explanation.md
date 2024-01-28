The bug in fastapi 9 does occur whenever the default for a parameter of a handler is set to `Body`, with the 
`media_type` set to an arbitrary string and `embed` is set to `True`. The bug does not occur when the `media_type` is 
set to `application/json`. The bug shows when retrieving the `openapi` schema, where the `media_type` shows as 
`application/json` instead of the provided `media_type`.