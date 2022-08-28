
#IMPORTACOES
import pytest
from num_romanos import converte


# 1
def test_numero_esperado():
    assert converte('V') == 5

# 2
def test_numero_diferente_do_esperado():
    assert converte('L') != 51

# 3
def test_numero_lower():
    assert converte('d') == 500

# 4
def test_numero_nao_existe_no_dicionario():
    assert converte('A') == 'Tente outro numero romano'

# 5
def test_argumento_diferente_de_string():
    with pytest.raises(TypeError):
        converte(5)

# QUESTAO 2
def test_deveEntenderNumerosComoIX():
    assert converte('IX') == 9

# 6
def test_extra_deveEntenderNumerosComoXI():
    assert converte('XI') == 11

# 7
def test_extra_numeros_com_mais_de_duas_casas():
    assert converte('XII') == 'Ainda não implementado, tente numeros apenas com duas casas'
