The bug in fastapi 1 does occur whenever the jsonable_encoder function was used with the keyword `exclude_defaults`. The
keyword is undefined in the buggy version.