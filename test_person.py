from pylike2movi import Person, PersonType, ProfileType


def test_person_minimum_data_nao_agente():
    bussines_name = 'Joao da Silva'
    p = Person(
        is_active=True,
        person_type=PersonType.PESSOA,
        profile_type=ProfileType.CLIENTE,
        bussines_name=bussines_name
    )
    assert p.is_active is True
    assert p.person_type == PersonType.PESSOA
    assert p.profile_type == ProfileType.CLIENTE
    assert p.bussines_name == bussines_name

# TODO: person agent, should have field acess_profile
# def test_person_minimum_data_agente():


# TODO: person type empresa, should have field corporate_name

def test_person_types():
    assert PersonType.PESSOA.value == 1
    assert PersonType.EMPRESA.value == 2
    assert PersonType.DEPARTAMENTO.value == 3


def test_profile_types():
    assert ProfileType.AGENTE.value == 1
    assert ProfileType.CLIENTE.value == 2
    assert ProfileType.AGENTE_CLIENTE.value == 3
