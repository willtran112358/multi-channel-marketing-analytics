"""Marketing event data models with Pydantic validation"""

from datetime import datetime
from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel, Field, field_validator


class ChannelType(str, Enum):
    EMAIL = "email"
    SOCIAL = "social"
    WEB = "web"
    PAID_ADS = "paid_ads"
    ORGANIC = "organic"
    REFERRAL = "referral"


class EventType(str, Enum):
    VIEW = "view"
    CLICK = "click"
    CONVERSION = "conversion"
    SUBSCRIBE = "subscribe"
    UNSUBSCRIBE = "unsubscribe"
    PAGE_VISIT = "page_visit"
    CART_ADD = "cart_add"
    PURCHASE = "purchase"


class MarketingEvent(BaseModel):
    """Raw marketing event"""

    event_id: str
    customer_id: str
    campaign_id: str
    channel: ChannelType
    event_type: EventType
    timestamp: datetime
    properties: Dict[str, any] = Field(default_factory=dict)

    @field_validator("event_id", "customer_id", "campaign_id")
    def validate_ids(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError("ID cannot be empty")
        return v.strip()


class CustomerProfile(BaseModel):
    """Enriched customer profile"""

    customer_id: str
    email: str
    first_name: str
    last_name: str
    signup_date: datetime
    last_activity: datetime
    lifetime_value: float = 0.0
    churn_score: Optional[float] = None
    segment: str = "unknown"
    metadata: Dict[str, any] = Field(default_factory=dict)


class CampaignMetrics(BaseModel):
    """Campaign performance metrics"""

    campaign_id: str
    campaign_name: str
    start_date: datetime
    end_date: Optional[datetime] = None
    channel: ChannelType
    impressions: int = 0
    clicks: int = 0
    conversions: int = 0
    revenue: float = 0.0
    cost: float = 0.0

    @property
    def ctr(self) -> float:
        """Click-through rate"""
        return (self.clicks / self.impressions * 100) if self.impressions > 0 else 0.0

    @property
    def conversion_rate(self) -> float:
        """Conversion rate"""
        return (
            (self.conversions / self.clicks * 100) if self.clicks > 0 else 0.0
        )

    @property
    def roi(self) -> float:
        """Return on investment"""
        return ((self.revenue - self.cost) / self.cost * 100) if self.cost > 0 else 0.0
