# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
import numpy.polynomial.polynomial as nppoly


def roots_20(coef: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja wyznaczająca miejsca zerowe wielomianu funkcją
    `nppoly.polyroots()`, najpierw lekko zaburzając wejściowe współczynniki 
    wielomianu (N(0,1) * 1e-10).

    Args:
        coef (np.ndarray): Wektor współczynników wielomianu (n,).

    Returns:
        (tuple[np.ndarray, np. ndarray]):
            - Zaburzony wektor współczynników (n,),
            - Wektor miejsc zerowych (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(coef, np.ndarray):
        return None
    if coef.ndim != 1 or coef.size == 0:
        return None

    coef = coef + np.random.random_sample(coef.shape) * 1e-10
    roots = nppoly.polyroots(coef)
    return coef, roots


def frob_a(a: np.ndarray) -> np.ndarray | None:
    if not isinstance(a, np.ndarray) or a.ndim != 1 or len(a) < 2:
        return None
    if a[-1] == 0:
        return None

    n = len(a) - 1
    F = np.zeros((n, n))
    F[:-1, 1:] = np.eye(n - 1)
    F[-1, :] = -a[:-1] / a[-1]
    return F

coef = [1, 4, 5, 2]
F = frob_a(np.array(coef))
print(F)


def is_nonsingular(A: np.ndarray) -> bool | None:
    """Funkcja sprawdzająca czy podana macierz NIE JEST singularna. Przy
    implementacji należy pamiętać o definicji zera maszynowego.

    Args:
        A (np.ndarray): Macierz (n,n) do przetestowania.

    Returns:
        (bool): `True`, jeżeli macierz A nie jest singularna, w przeciwnym 
            wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(A, np.ndarray):
        return None
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    
    try:
        np.linalg.inv(A)
        return True
    except np.linalg.LinAlgError:
        return False
    
