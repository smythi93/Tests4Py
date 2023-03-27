The bug in fastapi 2 does occur whenever a dependency of a websocket is overriden, i.e., the `dependency_overrides` 
attribute of the app contains an entry for the websocket that should be invoked. The buggy version does not override
the dependency.