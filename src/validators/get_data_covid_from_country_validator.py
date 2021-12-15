"""Diretório de validações para get_data_covid_from_country"""
from cerberus import Validator

def get_from_country_validator(request: any):
    """Validor de paginação"""
    querry_param_validator = Validator({
        'country': {
            'type': 'string',
            'allowed': ['BRA', 'USA'],
            'required': True
        }
    })

    response = querry_param_validator.validate(request.query_params)

    if response is False:
        raise Exception(querry_param_validator.errors)
