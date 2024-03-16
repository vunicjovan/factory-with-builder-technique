from src.enumerations.base.base_enum import BaseEnum
from src.enumerations.brand import Brand


class Model(BaseEnum):
    # BMW models
    SERIES_3 = "Series 3"
    SERIES_5 = "Series 5"
    SERIES_7 = "Series 7"
    ...  # Placeholder for additional BMW models

    # Audi models
    A1 = "A1"
    A4 = "A4"
    TT = "TT"
    ...  # Placeholder for additional Audi models

    # Mercedes-Benz models
    C_CLASS = "C Class"
    E_CLASS = "E Class"
    AMG = "AMG"
    ...  # Placeholder for additional Mercedes-Benz models

    ...  # Placeholder for additional models of other brands

    @classmethod
    def bmw_models(cls) -> list:
        return [cls.SERIES_3, cls.SERIES_5, cls.SERIES_7]

    @classmethod
    def audi_models(cls) -> list:
        return [cls.A1, cls.A4, cls.TT]

    @classmethod
    def mercedes_benz_models(cls) -> list:
        return [cls.C_CLASS, cls.E_CLASS, cls.AMG]

    ...  # Placeholder for additional methods of other brands

    @classmethod
    def models_for_brand(cls, brand: Brand) -> list:
        model_function_name = f"{brand.name.lower()}_models"
        model_function_callable = getattr(cls, model_function_name)

        return model_function_callable()
