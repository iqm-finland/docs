# Copyright 2024 IQM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from functools import cached_property

from pydantic import BaseModel, ConfigDict


# Change the behaviour of pydantic globally
class ImmutableBaseModel(BaseModel):
    # Unable to use cached_property
    # https://github.com/pydantic/pydantic/issues/1241
    model_config = ConfigDict(frozen=True, ignored_types=(cached_property,))
