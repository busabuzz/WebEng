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

    flights_cancelled = Column(Integer)
    flights_on_time = Column(Integer)
    flights_total = Column(Integer)
    flights_delayed = Column(Integer)
    flights_diverted = Column(Integer)

    delay_late_aircraft = Column(Integer)
    delay_weather = Column(Integer)
    delay_security = Column(Integer)
    delay_national_aviation_system = Column(Integer)
    delay_carrier = Column(Integer)

    minutes_late_aircraft = Column(Integer)
    minutes_weather = Column(Integer)
    minutes_security = Column(Integer)
    minutes_national_aviation_system = Column(Integer)
    minutes_carrier = Column(Integer)
    minutes_total = Column(Integer)

    time_label = Column(String(10))
    time_year = Column(Integer)
    time_month = Column(Integer)


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session


def load_db(db_session, data):
    for index, element in enumerate(data):
        if index > 10:
            break
        airport = db_session.query(Airport).filter(Airport.code == element['airport']['code']).first()
        carrier = db_session.query(Carrier).filter(Carrier.code == element['carrier']['code']).first()
        if airport is None:
            airport = Airport(code=element['airport']['code'], name=element['airport']['name'])
        if carrier is None:
            carrier = Carrier(code=element['carrier']['code'], name=element['carrier']['name'])

        airport.carriers.append(carrier)
        db_session.add(airport)
        db_session.add(carrier)
        db_session.commit()

        print(db_session.query(AirportCarrier).first())

        airport_carrier = db_session.query(AirportCarrier)\
            .filter(AirportCarrier.airport_code == element['airport']['code'],
                    AirportCarrier.carrier_code == element['carrier']['code']).update({AirportCarrier.flights_cancelled: 6}, synchronize_session=False)

        airport_carrier.flights_cancelled = element['statistics']['flights']['cancelled']
        airport_carrier.flights_on_time = element['statistics']['flights']['on time']
        airport_carrier.flights_total = element['statistics']['flights']['total']
        airport_carrier.flights_delayed = element['statistics']['flights']['delayed']
        airport_carrier.flights_diverted = element['statistics']['flights']['diverted']

        airport_carrier.delay_late_aircraft = element['statistics']['# of delays']['late aircraft']
        airport_carrier.delay_weather = element['statistics']['# of delays']['weather']
        airport_carrier.delay_security = element['statistics']['# of delays']['security']
        airport_carrier.delay_national_aviation_system = element['statistics']['# of delays']['national aviation system']
        airport_carrier.delay_carrier = element['statistics']['# of delays']['carrier']

        airport_carrier.minutes_late_aircraft = element['statistics']['minutes delayed']['late aircraft']
        airport_carrier.minutes_weather = element['statistics']['minutes delayed']['weather']
        airport_carrier.minutes_security = element['statistics']['minutes delayed']['security']
        airport_carrier.minutes_national_aviation_system = element['statistics']['minutes delayed']['national aviation system']
        airport_carrier.minutes_carrier = element['statistics']['minutes delayed']['carrier']
        airport_carrier.minutes_total = element['statistics']['minutes delayed']['total']

        airport_carrier.time_label = element['time']['label']
        airport_carrier.time_month = element['time']['month']
        airport_carrier.time_year = element['time']['year']

        # db_session.add(airport_carrier)
        db_session.commit()

    dumpy = db_session.query(AirportCarrier).all()
    for dump in dumpy:
        print(dump.airport_code, dump.carrier_code, dump.flights_cancelled)



