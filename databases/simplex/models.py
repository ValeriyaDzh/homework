import uuid
from datetime import datetime, UTC
from sqlalchemy import UUID, Column, String, Integer, Date, DateTime

from database import Base


class SpimexTradingResults(Base):

    __tablename__ = "spimex_trading_results"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    exchange_product_id = Column(String, nullable=False)
    exchange_product_name = Column(String, nullable=False)
    oil_id = Column(String, nullable=False)
    delivery_basis_id = Column(String, nullable=False)
    delivery_basis_name = Column(String, nullable=False)
    delivery_type_id = Column(String, nullable=False)
    volume = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    date = Column(Date)
    created_on = Column(DateTime, default=datetime.now)
    updated_on = Column(DateTime, default=datetime.now, onupdate=datetime.now)
