class Word(object):
      def __init__(self, value=0, size=3):
         # Currently assumes size = 3...
         self._value = bytearray([value&0xFF0000>>16, value & 0x00FF00 >> 8, value & 0xFF])

class RAM(object):
   def __init__(self, words):
      self._memory = [Word() for _ in range(words)]
      self._size = words

class ALU(object):
   def __init__(self):
      self._temp_input_register = Register(value=0, size=2)
      pass

class Register(object):
   def __init__(self, value=0, size=3):
      self._size = size
      self._value = vlaue

class Processor(object):
   def __init__(self):
      self._accumulator = Register(size=3)
      self._program_counter = Register(size=2)
      self._instruction_register = Register(size=3)
      self._address_bus = Bus(size=2)
      self._data_bus = Bus(size=2)
      self._ram = RAM()
      self._alu = ALU()
      self._status = {"carry": Bit(), "zero": Bit()}

class Program(object):
   def __init__(self, file=None):
      self._program = []
      if file is not None:
         self.load_program(file)