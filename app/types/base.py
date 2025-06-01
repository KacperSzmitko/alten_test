from pydantic import BaseModel
# from pydantic import BaseModel, ConfigDict, model_validator
# from pydantic.alias_generators import to_camel, to_snake


class BaseInputModel(BaseModel): ...


class BaseOutputModel(BaseModel): ...
