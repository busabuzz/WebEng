from sqlalchemy import create_engine, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Airport(Base):
    __tablename__ = 'airports'
    code = Column(String(10), primary_key=True)
    name = Column(String(100))
    carriers = relationship("Carrier", secondary='airport_carriers')


class Carrier(Base):
    __tablename__ = 'carriers'
    code = Column(String(10), primary_key=True)
    name = Column(String(100))
    airports = relationship("Airport", secondary='airport_carriers')


class AirportCarrier(Base):
    __tablename__ = 'airport_carriers'
    airport_code = Column(Integer, ForeignKey('airports.code'), primary_key=True)
    carrier_code = Column(Integer, ForeignKey('carriers.code'), primary_key=True)
    # statistics_id = Column(Integer, ForeignKey('airport_carrier_statistics.id'))
    # time_id = Column(Integer, ForeignKey('time.id'))


# class AirportCarrierStatistics(Base):
#     __tablename__ = 'airport_carrier_statistics'
#     id = Column(Integer, primary_key=True)
#     airport_carrier_id = Column(Integer, ForeignKey('airport_carriers.id'))
#     flights_id = Column(Integer, ForeignKey('flights.id'))
#     delay_counts_id = Column(Integer, ForeignKey('delay_counts.id'))
#     delay_minutes_id = Column(Integer, ForeignKey('delay_minutes.id'))
#
#
# class Flights(Base):
#     __tablename__ = 'flights'
#     id = Column(Integer, primary_key=True)
#     cancelled = Column(Integer)
#     on_time = Column(Integer)
#     total = Column(Integer)
#     delayed = Column(Integer)
#     diverted = Column(Integer)
#
#
# class DelayCount(Base):
#     __tablename__ = 'delay_counts'
#     id = Column(Integer, primary_key=True)
#     late_aircraft = Column(Integer)
#     weather = Column(Integer)
#     security = Column(Integer)
#     national_aviation_system = Column(Integer)
#     carrier = Column(Integer)
#
#
# class DelayMinutes(Base):
#     __tablename__ = 'delay_minutes'
#     id = Column(Integer, primary_key=True)
#     late_aircraft = Column(Integer)
#     weather = Column(Integer)
#     security = Column(Integer)
#     national_aviation_system = Column(Integer)
#     carrier = Column(Integer)
#     total = Column(Integer)
#
#
# class Time(Base):
#     __tablename__ = 'time'
#     id = Column(Integer, primary_key=True)
#     label = Column(String(10))
#     year = Column(Integer)
#     month = Column(Integer)


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session


def load_db(db_session, data):
    for index, element in enumerate(data):
        if index > 50:
            break
        airport = db_session.query(Airport).filter(Airport.code == element['airport']['code']).first()
        carrier = db_session.query(Carrier).filter(Carrier.code == element['carrier']['code']).first()
        if airport is None:
            airport = Airport(code=element['airport']['code'], name=element['airport']['name'])
        if carrier is None:
            carrier = Carrier(code=element['carrier']['code'], name=element['carrier']['name'])

        airport.carriers.append(carrier)
        # carrier.airports.append(airport)
        db_session.add(airport)
        db_session.add(carrier)
        db_session.commit()

    dumpy = db_session.query(AirportCarrier).all()
    for dump in dumpy:
        print(dump.airport_code, dump.carrier_code)



