from impact.tests.api_test_case import APITestCase
from impact.tests.factories import ClearanceFactory


class TestOrganization(APITestCase):
    def test_str(self):
        clearance = ClearanceFactory()
        assert str(clearance.user) in str(clearance)
        assert str(clearance.program_family) in str(clearance)
        assert clearance.level in str(clearance)