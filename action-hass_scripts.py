#!/usr/bin/env python3

import requests
from functools import partial

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology.dialogue.intent import IntentMessage


CONFIG_INI = "config.ini"
DEFAULT_MQTT_ADDR = "localhost:1883"

# Config keys
INTENTS = "intents"
MQTT = "mqtt"
BROKER = "broker"
HASS = "hass"
API_URL = "api_url"
AUTH_TOKEN = "auth_token"


class HassScripts(object):
    def __init__(self):
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except Exception as e:
            print("[Error] Failed to parse config {}".format(e))
            self.config = {MQTT: {}, HASS: {}, INTENTS: {}}

        for c in (API_URL, AUTH_TOKEN):
            if c not in self.config[HASS]:
                print("[Error] Required hass config not present: {}".format(c))

        if not self.config[INTENTS]:
            print("[Error] No intents configured")

        self.start_blocking()

    def common(self, script: str, hermes: Hermes, intent_message: IntentMessage):
        hermes.publish_end_session(intent_message.session_id, "")

        url = "{}/services/script/turn_on".format(self.config[HASS].get(API_URL))
        headers = {
            "Authorization": "Bearer {}".format(self.config[HASS].get(AUTH_TOKEN)),
            "Content-Type": "application/json",
        }
        post_data = {"entity_id": "script.{}".format(script)}

        resp = requests.post(url, headers=headers, json=post_data)
        if resp.status_code != 200:
            print(
                "[Error] Request to {} returned: '{} {}'".format(
                    url, resp.status_code, resp.reason
                )
            )

    def start_blocking(self):
        print(self.config)
        with Hermes(self.config[MQTT].get(BROKER, DEFAULT_MQTT_ADDR)) as h:
            for intent, script in self.config[INTENTS].items():
                h.subscribe_intent(intent, partial(self.common, script))
            h.loop_forever()


if __name__ == "__main__":
    HassScripts()
