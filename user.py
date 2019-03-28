import urllib.parse
import urllib.request


# Takes user name and platform as arguments. Options are "uplay", "psn", and "xbl"
# Defaults: platform: uplay
# Request is returned as JSON and stored in a dictionary
async def get_by_name(name, platform="uplay") -> dict:
    name = urllib.parse.quote(name)
    platform = platform.lower()

    try:
        if (platform == "uplay") or (platform == "psn") or (platform == "xbl"):
            data = urllib.request.urlopen(f"https://thedivisiontab.com/api/"
                                          f"search.php?name={name}&platform={platform}")
        else:
            raise ValueError(f"Expected uplay, psn, or xbl but got {platform}")

    except AssertionError as error:
        print(error)

    else:
        return data


# Takes uplay user ID as the only argument
# Request is returned as JSON and stored in a dictionary
async def get_by_id(user_id) -> dict:
    try:
        user_id = urllib.parse.quote(user_id)
        data = urllib.request.urlopen(f"https://thedivisiontab.com/api/"
                                      f"search.php?pid={user_id}")
    except AssertionError as error:
        print(error)

    else:
        return data


def _check_results(result_total):
    assert (result_total != 0), "No results found"
