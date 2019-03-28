# MIT License
#
# Copyright (c) 2019 Alex Forehand
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import urllib.parse
import urllib.request

import exceptions


# Takes user name and platform as arguments. Options are "uplay", "psn", and "xbl"
# Defaults: platform: uplay
# Request is returned as JSON and stored in a dictionary
async def get_by_name(name, platform="uplay") -> dict:
    name = urllib.parse.quote(name)
    platform = platform.lower()

    if platform not in ("uplay", "psn", "xbl"):
        raise ValueError(f"Expected uplay, psn, or xbl but got {platform}")

    data = urllib.request.urlopen(f"https://thedivisiontab.com/api/"
                                  f"search.php?name={name}&platform={platform}")
    if data['totalresults'] is 0:
        raise exceptions.NoResultsFound("No results found")

    return data


# Takes uplay user ID as the only argument
# Defaults: none
# Request is returned as JSON and stored in a dictionary
async def get_by_id(user_id) -> dict:
    user_id = urllib.parse.quote(user_id)
    data = urllib.request.urlopen(f"https://thedivisiontab.com/api/"
                                  f"search.php?pid={user_id}")

    if data['totalresults'] is 0:
        raise exceptions.NoResultsFound("No results found")

    return data
