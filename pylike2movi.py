from enum import Enum
from json import JSONDecoder
from inflection import camelize

import requests

class Movidesk:

    def __init__(self, token, url='https://api.movidesk.com/public/v1'):
        self.token = token
        self.url = url


    @property
    def tickets(self):
        response = requests.get(
            url='/'.join([self.url, 'tickets']),
            params={'token': self.token, '$select': 'id,subject'})

        response.raise_for_status()
        return response.json()

    def search_ticket(self, **kwargs):

        filters = ' and '.join([f'contains({k}, \'{v}\')' for (k, v) in kwargs.items()])

        response = requests.get(
            url='/'.join([self.url, 'tickets']),
            params={'token': self.token, '$select': 'id,subject',
                    '$filter': filters})

        response.raise_for_status()
        return map(lambda x: Ticket(**x), response.json())

    def update(self, ticket): #Maybe I would be cool to hava just a update with single dispatch
        response = requests.patch(
            url='/'.join([self.url, 'tickets']),
            params={'token': self.token, 'id': ticket.id},
            json=ticket.dict)

        response.raise_for_status()


class TicketType(Enum):
    INTERNO = 1
    PUBLICO = 2


class Ticket:
    def __init__(self, type=None, subject=None, category=None, status=None,
                 created_by=None, service_first_level_id=None, id=None,
                 clients=[], actions=[]):

        self.id = id
        self.type = type
        self.created_by = created_by
        self.clients = clients
        self.subject = subject
        self.category = category
        self.status = status
        self.service_first_level_id = service_first_level_id
        self.actions = actions

    def add_action(self, action):
        self.actions.append(action)

    @property
    def dict(self):
        return {camelize(k): v for (k, v) in self.__dict__.items() if v}


class Person:
    def __init__(self, *, is_active, person_type, profile_type,
                 bussines_name):
        self.is_active = is_active
        self.person_type = person_type
        self.profile_type = profile_type
        self.bussines_name = bussines_name


class PersonType(Enum):
    PESSOA = 1
    EMPRESA = 2
    DEPARTAMENTO = 3


class ProfileType(Enum):
    AGENTE =1
    CLIENTE = 2
    AGENTE_CLIENTE = 3
