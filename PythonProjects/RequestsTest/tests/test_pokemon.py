import requests
import pytest

def test_status_code_and_name() :
    responseForGetTrainers = requests.get(
        url='https://api.pokemonbattle.me:9104/trainers' , 
        params={'trainer_id' : 2543},
        timeout= 5
    )
    assert responseForGetTrainers.status_code == 200
    assert responseForGetTrainers.json()['trainer_name'] == 'Max'


