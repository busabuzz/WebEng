from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# example data
Airports = [
    {
      "code": "ATL",
      "name": "Atlanta, GA: Hartsfield-Jackson Atlanta International"
    },
    {
      "code": "BOS",
      "name": "Boston, MA: Logan International"
    },
    {
        "code": "BWI",
        "name": "Baltimore, MD: Baltimore/Washington International Thurgood Marshall"
    }
]

Carriers = [
    {
        "code": "AA",
        "name": "American Airlines Inc."
    },
    {
      "code": "AA",
      "name": "American Airlines Inc."
    },
    {
      "code": "DL",
      "name": "Delta Air Lines Inc."
    }
]

""" Elke functienaam wordt gekoppeld aan de operationId in de YAML file"""

# TODO: Data inlezen (ez)
# TODO: Responses opstellen
# TODO: Responses serializen naar XML, JSON is native. moet dus een module voor komen, misschien heeft flask wat.
# TODO: Documentatie in YAML completen.
# TODO: Alle parameters invoeren in YAML.
# TODO: meer?


def airports(content_type):
    return []


def carriers():
    return []


def airport_carriers(airport_code):
    return []


def carrier_get_statistics(carrier_code):
    return []


def carrier_post_statistics(carrier_code):
    return []


def carrier_put_statistics(carrier_code):
    return []


def carrier_delete_statistics(carrier_code):
    return []


def carrier_performance(carrier_code):
    return []


def carrier_delays(carrier_code):
    return []


def carrier_delays_statistics(carrier_code):
    return []


