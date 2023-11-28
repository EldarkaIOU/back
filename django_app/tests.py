import unittest
from unittest.mock import MagicMock
from .management.commands.run_telegram_bot import start, show_cars, help_command, echo_all


class TestBot(unittest.TestCase):

    def test_start(self):
        message = MagicMock()
        message.chat.id = 534895748
        start(message)

    def test_help(self):
        message = MagicMock()
        message.chat.id = 534895748
        help_command(message)

    def test_figures(self):
        message = MagicMock()
        message.chat.id = 534895748
        show_cars(message)



if __name__ == '__main__':
    unittest.main()