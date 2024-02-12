import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="pdf_coordinates_learner",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="pdf_coordinates_learner_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from pdf_coordinates_learner.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export pdf_coordinates_learner_KEY=value
export pdf_coordinates_learner_KEY="@int 42"
export pdf_coordinates_learner_KEY="@jinja {{ this.db.uri }}"
export pdf_coordinates_learner_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
pdf_coordinates_learner_ENV=production pdf_coordinates_learner run
```

Read more on https://dynaconf.com
"""
