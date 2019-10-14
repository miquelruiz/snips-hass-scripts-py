## snips-hass-scripts-py

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/snipsco/snips-app-template-py/blob/master/LICENSE)

> This template is made for **_python >= 3.5_**

Snips Voice App to call [Home Assistant scripts](https://www.home-assistant.io/integrations/script) via the REST api.

### Example config.ini
```bash
[intents]
# This is the map from intent to home assistant script. This example subscribes
# to the intent "speakerInterrupt" provided by the "Music Player app" [1], and
# triggers a custom script (which you'll have to create [2]) called "stop_music".
speakerInterrupt=stop_music

# Another example using "SirBuildsALot7:bye" intent provided by the "Greetings"
# app [3], and calling a script named "night_mode".
SirBuildsALot7:bye=night_mode

# You can add as many bindings as you want.
volumeUp=volume_up
HassTurnOff=turn_something_off

[hass]
api_url=http[s]://<your home assistant fqdn>[:port]/api
auth_token=<auth token [4]>

[mqtt]
broker=<optional. Defaults to "localhost:1883">


# [1] https://console.snips.ai/store/en/skill_yloxNXawvV1
# [2] https://www.home-assistant.io/integrations/script
# [3] https://console.snips.ai/store/en/skill_QbxeKklVaDQ
# [4] https://developers.home-assistant.io/docs/en/auth_api.html#long-lived-access-token
```
