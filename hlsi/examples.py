"""TODO: Add docstring."""
from integrator import Communication, Interface, Kernel, Stream, Task

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
            Interface.__init__(self, name, data=32, enable=1, ready=1)
            self.add_modport('blockL', 'o_data', 'i_enable', 'o_ready')
            self.add_modport('blockR', 'i_data', 'o_enable', 'i_ready')

    # block config, suppose to be load from pragma
    knl0 = Kernel('knl0')
    knl0.config_interface('in_infc',
                          'blockR',
                          data='k0_dataL',
                          enable='k0_enableL',
                          ready='k0_readyL')
    knl0.config_interface('out_infc',
                          'blockL',
                          data='k0_dataR',
                          enable='k0_enableR',
                          ready='k0_readyR')
    knl0.config_clk('k0_clk')

    knl1 = Kernel('knl1')
    knl1.config_interface('in_infc',
                          'blockR',
                          data='k1_dataL',
                          enable='k1_enableL',
                          ready='k1_readyL')
    knl1.config_interface('out_infc',
                          'blockL',
                          data='k1_dataR',
                          enable='k1_enableR',
                          ready='k1_readyR')
    knl1.config_clk('k1_clk')

    myinfc0 = Myinfc('myinfc0')
    myinfc1 = Myinfc('myinfc1')
    myinfc2 = Myinfc('myinfc2')
    myTask = Task() \
        .invoke(knl0, in_infc=myinfc0, out_infc=myinfc1) \
        .invoke(knl1, in_infc=myinfc1, out_infc=myinfc2)
    myTask.add_io(myinfc0, 'blockR')
    myTask.add_io(myinfc2, 'blockL')
    myTask.to_verilog('wrapper.v')

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

    # myTask = Task() \
    #     .invoke(knl0, mycomm0, mycomm1, strm) \
    #     .invoke(knl0, strm, mycomm2)

    # myTask.to_verilog('wrapper/folder/path')
