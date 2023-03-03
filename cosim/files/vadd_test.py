"""TODO: Add docstring."""

from integrator import Interface, Kernel, Task


class bram_intf(Interface):
    """TODO: Add docstring."""

    def __init__(self, name):
        """TODO: Add docstring."""
        Interface.__init__(self,
                           name,
                           wen=1,
                           ren=1,
                           addr=32,
                           data_r=32,
                           data_w=32)
        self.add_modport('block', 'o_wen', 'o_ren', 'o_addr', 'i_data_r',
                         'o_data_w')
        self.add_modport('mem', 'i_wen', 'i_ren', 'i_addr', 'o_data_r',
                         'i_data_w')


class ctrl_intf(Interface):
    """TODO: Add docstring."""

    def __init__(self, name):
        """TODO: Add docstring."""
        Interface.__init__(self, name, done=1, idle=1, ready=1, start=1)
        self.add_modport('fsm', 'i_done', 'i_idle', 'i_ready', 'o_start')
        self.add_modport('dp', 'o_done', 'o_idle', 'o_ready', 'i_start')


in_mem1 = Kernel('Block_Memory')
in_mem1.config_clk('sys_clk')
in_mem1.config_rst('sys_rst')
in_mem1.config_interface('intf',
                         'mem',
                         wen='wen_s',
                         ren='ren_s',
                         addr='addr_s',
                         data_r='datr_s',
                         data_w='datw_s')

in_mem2 = Kernel('Block_Memory')
in_mem2.config_clk('sys_clk')
in_mem2.config_rst('sys_rst')
in_mem2.config_interface('intf',
                         'mem',
                         wen='wen_s',
                         ren='ren_s',
                         addr='addr_s',
                         data_r='datr_s',
                         data_w='datw_s')

out_mem = Kernel('Block_Memory')
out_mem.config_clk('sys_clk')
out_mem.config_rst('sys_rst')
out_mem.config_interface('intf',
                         'mem',
                         wen='wen_s',
                         ren='ren_s',
                         addr='addr_s',
                         data_r='datr_s',
                         data_w='datw_s')

vadd = Kernel('vadd')
vadd.config_clk('ap_clk')
vadd.config_rst('ap_rst')
vadd.config_interface('inmem1',
                      'block',
                      wen='in1_WEN_A',
                      ren='in1_EN_A',
                      addr='in1_Addr_A',
                      data_r='in1_Dout_A',
                      data_w='in1_Din_A')
vadd.config_interface('inmem2',
                      'block',
                      wen='in2_WEN_A',
                      ren='in2_EN_A',
                      addr='in2_Addr_A',
                      data_r='in2_Dout_A',
                      data_w='in2_Din_A')
vadd.config_interface('outmem',
                      'block',
                      wen='out_r_WEN_A',
                      ren='out_r_EN_A',
                      addr='out_r_Addr_A',
                      data_r='out_r_Dout_A',
                      data_w='out_r_Din_A')
vadd.config_interface('ctrl',
                      'dp',
                      done='ap_done',
                      start='ap_start',
                      idle='ap_idle',
                      ready='ap_ready')

ctrl = Kernel('ctrl')
ctrl.config_clk('clk')
ctrl.config_rst('rst')
ctrl.config_interface('ctrl',
                      'fsm',
                      done='adder_done',
                      start='adder_start',
                      idle='adder_idle',
                      ready='adder_ready')

bram_intf_in_1 = bram_intf('bram_intf_in_1')
bram_intf_in_2 = bram_intf('bram_intf_in_2')
bram_intf_out = bram_intf('bram_intf_out')
ctrl_intf_1 = ctrl_intf('ctrl_intf_1')

dut = Task()\
        .invoke(vadd,
                inmem1=bram_intf_in_1,
                inmem2=bram_intf_in_2,
                outmem=bram_intf_out,
                ctrl=ctrl_intf_1
                )\
        .invoke(ctrl,
                ctrl=ctrl_intf_1)\
        .invoke(in_mem1,
                intf=bram_intf_in_1)\
        .invoke(in_mem2,
                intf=bram_intf_in_2)\
        .invoke(out_mem,
                intf=bram_intf_out)\
        .to_verilog('hlsi_DUT.v')
