The bug in fastapi 5 does occur when a model A inherits from another model B and a model C contains a field of type B.
When responding with model C fastapi includes the fields of model A even though it should only contain information
about model B.