from enum import Enum

class Movidesk:

    def __init__(self, token, *, url='https://api.movidesk.com/public/v1'):
        self.token = token
        self.url = url

class TicketType(Enum):
    INTERNO = 1
    PUBLICO = 2

class Ticket:
    def __init__(self, *, type, created_by, clients=[]):
        self.type = type
        self.created_by = created_by
        self.clients = clients

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

