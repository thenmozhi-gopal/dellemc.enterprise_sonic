#
# -*- coding: utf-8 -*-
# Copyright 2024 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The arg spec for the sonic_mac module
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class MacArgs(object):  # pylint: disable=R0903
    """The arg spec for the sonic_mac module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'mac': {
                    'options': {
                        'aging_time': {'default': '600', 'type': 'int'},
                        'dampening_interval': {'default': '5', 'type': 'int'},
                        'dampening_threshold': {'default': '5', 'type': 'int'},
                        'mac_table_entries': {
                            'elements': 'dict',
                            'options': {
                                'interface': {'type': 'str'},
                                'mac_address': {'required': True, 'type': 'str'},
                                'vlan_id': {'required': True, 'type': 'int'}
                            },
                            'type': 'list'
                        }
                    },
                    'type': 'dict'
                },
                'vrf_name': {'default': 'default', 'type': 'str'}
            },
            'type': 'list'
        },
        'state': {'choices': ['merged', 'deleted', 'replaced', 'overridden'], 'default': 'merged', 'type': 'str'}
    }  # pylint: disable=C0301
