from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.dellemc.enterprise_sonic.tests.unit.compat.mock import (
    patch,
)
from ansible_collections.dellemc.enterprise_sonic.plugins.modules import (
    sonic_copp,
)
from ansible_collections.dellemc.enterprise_sonic.tests.unit.modules.utils import (
    set_module_args,
)
from .sonic_module import TestSonicModule


class TestSonicCoppModule(TestSonicModule):
    module = sonic_copp

    @classmethod
    def setUpClass(cls):
        cls.mock_facts_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.facts.copp.copp.edit_config"
        )
        cls.mock_config_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.copp.copp.edit_config"
        )
        cls.mock_utils_edit_config = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.bgp_utils.edit_config"
        )
        cls.mock_get_interface_naming_mode = patch(
            "ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.utils.utils.get_device_interface_naming_mode"
        )
        cls.fixture_data = cls.load_fixtures('sonic_copp.yaml')

    def setUp(self):
        super(TestSonicCoppModule, self).setUp()
        self.facts_edit_config = self.mock_facts_edit_config.start()
        self.config_edit_config = self.mock_config_edit_config.start()
        self.facts_edit_config.side_effect = self.facts_side_effect
        self.config_edit_config.side_effect = self.config_side_effect
        self.get_interface_naming_mode = self.mock_get_interface_naming_mode.start()
        self.get_interface_naming_mode.return_value = 'native'
        self.utils_edit_config = self.mock_utils_edit_config.start()
        self.utils_edit_config.side_effect = self.facts_side_effect

    def tearDown(self):
        super(TestSonicCoppModule, self).tearDown()
        self.mock_facts_edit_config.stop()
        self.mock_config_edit_config.stop()
        self.mock_get_interface_naming_mode.stop()
        self.mock_utils_edit_config.stop()

    def test_sonic_copp_merged_01(self):
        set_module_args(self.fixture_data['merged_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['merged_01']['existing_copp_config'])
        self.initialize_config_requests(self.fixture_data['merged_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_copp_replaced_01(self):
        set_module_args(self.fixture_data['replaced_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['replaced_01']['existing_copp_config'])
        self.initialize_config_requests(self.fixture_data['replaced_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_copp_overridden_01(self):
        set_module_args(self.fixture_data['overridden_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_01']['existing_copp_config'])
        self.initialize_config_requests(self.fixture_data['overridden_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_copp_overridden_02(self):
        set_module_args(self.fixture_data['overridden_02']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['overridden_02']['existing_copp_config'])
        self.initialize_config_requests(self.fixture_data['overridden_02']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()

    def test_sonic_copp_deleted_01(self):
        set_module_args(self.fixture_data['deleted_01']['module_args'])
        self.initialize_facts_get_requests(self.fixture_data['deleted_01']['existing_copp_config'])
        self.initialize_config_requests(self.fixture_data['deleted_01']['expected_config_requests'])
        result = self.execute_module(changed=True)
        self.validate_config_requests()
