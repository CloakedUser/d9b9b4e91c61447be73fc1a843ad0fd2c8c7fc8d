# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import pprint

from conecli import config
from conecli import _quandl_abstraction


def command_line_main():
    # This is the main CLI entry-point, this is run  from the install
    # binary via PBR.
    config.parse_args()

    # NOTE: Get the function for the report type
    func = _quandl_abstraction.func_for_report()
    output = func(config.SYMBOLS)

    pprint.pprint(output)
