#
# Kenny Kirtland
# @2017
#
# Tournament Tests
#
#

from unittest import TestCase

from tournament import Tournament

class TournamentTest(TestCase):
    def test_Process_Verify_TournamentCreated(self):
        t = Tournament()
        self.assertIsNotNone(t)