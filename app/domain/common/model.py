from pydantic import BaseModel as PydanticBaseModel, Extra, ValidationError, ConfigDict


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
        except ValidationError as error:
            raise error
