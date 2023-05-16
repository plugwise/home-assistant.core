"""Plugwise integration models."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, cast

from homeassistant.helpers.entity import EntityDescription

from .utils import get_nested_attr

T = TypeVar("T")

@dataclass
class PlugwiseRequiredKeysMixin(EntityDescription, Generic[T]):
    """Mixin for required keys."""

    key: str | None = None
    pw_value: str | None = None
    pw_value_fn: Callable[[T], Any] | None = None

    def get_pw_value(self, obj: T) -> Any:
        """Return value from Plugwise device."""
        LOGGER.info("HOI calling internal with %s", obj)
        if self.pw_value is not None:
            return get_nested_attr(obj, self.pw_value)
        if self.pw_value_fn is not None:
            return self.wp_value_fn(obj)
        if self.key is not None:
            return get_nested_attr(obj, self.key)

        # reminder for future that one is required
        raise RuntimeError(  # pragma: no cover
            "`pw_value` or `key` is required"
        )

    def get_pw_values(self, obj: T) -> Any:
        if self.pw_values is not None:
            return self.get_nested_attr(obj, self.pw_value)
        if self.pw_values_fn is not None:
            return self.pw_value_fn(obj)
        if self.key is not None:
            return get_nested_attr(obj, self.key)

        # reminder for future that one is required
        raise RuntimeError(  # pragma: no cover
            "`pw_value` or `key` is required"
        )

