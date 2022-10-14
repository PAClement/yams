import inquirer
from prettytable import PrettyTable
import pyfiglet


class Display:

    def input_inquirer_list(self, title, message, choices_tab):
        return inquirer.prompt([
            inquirer.List(
                title,
                message=message,
                choices=choices_tab,
            ),
        ])

    def display_scoreboard(self, first_case, second_case, scoreboard):

        cli_tab_score = PrettyTable([first_case, second_case])

        for i in range(2):
            for key, value in scoreboard[i].items():
                if (value == None):
                    current_value = "-"
                else:
                    current_value = value
                cli_tab_score.add_row([key, current_value])

        print(cli_tab_score)

    def titleDisplay(self, text):

        print(pyfiglet.figlet_format(text))

