from random import randint


class my_randint:
    def __init__(self, rand_number_list_length=40):
        self.list_pointer = 0
        self.list_length = rand_number_list_length
        self.rand_number_list = [randint(0, 4294967295)
                                 for i in range(rand_number_list_length)]

    def re_init(self, rand_number_list_length=-1):
        if rand_number_list_length == -1:
            rand_number_list_length = self.list_length
        else:
            self.list_length = rand_number_list_length
        self.list_pointer = 0
        self.rand_number_list = [randint(0, 4294967295)
                                 for i in range(rand_number_list_length)]

    def __call__(self, start_integer, end_integer):
        res = self.rand_number_list[self.list_pointer]
        self.list_pointer = self.list_pointer + 1
        if self.list_pointer == self.list_length:
            self.list_pointer = 0
        return start_integer + res % (end_integer - start_integer + 1)
