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


