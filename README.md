# thedivisiontab-py
A Python wrapper for the The Division Tab API
# Usage
```python
>> from thedivisiontab_py.thedivisiontab_py import user

# Default platform: uplay
# Platforms: uplay, psn, xbl
>> result = await user.get_by_name("Dhs92", "uplay")
# expected output
# https://paste.dhs92.me/neyisekiqi.json

# only accepts a uplay pid
>> result = await user.get_by_id("")
# expected output
# https://paste.dhs92.me/owucazolur.json
