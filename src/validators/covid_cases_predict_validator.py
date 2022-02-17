"""Diretório de validações para covid_cases_predict"""
from cerberus import Validator
from src.data.database.get_countries import GetCountry
from src.infra.database.repo import CountryRepo
from src.errors import HttpUnprocessableEntityError

countries_repo = CountryRepo()
get_countries = GetCountry(countries_repo)

get_countries_response = get_countries.all_countries()
all_countries = []

for data in get_countries_response["data"]:
    all_countries.append(data.name)

if all_countries == []:
    all_countries = ["BRA"]


def covid_cases_predict_validator(request: any) -> None:
    """Validor de parâmtros da url"""

    query_params = dict(request.query_params)
    try:

        query_params["days"] = int(query_params["days"])

    except KeyError:
        pass
    except Exception as error:
        raise HttpUnprocessableEntityError(message=str(error)) from error

    querry_param_validator = Validator(
        {
            "country": {"type": "string", "allowed": all_countries, "required": True},
            "days": {"type": "integer", "min": 0, "required": True},
        }
    )

    response = querry_param_validator.validate(query_params)

    if response is False:
        raise HttpUnprocessableEntityError(message=querry_param_validator.errors)
