from sqlalchemy import Column, String, Integer, ForeignKey, Float, DateTime

from database import Base


###BOOK###
class Genre(Base):

    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)


class Author(Base):

    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Book(Base):

    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genre.id"))
    price = Column(Float)
    amount = Column(Integer, default=0)


###CUSTOMER###
class City(Base):

    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False, unique=True)
    days_delivery = Column(Integer)  # ???


class Client(Base):

    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    city_id = Column(Integer, ForeignKey("city.id"))
    email = Column(String, nullable=False, unique=True)


###ORDER###
class Buy(Base):

    __tablename__ = "buy"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    client_id = Column(Integer, ForeignKey("client.id", ondelete="CASCADE"))


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


class BuyStep(Base):

    __tablename__ = "buy_step"

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.id"))
    step_id = Column(Integer, ForeignKey("step.id"))
    date_beg = Column(DateTime)
    date_end = Column(DateTime)
