class BusError(Exception):
    """Базовое исключение приложения."""


class BusNotFoundError(BusError):
    """Автобус не найден."""


class DuplicateBusError(BusError):
    """Автобус уже существует."""