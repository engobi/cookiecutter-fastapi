from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Site(BaseModel):
    id: int
    buy_card_id: int
    company_id: int
    status: str
    autoskinz: bool
    autovideo: bool
    tagged: bool
    name: str
    description: str
    description_en: str
    lang: str
    country: str
    url: str
    ssl_support: bool 
    page_view_per_month: int
    unique_visitor_per_month: int
    analytics_source: Optional[str] = None
    analytics_image: Optional[str] = None
    blocked_channels: Optional[str] = None
    blocklist: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    currency: str
