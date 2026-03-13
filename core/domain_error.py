class DomainError(Exception):
    """Error base del dominio"""

    pass


class EmptyTitleError(DomainError):
    """Error al crear el título"""

    pass


class InvalidAmountError(DomainError):
    """Error al ingresar el monto."""

    pass


class InvalidExpenseDateError(DomainError):
    """Se lanza cuando la fecha es inválida"""

    pass
