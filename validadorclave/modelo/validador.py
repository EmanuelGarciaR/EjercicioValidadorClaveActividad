# TODO: Implementa el código del ejercicio aquí
# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from errores import NoCumpleLongitudMinimaError, NoTieneNumeroError, NoTienePalabraSecretaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada == len(clave):
            return True

    def _contiene_mayuscula(self, clave: str) -> bool:
        return clave.isupper()

    def _contiene_minuscula(self, clave: str) -> bool:
        return clave.islower()

    def _contiene_numero(self, clave: str) -> bool:
        return clave.isdigit()

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave: str) -> bool:
        cant_mayus = 0
        if clave in "calisto":
            for i in clave:
                mayus = i.isupper()
                if mayus:
                    cant_mayus += 1
        if cant_mayus >= 2 and cant_mayus != len(clave):
            return True

    def es_valida(self, clave: str) -> bool:
        cont_digit = 0
        for i in clave:
            digit = i.isdigit()
            if digit:
                cont_digit += 1
        if len(clave) > 6:
            if cont_digit >= 1:
                if self.contiene_calisto(clave):
                    return True
                raise NoTienePalabraSecretaError("Error: ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
            raise NoTieneNumeroError("Error: ReglaCalisto: La clave debe tener al menos 1 digito")
        raise NoCumpleLongitudMinimaError("Error: ReglaValidacionCalisto: La clave debe tener una longitud de más de 6 caracteres")


class ReglasValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave: str) -> bool:
        match = "@_#$%"
        for i in clave:
            if i in match:
                return True

    def es_valida(self, clave: str) -> bool:
        cont_mayus = 0
        cont_minus = 0
        cont_digit = 0
        for i in clave:
            mayus = i.isupper()
            minus = i.islower()
            digit = i.isdigit()
            if mayus:
                cont_mayus += 1
            if minus:
                cont_minus += 1
            if digit:
                cont_digit += 1

        if len(clave) > 8 and cont_mayus >= 1 and cont_minus >= 1 and cont_digit >= 1 and self.contiene_caracter_especial(
                clave):
            return True

class Validador:
    pass
