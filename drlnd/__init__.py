#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The __init__.py files are required to make Python treat the directories as
containing packages; this is done to prevent directories with a common name,
such as string, from unintentionally hiding valid modules that occur later
(deeper) on the module search path.


@author: ucaiado

Created on 10/06/2018
"""

from .utils.make_env import make
from .ddpg.agent import MultiAgent as MADDPG
from .ddpg.agent import PARAMS as MADDPG_PARAMS
