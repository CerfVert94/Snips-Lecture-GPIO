#!/usr/bin/env python2
import OPiGPIO
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
	"""
	Executes the action prompted by a vocal command.
	The vocal command is analysed and passed as an argument (intent_message)
	
	"""
	# intentName : the name of "intention" supposedly meant by vocal command (chosen by NLU)
	intentName = intent_message.intent.intent_name
	# Probability : the match in percentage between the vocal command and the "intention" chosen by NLU.
	probability = intent_message.intent.probability

	gpio_pin_num = 12
	OPiGPIO.gpio_config_in(gpio_pin_num)

	# Probability thresold should reach 0.9. Otherwise, it's an unknown command
	if intentName == 'Letmeknow:Lire' :
		if probability > 0.5 :
			sentence = OPiGPIO.read_gpio(gpio_pin_num)
		else :
			sentence = " Je n'ai pas compris " + str(probability)
	OPiGPIO.gpio_unexport(gpio_pin_num)
	hermes.publish_end_session(intent_message.session_id, sentence)
with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
