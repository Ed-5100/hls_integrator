"""TODO: Add docstring."""

from typing import Optional

from migen.fhdl.module import Module
from migen.fhdl.specials import Instance
from migen.fhdl.structure import ClockSignal, ResetSignal, Signal
from migen.fhdl.verilog import convert
from migen.genlib.fifo import SyncFIFO


class Interface():
    """TODO: Add docstring."""

    # ====================================================
    # Interface Class
    # self.name:       name of interface object, need to be unique
    # self.modports:   dict('name':{'i':[strs], 'o':[strs]})
    # self.kernal_map: dict(modport:kernal) ???
    # ====================================================

    # port direction for connected kernel
    def __init__(self, name, **kwargs):
        """TODO: Add docstring."""
        self.name = name
        self.io = {}
        for key in kwargs:
            self.io[key] = kwargs[key]
        self.modports = {}

    def add_modport(self, name, *args):
        """TODO: Add docstring."""
        i_ports = []
        o_ports = []
        assert len(args) == len(self.io), \
            'length of modport io needs to be the same as interface io'

        assert len(self.modports) <= 2, \
            'modport cannot be more than 2'

        for i in args:
            port_type, port = i.split('_', maxsplit=1)
            assert port in self.io, 'port {} not found'.format(port)
            if port_type == 'i':
                i_ports.append(port)
            if port_type == 'o':
                o_ports.append(port)
            self.modports[name] = {'i': i_ports, 'o': o_ports}

    def get_modport(self, name):
        """TODO: Add docstring."""
        return


class Communication():
    """TODO: Add docstring."""

    def __init__(self, **kwargs):
        """TODO: Add docstring."""
        self.type = None
        self.interfaces = {}
        for intf_name in kwargs:
            self.interfaces[intf_name] = kwargs[intf_name]

    def load_verilog(self, source, ios):
        """TODO: Add docstring."""

    def load_migen_module(self, module, ios):
        """TODO: Add docstring."""
        self.type = 'm'
        self.module = module
        self.ios = ios

    def get_infc(self, interface):
        """TODO: Add docstring."""


class Stream(Communication):
    """TODO: Add docstring."""

    def __init__(self, width, depth):
        """TODO: Add docstring."""
        istream = Interface(
            'istream',
            strm_in_dout=width,
            strm_in_empty_n=1,
            strm_in_read=1,
        )
        istream.add_modport(
            'kernel',
            'o_strm_in_dout',
            'o_strm_in_empty_n',
            'i_strm_in_read',
        )
        istream.add_modport(
            'fifo',
            'i_strm_in_dout',
            'i_strm_in_empty_n',
            'o_strm_in_read',
        )

        ostream = Interface(
            'ostream',
            strm_out_din=width,
            strm_out_full_n=1,
            strm_out_write=1,
        )
        ostream.add_modport(
            'kernel',
            'o_strm_out_din',
            'i_strm_out_full_n',
            'o_strm_out_write',
        )
        ostream.add_modport(
            'fifo',
            'i_strm_out_din',
            'o_strm_out_full_n',
            'i_strm_out_write',
        )

        Communication.__init__(self,
                               istream=(istream, 'fifo'),
                               ostream=(ostream, 'fifo'))

        class fifo(SyncFIFO):
            """TODO: Add docstring."""

            def __init__(self, width, depth):
                SyncFIFO.__init__(self, width, depth)
                self.dout
                self.readable
                self.re
                self.din
                self.writable
                self.we
                self.ios = {
                    'istream':
                    ['strm_in_dout', 'strm_in_empty_n', 'strm_in_read'],
                    'ostream':
                    ['strm_out_din', 'strm_out_full_n', 'strm_out_write']
                }

        myfifo = fifo(width, depth)
        self.load_migen_module(myfifo, myfifo.ios)


class Kernel():
    """TODO: Add docstring."""

    # ====================================================
    # Kernel Class
    # self.interfaces['infc']:
    #   [infc_name->str,] name of interfaces. unique within kernal
    #
    # self.interfaces['modport']:
    #   [modport_name->str,] name of modport. corresponding index with infc
    #
    # self.interfaces['io']:
    #   [{infc_port->str:kernal_io->str},]
    # ====================================================

    class Connection:
        """TODO: Add docstring."""

        def __init__(self, knl_infc_name, infc, modport):
            """TODO: Add docstring."""
            self.knl_infc_name = knl_infc_name
            self.infc = infc
            self.modport = modport

    interfaces: dict
    connections: list[Connection]
    clk: Optional[str]
    rst: Optional[str]

    def __init__(self, name: str):
        """TODO: Add docstring."""
        self.name = name
        self.interfaces = {'infc_name': [], 'modport': [], 'io': []}
        self.connections = []
        self.clk = None
        self.rst = None

    # read parsed file for port_group information
    def load_config(self, identifier, type, file):
        """TODO: Add docstring."""

    def config_interface(self, interface: str, modport: str, **kwargs):
        """TODO: Add docstring."""
        self.interfaces['infc_name'].append(interface)
        self.interfaces['modport'].append(modport)
        infc_ios = {}
        for key in kwargs:
            infc_ios[key] = kwargs[key]
        self.interfaces['io'].append(infc_ios)

    def config_clk(self, knl_clk: Optional[str]):
        """TODO: Add docstring."""
        self.clk = knl_clk

    def config_rst(self, knl_rst: Optional[str]):
        """TODO: Add docstring."""
        self.rst = knl_rst


class Task():
    """TODO: Add docstring."""

    # ====================================================
    # Task Class
    # self.block['kernels']:      [Kernal,]
    # self.block['interfaces']:   [[Interface,],]
    # self.interface_set:         a set of all interfaces in the task
    # ====================================================

    def __init__(self):
        """TODO: Add docstring."""
        self.kernals = []
        self.interfaces = []
        self.io = []

    def invoke(self, kernel: Kernel, **kwargs: Interface):
        """TODO: Add docstring."""
        self.kernals.append(kernel)
        for knl_infc_name in kwargs:
            infc_obj = kwargs[knl_infc_name]
            modport = kernel.interfaces['modport'][
                kernel.interfaces['infc_name'].index(knl_infc_name)]
            kernel.connections.append(
                kernel.Connection(knl_infc_name, infc_obj, modport))
            if infc_obj not in self.interfaces:
                self.interfaces.append(infc_obj)
        return self

    def add_io(self, infc: Interface, modport: str):
        """TODO: Add docstring."""
        self.io.append((infc, modport))

    def to_verilog(self, path):
        """TODO: Add docstring."""
        wrapper = self.to_migen()
        convert(wrapper, wrapper.io).write(path)

    def to_migen(self):
        """TODO: Add docstring."""
        interfaces = self.interfaces
        kernals = self.kernals
        io = self.io
        return self.__Wrapper(kernals, interfaces, io)

    # wrapper inner class
    class __Wrapper(Module):
        """TODO: Add docstring."""

        def __init__(self, kernals: list[Kernel], interfaces: list[Interface],
                     io: list[tuple[Interface, str]]):
            """TODO: Add docstring."""
            self.io = set()
            signal_dic = {}
            for infc in interfaces:
                for port_name in infc.io:
                    signal_name = '{}_{}'.format(infc.name, port_name)
                    signal_dic[signal_name] = Signal(infc.io[port_name],
                                                     name_override=signal_name)

            for knl in kernals:
                wire_connection_dic = {}
                if knl.clk is not None:
                    wire_connection_dic['i_{}'.format(knl.clk)] = ClockSignal()
                if knl.rst is not None:
                    wire_connection_dic['i_{}'.format(knl.rst)] = ResetSignal()

                for infc_connect in knl.connections:
                    infc = infc_connect.infc
                    modport = infc_connect.modport
                    knl_infc_name = infc_connect.knl_infc_name
                    idx = knl.interfaces['infc_name'].index(knl_infc_name)
                    infc_ios = knl.interfaces['io'][idx]
                    for infc_wire in infc_ios:
                        knl_wire = infc_ios[infc_wire]
                        if infc_wire in infc.modports[modport]['i']:
                            direction = 'i'
                        elif infc_wire in infc.modports[modport]['o']:
                            direction = 'o'
                        else:
                            raise Exception(
                                'kernal interface not'
                                'match to interface object: {}'.format(
                                    infc_wire))
                        wire_connection_dic['{}_{}'.format(
                            direction, knl_wire)] = signal_dic['{}_{}'.format(
                                infc.name, infc_wire)]

                self.specials += Instance(knl.name, **wire_connection_dic)

            for io_infc, modport in io:
                for i_port in io_infc.modports[modport]['i']:
                    io_sig = signal_dic['{}_{}'.format(io_infc.name, i_port)]
                    self.io.add(io_sig)
                for o_port in io_infc.modports[modport]['o']:
                    io_sig = signal_dic['{}_{}'.format(io_infc.name, o_port)]
                    self.io.add(io_sig)
