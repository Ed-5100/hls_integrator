"""TODO: Add docstring."""
from integrator import Communication, Interface, Stream, Task

# TODO
knl0 = None
parameter0 = None
parameter1 = None

ex = 0
# example
if ex == 0:
    # ex0 infc
    '''
    Myinfc0>---[knal0]---Myinfc1---[knal1]---Myinfc2
    '''

    class Myinfc(Interface):
        """TODO: Add docstring."""

        def __init__(self, name):
            """TODO: Add docstring."""
            Interface.__init__(name,
                               input0=1,
                               input1=1,
                               output0=1,
                               output1=parameter0,
                               output2=parameter1)
            self.add_mode_port('in'
                               'i_input0', 'i_input1', 'o_output0',
                               'o_output1', 'o_output2')
            self.add_mode_port('out'
                               'o_input0', 'o_input1', 'i_output0',
                               'i_output1', 'i_output2')

    myinfc0 = Myinfc('myinfc0')
    myinfc1 = Myinfc('myinfc1')
    myinfc2 = Myinfc('myinfc2')
    myTask = Task() \
        .invoke(knl0, myinfc0, myinfc1) \
        .invoke(knl0, myinfc1, myinfc2)

elif ex == 1:
    # ex1 comm
    '''
         Mycomm0>-----------|
                            |
                            ===[knal0]-----stream-----[knal1]----->Mycomm2
                            |
         Mycomm1>-----------|
    '''

    # create interface
    class Mycomm(Communication):
        """TODO: Add docstring."""

        def __init__(self, parameter0=1, parameter1=1):
            """TODO: Add docstring."""
            myintf = Interface('myintf',
                               input0=1,
                               input1=1,
                               output0=1,
                               output1=parameter0,
                               output2=parameter1)
            self.add_mode_port('in'
                               'i_input0', 'i_input1', 'o_output0',
                               'o_output1', 'o_output2')
            self.add_mode_port('out'
                               'o_input0', 'o_input1', 'i_output0',
                               'i_output1', 'i_output2')

            Communication.__init__(self,
                                   master=(myintf, 'in'),
                                   slave=(myintf, 'out'))
            Communication.load_verilog('path/to/verilog', 'my_Communication')

    mycomm0 = Mycomm(parameter0=4, parameter1=32)
    mycomm1 = Mycomm(parameter0=4, parameter1=32)
    mycomm2 = Mycomm(parameter0=4, parameter1=32)
    strm = Stream(width=32, depth=8)

    # TODO:
    # knl0 = Kernel('block0', 'path/to/pragma', 'verilog')
    # knl1 = Kernel('block1', 'path/to/hls_report', 'vivado_HLS')

    myTask = Task() \
        .invoke(knl0, mycomm0, mycomm1, strm) \
        .invoke(knl0, strm, mycomm2)

    myTask.to_verilog('wrapper/folder/path')
