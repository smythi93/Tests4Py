The bug in fastapi 3 does occur whenever a model has an `alias` and the model gets serialized with `serialize_response`,
for instance, in case of a `get` response.