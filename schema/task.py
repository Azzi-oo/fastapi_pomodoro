from pydantic import BaseModel, Field, model_validator


class Task(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int = Field(alias='cats')
    
    
    # @model_validator(mode="after")
    # @classmethod
    # def check_name_or_pomodoro_count_is_not_none(self):
    #     print(self)
    #     return self