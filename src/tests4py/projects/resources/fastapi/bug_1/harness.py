import argparse

# noinspection PyUnresolvedReferences
from fastapi.encoders import jsonable_encoder

# noinspection PyUnresolvedReferences
from pydantic import BaseModel

try:
    # noinspection PyUnresolvedReferences
    from pydantic import Field
except ImportError:
    # noinspection PyUnresolvedReferences
    from pydantic import Schema as Field

if __name__ == "__main__":
    arguments = argparse.ArgumentParser()

    arguments.add_argument("-o", dest="obj")  # obj
    arguments.add_argument("-i", dest="include", default=None)  # include
    arguments.add_argument("-e", dest="exclude", default=None)  # exclude
    arguments.add_argument(
        "-a", dest="by_alias", default=None, action="store_true"
    )  # by_alias
    arguments.add_argument(
        "-s", dest="skip_defaults", default=None, action="store_true"
    )  # skip_defaults
    arguments.add_argument(
        "-u", dest="exclude_unset", default=None, action="store_true"
    )  # exclude_unset
    arguments.add_argument(
        "-d", dest="exclude_defaults", default=None, action="store_true"
    )  # exclude_defaults
    arguments.add_argument(
        "-ni", dest="include_none", default=None, action="store_true"
    )  # include_none
    arguments.add_argument(
        "-ne", dest="exclude_none", default=None, action="store_true"
    )  # include_none
    arguments.add_argument("-c", dest="custom_encoder", default=None)  # custom_encoder
    arguments.add_argument(
        "-q", dest="sqlalchemy_safe", default=None, action="store_true"
    )  # sqlalchemy_safe

    args = arguments.parse_args()

    class Model(BaseModel):
        foo: str = Field(..., alias="foo")
        bar: str = "bar"
        bla: str = "bla"

        class Config:
            use_enum_values = True

    parameters = dict()
    if args.obj is not None:
        parameters["obj"] = eval(args.obj)
    if args.include is not None:
        parameters["exclude"] = set(args.include.split(","))
    if args.exclude is not None:
        parameters["exclude"] = set(args.exclude.split(","))
    if args.by_alias is not None:
        parameters["by_alias"] = False
    if args.skip_defaults is not None:
        parameters["skip_defaults"] = True
    if args.exclude_unset is not None:
        parameters["exclude_unset"] = True
    if args.exclude_defaults is not None:
        parameters["exclude_defaults"] = True
    if args.include_none is not None:
        parameters["include_none"] = False
    if args.exclude_none is not None:
        parameters["exclude_none"] = True
    if args.custom_encoder is not None:
        parameters["custom_encoder"] = eval(args.custom_encoder)
    if args.sqlalchemy_safe is not None:
        parameters["sqlalchemy_safe"] = False

    jsonable_encoder(**parameters)
