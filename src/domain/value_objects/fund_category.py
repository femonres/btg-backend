from pydantic import BaseModel, field_validator

class FundCategory(BaseModel):
    category: str

    @field_validator('category')
    def validate_category(cls, v):
        valid_categories = {"FPV", "FIC"}
        if v not in valid_categories:
            raise ValueError(f"Categoría no válida: {v}. las permitidas son: {valid_categories}.")
        return v
