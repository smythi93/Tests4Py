The bug in fastapi 7 does occur whenever the except handler response contains an object that is not serializable. This
could be the case, when the error correspond to a constraint like `gt=Decimal(0.0)`. Since the type `Decimal`is not
serializable but the response tries to add it without validation or the sanitization of ot, an error is raised. 