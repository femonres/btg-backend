class FundCategory:
    VALID_CATEGORIES = {"FPV", "FIC"}

    def __init__(self, category: str):
        self.category = self.validate_category(category)

    @staticmethod
    def validate_category(category: str) -> str:
        if category not in FundCategory.VALID_CATEGORIES:
            raise ValueError(f"Categoría no válida: {category}. Las permitidas son: {FundCategory.VALID_CATEGORIES}.")
        return category