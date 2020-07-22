from pydantic import BaseModel
from typing import Optional


'''
{
   "id":"5",
   "buy_card_id":"1",
   "company_id":"1059",
   "status":"enabled",
   "autoskinz":"1",
   "autovideo":"1",
   "tagged":"1",
   "name":"Virtuafoot",
   "description":"Site de simulation de gestion de clubs de football",
   "description_en":"Football club management simulation game website",
   "lang":"fr",
   "country":"FR",
   "url":"www.virtuafoot.com",
   "ssl_support":"0",
   "page_view_per_month":"27000000",
   "unique_visitor_per_month":"150000",
   "analytics_source":"NULL",
   "analytics_image":"NULL",
   "blocked_channels":"NULL",
   "blocklist":"NULL",
   "created_at":"2015-07-23 10:09:22",
   "updated_at":"2017-07-31 12:36:46",
   "deleted_at":null,
   "currency":"EUR"
}
'''
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
