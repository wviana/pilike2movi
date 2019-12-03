from pylike2movi import Movidesk
from pytest import raises
from collections.abc import Iterable
from urllib.parse import unquote_plus

import responses


def test_instance_movidesk_with_token():
    token = 'test1234'
    md = Movidesk(token=token)
    assert md.token == token
    assert md.url == 'https://api.movidesk.com/public/v1'


def test_instance_with_token_and_url():
    token = 'anything'
    url = 'https://thatwillnotchange.movidesk.com/public/v1'
    md = Movidesk(token, url=url)
    assert md.token == token
    assert md.url == url


@responses.activate
def test_list_ticket():
    responses.add(responses.GET, 'https://api.movidesk.com/public/v1/tickets',
                  json=[], status=200)

    token = 'anything'
    md = Movidesk(token)
    found_tickets = md.tickets
    assert isinstance(found_tickets, Iterable)
    assert len(responses.calls) == 1


@responses.activate
def test_search_ticket_by_subject_finding_one():
    responses.add(responses.GET, 'https://api.movidesk.com/public/v1/tickets',
                  json=[{'subject': 'teste gatilho não assumido', 'id': 25}],
                  status=200)

    token = 'anything'
    md = Movidesk(token)
    subject_value = 'teste'
    found_tickets = md.search_ticket(subject=subject_value)
    assert len(responses.calls) == 1

    filter_query = f'$filter=contains(subject, \'{subject_value}\')'
    called_url = responses.calls[0].request.url
    assert filter_query in unquote_plus(called_url)

    assert isinstance(found_tickets, Iterable)
    assert len(list(found_tickets)) == 1


@responses.activate
def test_search_ticket_one_dynamic_fields():
    responses.add(responses.GET, 'https://api.movidesk.com/public/v1/tickets',
                  json=[{'subject': 'teste gatilho não assumido', 'id': 25}],
                  status=200)

    token = 'anything'
    md = Movidesk(token)
    md.search_ticket(id=35)

    filter_query = f'$filter=contains(id, \'35\')'
    called_url = responses.calls[0].request.url
    assert filter_query in unquote_plus(called_url)


@responses.activate
def test_add_action_to_existing_ticket():
    responses.add(responses.GET, 'https://api.movidesk.com/public/v1/tickets',
                  json=[{'subject': 'teste gatilho não assumido', 'id': 25}],
                  status=200)

    token = 'anything'
    md = Movidesk(token)
    ticket = next(md.search_ticket(subject='teste'))

    action_description = 'Teste de descricao'
    ticket.add_action({'description': action_description})

    assert len(responses.calls) == 1
    assert len(ticket.actions) > 0
    assert ticket.actions[-1]['description'] == action_description

    responses.add(responses.PATCH, 'https://api.movidesk.com/public/v1/tickets',
                  json=[{'subject': 'teste gatilho não assumido', 'id': 25}],
                  status=200)
    md.update(ticket)

    assert len(responses.calls) == 2
    assert f'id={ticket.id}' in unquote_plus(responses.calls[1].request.url)



