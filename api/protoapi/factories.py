# -*- encoding: utf-8 -*-

import factory
from faker import Factory as FakerFactory

from protoapi.models import (
        Record, 
        Type, 
        User, 
)

faker = FakerFactory.create()
faker.seed(983843)