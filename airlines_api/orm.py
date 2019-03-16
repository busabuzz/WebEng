from sqlalchemy import create_engine, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Airport(Base):
    __tablename__ = 'airports'
    code = Column(String(10), primary_key=True)
    name = Column(String(100))


class Carrier(Base):
    __tablename__ = 'carriers'
    code = Column(String(10), primary_key=True)
    name = Column(String(100))


class AirportCarrier(Base):
    __tablename__ = 'airport_carriers'
    id = Column(Integer, primary_key=True)
    airport_code = Column(Integer, ForeignKey('airports.code'))
    carrier_code = Column(Integer, ForeignKey('carriers.code'))
    statistics_id = Column(Integer, ForeignKey('airport_carrier_statistics.id'))
    time_id = Column(Integer, ForeignKey('time.id'))


class AirportCarrierStatistics(Base):
    __tablename__ = 'airport_carrier_statistics'
    id = Column(Integer, primary_key=True)
    airport_carrier_id = Column(Integer, ForeignKey('airport_carriers.id'))
    flights_id = Column(Integer, ForeignKey('flights.id'))
    delay_counts_id = Column(Integer, ForeignKey('delay_counts.id'))
    delay_minutes_id = Column(Integer, ForeignKey('delay_minutes.id'))


class Flights(Base):
    __tablename__ = 'flights'
    id = Column(Integer, primary_key=True)
    cancelled = Column(Integer)
    on_time = Column(Integer)
    total = Column(Integer)
    delayed = Column(Integer)
    diverted = Column(Integer)


class DelayCount(Base):
    __tablename__ = 'delay_counts'
    id = Column(Integer, primary_key=True)
    late_aircraft = Column(Integer)
    weather = Column(Integer)
    security = Column(Integer)
    national_aviation_system = Column(Integer)
    carrier = Column(Integer)


class DelayMinutes(Base):
    __tablename__ = 'delay_minutes'
    id = Column(Integer, primary_key=True)
    late_aircraft = Column(Integer)
    weather = Column(Integer)
    security = Column(Integer)
    national_aviation_system = Column(Integer)
    carrier = Column(Integer)
    total = Column(Integer)


class Time(Base):
    __tablename__ = 'time'
    id = Column(Integer, primary_key=True)
    label = Column(String(10))
    year = Column(Integer)
    month = Column(Integer)


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
