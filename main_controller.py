from interface import InterfacePrints
from user_controller import UserController
from adm_controller import AdmController


class MainController:
    def __init__(self):
        pass
    
    def run(self):
        InterfacePrints.print_menu()
        try:
            choice = int(input())
        except:
            InterfacePrints.print_invalid_option()
            self.run()
            return

        options = {
            1: UserController,
            2: AdmController,
        }

        self._run_auxiliar(choice, options)

    def _run_auxiliar(self, choice, options):
        if choice in options.keys():
            mode_controller = options[choice]()
            mode_controller.run()

        elif choice == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()
