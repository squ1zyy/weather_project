import requests
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Session, relationship
from json import dumps
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(170), nullable=False)


def fill_cities(eng):
    session = Session(bind=eng)
    cities_list = ["Dnipro", "Kharkiv", "Lviv", "London"]
    cities_obj_list = [City(name=city_name) for city_name in cities_list]
    session.add_all(cities_obj_list)
    session.commit()
    return 'Success'


class Weather(Base):
    __tablename__ = 'weather_1'
    id = Column(Integer, primary_key=True)
    temperature = Column(String(4), nullable=False)
    wind_speed = Column(String(10), nullable=False)
    curr_weather = Column(String(10), nullable=False)
    city = relationship("City")
    city_id = Column(ForeignKey("cities.id"))
    date = Column(DateTime(), default=datetime.now())


def fill_weather(eng):
    session = Session(bind=eng)
    query = session.query(City)
    city_objects = query.all()
    weather_obj_list = []
    for el in city_objects:
        city_name = el.name
        req = requests.get('https://api.openweathermap.org/data/2.5/weather',
              params={'appid': 'dc4782cd45700c18c29efd99522de225',
                      'units': 'metric',
                      'q': city_name})
        print(city_name)
        city_id = el.id
        temperature = req.json()['main']['temp']
        wind_speed = req.json()['wind']['speed']
        curr_weather = req.json()['weather'][0]['main']
        weather_obj = Weather(temperature=temperature, wind_speed=wind_speed, 
                            curr_weather=curr_weather, city_id=city_id)
        weather_obj_list.append(weather_obj)
        # print(dumps(req.json(), indent=4))

    print('1')
    print(weather_obj_list)
    session.add_all(weather_obj_list)
    session.commit()
    return 'Success'


if __name__ == "__main__":
    engine = create_engine('sqlite:///weather.db')
    Base.metadata.create_all(engine)
    # fill_cities(engine)
    fill_weather(engine)