"""Diretório de validações para countries"""
from cerberus import Validator
from src.data.database.get_countries import GetCountry
from src.infra.database.repo import CountryRepo
from src.errors import HttpUnprocessableEntityError, HttpBadRequestError

countries_repo = CountryRepo()
get_countries = GetCountry(countries_repo)

get_countries_response = get_countries.all_countries()
all_countries = []

for data in get_countries_response["data"]:
    all_countries.append(data.name)


def get_from_country_validator(request: any) -> None:
    """Validador de parâmtros da url"""

    querry_param_validator = Validator(
        {"name": {"type": "string", "allowed": all_countries}}
    )

    response = querry_param_validator.validate(request.query_params)

    if response is False:
        raise HttpUnprocessableEntityError(message=querry_param_validator.errors)


async def register_country_validator(request: any) -> None:
    """Validador de parâmetros de body"""

    body = None

    try:

        body = await request.json()

    except Exception:  # pylint: disable=W0703
        pass

    body_validator = Validator({"name": {"type": "string", "required": True}})

    if body is not None:
        response = body_validator.validate(body)
    else:
        raise HttpBadRequestError(message="This request need a name body-param")

    if response is False:
        raise HttpUnprocessableEntityError(message=body_validator.errors)
