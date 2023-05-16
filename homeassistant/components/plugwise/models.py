"""Plugwise integration models."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from homeassistant.helpers.entity import EntityDescription

from plugwise import DeviceData

T = TypeVar("T", bound=DeviceData)

@dataclass
class PlugwiseRequiredKeysMixin(EntityDescription, Generic[T]):
    """Mixin for required keys."""

    pw_value: str | None = None
    pw_value_fn: Callable[[T], Any] | None = None

    def get_pw_value(self, obj: T) -> Any:
        """Return value from Plugwise device."""
        if self.pw_value is not None:
            return obj.get(self.pw_value)
        if self.pw_value_fn is not None:
            return self.pw_value_fn(obj)
        if self.key is not None:
            return obj.get(self.key)

        # reminder for future that one is required
        raise RuntimeError(  # pragma: no cover
            "`pw_value` or `key` is required"
        )
