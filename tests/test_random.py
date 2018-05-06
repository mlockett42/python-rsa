import unittest
import rsa
import rsa.randnum
import random
import struct

class TestCustomRandom(unittest.TestCase):
    def test_custom_random_function(self):
        def custom_random(bytes):
            l = [random.randrange(256) for i in xrange(bytes)]
            return str(bytearray(l))

        random.seed(2)
        rsa.set_custom_urandom(custom_random)

        ret = rsa.randnum.read_random_bits(32)

        assert ret == '\xf4\xf2\x0e\x15'

            
        
