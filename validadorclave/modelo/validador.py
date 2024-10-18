# TODO: Implementa el código del ejercicio aquí
# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneNumeroError, NoTienePalabraSecretaError
from validadorclave.modelo.errores import NoTieneCaracterEspecialError, NoTieneLetraMinusculaError, \
    NoTieneLetraMayusculaError


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) >= self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        for item in clave:
            if item.isupper():
                return True
        return False


    def _contiene_minuscula(self, clave: str) -> bool:
        for item in clave:
            if item.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for item in clave:
            if item.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self, longitud_esperada: int= 6):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave: str) -> bool:
        """
                cant_mayus = 0
                if clave.lower() in "calisto":
                    for letter in clave:
                        if letter.isupper():
                            cant_mayus += 1
                    if cant_mayus >= 2 and cant_mayus != len(clave):
                        return True
                return False
        """
        if "calisto" in clave.lower():
            counter = 0
            for item in clave:
                if item in "CALISTO":
                    counter += 1

            if 2 <= counter < 7:
                return True
        return False


    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()
        return True
"""
        cont_digit = 0
        for i in clave:
            digit = i.isdigit()
            if digit:
                cont_digit += 1
        if len(clave) > 6:
            if cont_digit >= 1:
                if self.contiene_calisto(clave):
                    return True
                else:
                    raise NoTienePalabraSecretaError("Error: ReglaValidacionCalisto: La palabra calisto debe estar escrita con al menos dos letras en mayúscula")
            else:
                raise NoTieneNumeroError("Error: ReglaValidacionCalisto: La clave debe tener al menos 1 digito")
        else:
            raise NoCumpleLongitudMinimaError("Error: ReglaValidacionCalisto: La clave debe tener una longitud de más de 6 caracteres")
"""

class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self, longitud_esperada: int = 8):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave: str) -> bool:
        """
                    match = "@_#$%"
                    for i in clave:
                        if i in match:
                            return True
                    return False
                """
        especial = "@_#$%"
        for i in especial:
            if i in clave:
                return True
        return False



    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError()
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()

        return True
"""
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

        if len(clave) > 8:
            if cont_mayus >= 1:
                if cont_minus >= 1:
                    if cont_digit >= 1:
                        if self.contiene_caracter_especial(clave):
                            return True
                        else:
                            raise NoTieneCaracterEspecialError("Error: ReglaValidacionGanimedes: La clave no contiene algún caracter especial")
                    else:
                        raise NoTieneNumeroError("Error: ReglaValidacionGanimedes: La clave debe tener al menos 1 digito")
                else:
                    raise NoTieneLetraMinusculaError("Error: ReglaValidacionGanimedes: La clave debe tener al menos 1 minúscula")
            else:
                raise NoTieneLetraMayusculaError("Error: ReglaValidacionGanimedes: La clave debe tener al menos 1 mayúscula")
        else:
            raise NoCumpleLongitudMinimaError("Error: ReglaValidacionGanimedes: La clave debe tener una longitud de más de 8 caracteres")
"""

class Validador:
    def __init__(self, regla:ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)

