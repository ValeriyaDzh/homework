import uuid
from datetime import datetime, date
from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class SpimexTradingResults(Base):

    __tablename__ = "spimex_trading_results"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    exchange_product_id: Mapped[str]
    exchange_product_name: Mapped[str]
    oil_id: Mapped[str]
    delivery_basis_id: Mapped[str]
    delivery_basis_name: Mapped[str]
    delivery_type_id: Mapped[str]
    volume: Mapped[int] = mapped_column(nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    date: Mapped[date]
    created_on: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_on: Mapped[datetime] = mapped_column(
        default=datetime.now, onupdate=datetime.now
    )
