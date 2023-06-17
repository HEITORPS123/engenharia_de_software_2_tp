import os
import sys
from time import sleep
from interface import InterfacePrints
from user_controller import UserController
from adm_controller import AdmController


class MainController:
    def __init__(self, conn):
        self.conn = conn
    
    def run(self, from_file=False, file_path=None, to_file=False, outfile_path=None):
        
        if from_file:
            os.environ['DO_CLEAR'] = "False"
            sys.stdin = open(file_path)

        if to_file:
            os.environ['DO_CLEAR'] = "False"
            sys.stdout = open(outfile_path, 'w')        
        
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
        
        if from_file:
            sys.stdin.close()
            sys.stdin = sys.__stdin__

        if to_file:
            sys.stdout.close()
            sys.stdout = sys.__stdout__

    def _run_auxiliar(self, choice, options):
        if choice in options.keys():
            mode_controller = options[choice](self.conn)
            mode_controller.login()
            self.run()

        elif choice == 0:
            InterfacePrints.print_exiting_msg()
            return
        else:
            InterfacePrints.print_invalid_option()
            self.run()
            
