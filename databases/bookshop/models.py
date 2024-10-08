from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from database import Base


###BOOK###
class Genre(Base):

    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    books = relationship("Book", back_populates="genre", uselist=True)


class Author(Base):

    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author", uselist=True)


class Book(Base):

    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genre.id"))
    price = Column(Float)
    amount = Column(Integer, default=0)

    genre = relationship("Genre", back_populates="books", uselist=False)
    author = relationship("Author", back_populates="books", uselist=False)


###CUSTOMER###
class City(Base):

    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False, unique=True)
    days_delivery = Column(Integer)

    clients = relationship("Client", back_populates="city", uselist=True)


class Client(Base):

    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("city.id"))
    email = Column(String, nullable=False, unique=True)

    city = relationship("City", back_populates="clients", uselist=False)
    buys = relationship("Buy", back_populates="client", uselist=True)


###ORDER###
class Buy(Base):

    __tablename__ = "buy"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    client_id = Column(Integer, ForeignKey("client.id", ondelete="CASCADE"))

    client = relationship("Client", back_populates="buys", uselist=False)


class BuyBook(Base):

    __tablename__ = "buy_book"

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.id"))
    book_id = Column(Integer, ForeignKey("book.id", ondelete="CASCADE"))
    amount = Column(Integer)


class Step(Base):

    __tablename__ = "step"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    by_steps = relationship("BuyStep", back_populates="step", uselist=True)


class BuyStep(Base):

    __tablename__ = "buy_step"

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.id"))
    step_id = Column(Integer, ForeignKey("step.id"))
    date_beg = Column(DateTime)
    date_end = Column(DateTime)

    step = relationship("Step", back_populates="by_steps", uselist=False)
