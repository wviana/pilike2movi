from pylike2movi import Ticket, TicketType, Person, PersonType, ProfileType


def test_ticket_minimun_data():
    me = Person(is_active=True, person_type=PersonType.PESSOA,
                profile_type=ProfileType.AGENTE, bussines_name='Wesley Viana')

    t = Ticket(
        type=TicketType.INTERNO,
        created_by=me,
        clients=[me]
    )

    assert t
    assert t.type == TicketType.INTERNO
    assert t.created_by == me
    assert len(t.clients) == 1
    assert t.clients[0] == me


def test_ticket_types():
    assert TicketType.INTERNO.value == 1
    assert TicketType.PUBLICO.value == 2


def test_current_minimum_ticket_data():
    """ This is about and api that I already had, so I known this is the minimum data to crate a ticket """
    """
    ticket = {
        'type': TicketVisibility.INTERNAL, # Mantem
        'subject': subject,  # "name": "ArtSoft", # Nome do Ticket # Planejamento do Projeto ArtSoft - <cnpj_com_pontos>
        'category': 'Requisição de Serviço', # Mantem
        'status': 'Aguardando',
        'createdDate': movidesk_timestamp(),
        'createdBy': {
            'id': settings.MovideskAlpeFieldSetting.CREATED_BY.value['id']
        },
        'actions': [
            {'id': 1, 'type': TicketVisibility.INTERNAL, 'description': subject} # Adicionar além de text da action returnDate # "list": "Devolutiva Comercial",
        ],
        'serviceFirstLevelId': service_id,
        'clients': [
            {
                'id': movidesk_company['id'],
                'personType': TicketPersonType.EMPRESA,
                'profileType': TicketProfileType.CLIENTE,
            }
        ],
    }
    """
    me = Person(is_active=True, person_type=PersonType.PESSOA,
                profile_type=ProfileType.AGENTE, bussines_name='Wesley Viana')

    subject_value = 'Planejamento do Projeto ArtSoft - <cnpj_com_pontos>'
    service_id = 12345
    t = Ticket(
        id=15,
        type=TicketType.INTERNO,
        subject=subject_value,
        category='Requisição de Serviço',
        status='Aguardando',
        created_by=me,
        actions=[
            {'id': 1, 'type': TicketType.INTERNO, 'description': subject_value}
        ],
        service_first_level_id=service_id,
        clients=[
            {
                'id': 1,
                'personType': PersonType.EMPRESA,
                'profileType': ProfileType.CLIENTE,
            }
        ])

    assert t
    assert t.id == 15
    assert len(t.actions) > 0
