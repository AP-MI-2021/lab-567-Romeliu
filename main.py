from Tests.test_crud import test_crud
from Tests.test_misc import test_misc
from UserInterface.console import run_ui


def main():
    vanzari = []
    vanzari = run_ui(vanzari)

if __name__ == '__main__':
    test_crud()
    test_misc()
    main()