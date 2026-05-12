"""Multi-channel attribution model implementations"""

from typing import Dict, List

import numpy as np
from pydantic import BaseModel


class AttributionResult(BaseModel):
    """Attribution credit allocation result"""

    customer_id: str
    touchpoints: List[Dict]
    attribution_model: str
    total_credit: float


class FirstTouchAttribution:
    """First-click attribution model"""

    @staticmethod
    def allocate(customer_touchpoints: List[Dict], conversion_value: float) -> Dict:
        """Allocate 100% credit to first touchpoint"""
        if not customer_touchpoints:
            return {}

        first_touch = customer_touchpoints[0]
        return {first_touch["channel"]: conversion_value}


class LastTouchAttribution:
    """Last-click attribution model"""

    @staticmethod
    def allocate(customer_touchpoints: List[Dict], conversion_value: float) -> Dict:
        """Allocate 100% credit to last touchpoint"""
        if not customer_touchpoints:
            return {}

        last_touch = customer_touchpoints[-1]
        return {last_touch["channel"]: conversion_value}


class LinearAttribution:
    """Linear attribution model"""

    @staticmethod
    def allocate(customer_touchpoints: List[Dict], conversion_value: float) -> Dict:
        """Allocate credit equally across all touchpoints"""
        if not customer_touchpoints:
            return {}

        credit_per_touchpoint = conversion_value / len(customer_touchpoints)
        result = {}

        for touch in customer_touchpoints:
            channel = touch["channel"]
            result[channel] = result.get(channel, 0) + credit_per_touchpoint

        return result


class TimeDecayAttribution:
    """Time decay attribution model - more recent touchpoints get higher credit"""

    @staticmethod
    def allocate(
        customer_touchpoints: List[Dict], conversion_value: float, half_life_days: int = 7
    ) -> Dict:
        """Allocate credit with exponential decay favoring recent touches"""
        if not customer_touchpoints:
            return {}

        # Calculate decay weights
        weights = []
        for i, touch in enumerate(customer_touchpoints):
            days_ago = (len(customer_touchpoints) - i - 1)
            weight = 2 ** (-days_ago / half_life_days)
            weights.append(weight)

        # Normalize weights
        total_weight = sum(weights)
        normalized_weights = [w / total_weight for w in weights]

        # Allocate credit
        result = {}
        for touch, weight in zip(customer_touchpoints, normalized_weights):
            channel = touch["channel"]
            credit = conversion_value * weight
            result[channel] = result.get(channel, 0) + credit

        return result
