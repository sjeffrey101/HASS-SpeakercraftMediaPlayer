"""Support for Speakercraft Party Mode Switch"""
import logging
import asyncio
from homeassistant.core import HomeAssistant
from homeassistant.components.button import ButtonEntity
from .media_player import SpeakerCraftZ
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities, discovery_info=None):

	_LOGGER.debug("async_setup_plaform() entry")
	
	devices = []

	sc = hass.data[DOMAIN].sc
	
	devices.append(SpeakercraftMasterPower(hass, sc.controller))
	
	async_add_entities(devices)
	_LOGGER.debug("async_setup_plaform() exit")
	
		
		
		
class SpeakercraftMasterPower(ButtonEntity):

	def __init__(self, hass: HomeAssistant, controller):

		self._name = "Speakercraft All Zones Off"

		super().__init__()
		self._hass = hass
		self._controller = controller 



	@property
	def name(self):
		"""Return the name of the zone."""
		return self._name


	async def async_press(self, **kwargs) -> None:
		_LOGGER.debug("Master Power Off")
		self._controller.cmdalloff()

