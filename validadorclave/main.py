from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneNumeroError, NoTienePalabraSecretaError, \
    NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneCaracterEspecialError
from validadorclave.modelo.validador import ReglaValidacion, Validador


def validar_clave(clave: str, reglas_validacion: list[ReglaValidacion]):
    for regla in reglas_validacion:
        validador = Validador(regla)
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida. La regla es: {regla.__class__.__name__}")
        except NoCumpleLongitudMinimaError:
            print(f"Error: {regla.__class__.__name__}: La clave no cumple la longitud mínima.")
        except NoTieneLetraMayusculaError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene letra mayúscula.")
        except NoTieneLetraMinusculaError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene letra minúscula.")
        except NoTieneNumeroError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene un número.")
        except NoTieneCaracterEspecialError:
            print(f"Error: {regla.__class__.__name__}: La clave no tiene un caracter especial.")
        except NoTienePalabraSecretaError:
            print(f"Error: {regla.__class__.__name__}: La clave no contiene la palabra secreta 'calisto'.")