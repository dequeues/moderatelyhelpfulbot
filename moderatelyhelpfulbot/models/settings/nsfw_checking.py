from typing import Dict

from pydantic import validator
from pydantic.dataclasses import dataclass


@dataclass
class NSFWChecking:
    ban_time_based_on_pct: Dict[int, int]

    @validator("ban_time_based_on_pct")
    def ban_time_based_on_pct_valid_thresholds(
        cls, values
    ):  # noqa: E501 pylint: disable=no-self-argument,no-self-use
        # pylint: enable=no-self-argument
        for threshold, duration_days in values.items():
            if duration_days < 0 or duration_days > 999:
                raise ValueError(
                    (
                        f"Threshold for {threshold} is invalid."
                        "{duration_days} must be 0 (for permanent),"
                        f" or below 999 (days)."
                    )
                )

        return values
