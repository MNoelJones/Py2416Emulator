from BitVector import BitVector


class BitArray(BitVector):
	def __init__(self, value=0, size=8):
		super(self.__class__, self).__init__(intVal=value, size=size)
		self._bitsize = size

	def hex(self):
		return self.get_bitvector_in_hex()

	@property
	def value(self):
		return self.int_val()

	@value.setter
	def value(self, new_val):
		self.set_value(intVal=new_val, size=self._bitsize)

	def set_bit(self, bit_number):
		assert bit_number < self._bitsize, "Attempt to set bit out of register size range"
		self |= BitVector(intVal=2**bit_number, size=self._bitsize)

	def unset_bit(self, bit_number):
		assert bit_number < self._bitsize, "Attempt to unset bit out of register size range"
		self &= ~BitVector(intVal=2**bit_number, size=self._bitsize)

	def isset(self, bit_number):
		assert bit_number < self._bitsize, "Attempt to test bit out of register size range"
		return ((self & BitVector(intVal=2**bit_number, size=self._bitsize)).int_val() != 0)

	def isunset(self, bit_number):
		assert bit_number < self._bitsize, "Attempt to test bit out of register size range"
		return not self.isset(bit_number)

class Word(BitArray):
	def __init__(self, value=0, size=3):
		super(self.__class__, self).__init__(value=value, size=size*8)
		self._bitsize = size*8

	def __str__(self):
		return self.value.hex()

	#def set_bit(self, bit_number):
		#self._value.set_bit(bit_number)

	#def unset_bit(self, bit_number):
		#self._value.unset_bit(bit_number)

	@property
	def value(self):
		return self.value

	@value.setter
	def value(self, new_val):
		self.value = new_val

class RAM(object):
	def __init__(self, words):
		self._memory = [Word() for _ in range(words)]
		self._size = words

	def __str__(self):
		out_str = ""
		first = True
		for word in self._memory:
			out_str += (" " if first else "") + str(word)
		return out_str

	def __getitem__(self, index):
		return self._memory[index]

class ALU(object):
	def __init__(self):
		self._temp_input_register = Register(value=0, bits=2*8)

	def __str__(self):
		return str(self._temp_input_register)


class Register(BitArray):
	def __init__(self, value=0, bits=3):
		self._bitsize = bits
		self._value = BitVector(intVal=value, size=self._bitsize)

	def __str__(self):
		return str(self._value)

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_val):
		self._value.set_value(new_val)

class Bus(Register):
	pass


class Processor(object):
	def __init__(self):
		self._accumulator = Register(bits=24)
		self._program_counter = Register(bits=16)
		self._instruction_register = Register(bits=24)
		self._address_bus = Bus(bits=16)
		self._data_bus = Bus(bits=16)
		self._ram = RAM(8)
		self._alu = ALU()
		self._status = {"carry": BitVector(size=1), "zero": BitVector(size=1)}

class RTL(object):
	class Instruction(object):
		def __init__(self, processor=None, op1=None, op2=None):
			self._processor = processor
			self._operands = [op1, op2]

		def __call__(self):
			pass

	class SetRegister(Instruction):
		def __init__(self, processor=None, op1=None, op2=None):
			super(self.__class__, self).__init__(processor, op1, op2)

		def __call__(self):
			""" op1 is the register to be assigned to, op2 is the value to be assigned """
			if isinstance(self._operands[1], BitArray):
				self._operands[0].value = self._operands[1].value
			else:
				self._operands[0].value = self._operands[1]

class Instruction(object):
	def __init__(self):
		self._name = None
		self._params = []
		self._rtl = []


class Program(object):
	def __init__(self, file=None):
		self._program = []
		if file is not None:
			self.load_program(file)

	def load_program(self, file):
		pass
