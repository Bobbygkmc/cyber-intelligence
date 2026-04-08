from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, Enum
import enum
from src.database import Base


class BusinessType(str, enum.Enum):
    restaurant = "Restaurant"
    retail = "Retail"
    service = "Service"
    manufacturing = "Manufacturing"
    franchise = "Franchise"
    healthcare = "Healthcare"
    technology = "Technology"
    other = "Other"


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    business_type = Column(String(50), nullable=False)
    location = Column(String(200), nullable=False)
    asking_price = Column(Float, nullable=False)
    annual_revenue = Column(Float, nullable=True)
    annual_cash_flow = Column(Float, nullable=True)
    description = Column(Text, nullable=False)
    seller_financing_available = Column(Boolean, default=False)
    # Seller financing terms (if offered)
    sf_down_payment_pct = Column(Float, nullable=True)   # e.g. 20.0 for 20%
    sf_interest_rate = Column(Float, nullable=True)       # annual %, e.g. 6.5
    sf_term_years = Column(Integer, nullable=True)
    # Contact
    contact_name = Column(String(100), nullable=False)
    contact_email = Column(String(200), nullable=False)
    contact_phone = Column(String(30), nullable=True)
    attorney_involved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
