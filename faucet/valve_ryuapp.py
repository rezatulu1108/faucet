"""RyuApp base class for FAUCET/Gauge."""

# Copyright (C) 2013 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2015 Brad Cowie, Christopher Lorier and Joe Stringer.
# Copyright (C) 2015 Research and Education Advanced Network New Zealand Ltd.
# Copyright (C) 2015--2017 The Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

from ryu.base import app_manager
from ryu.lib import hub
from faucet import valve_of
from faucet.valve_util import get_setting


class RyuAppBase(app_manager.RyuApp):
    """RyuApp base class for FAUCET/Gauge."""

    OFP_VERSIONS = valve_of.OFP_VERSIONS
    logname = ''

    @staticmethod
    def _thread_jitter(period, jitter=3):
        """Reschedule another thread with a random jitter."""
        hub.sleep(period + random.randint(0, jitter))

    def get_setting(self, setting):
        return get_setting('_'.join((self.logname, setting)))
