"""TODO: Add docstring."""
from migen.fhdl.module import Module
from migen.fhdl.structure import Signal
# from migen.fhdl.verilog import conve
from migen.genlib.fifo import SyncFIFO


class Interface():
    """TODO: Add docstring."""

    # port direction for connected kernel
    def __init__(self, name, **kwargs):
        """TODO: Add docstring."""
        self.name = name
        self.io = {}
        for key in kwargs:
            self.io[key] = kwargs[key]
        self.mode_ports = {}

    def add_mode_port(self, name, *args):
        """TODO: Add docstring."""
        i_ports = []
        o_ports = []
        assert len(
            args
        ) == self.io, \
            'length of mode port io needs to be the same as interface io'
        for i in args:
            port_type, port = i.split('_', maxsplit=1)
            assert port in self.io, 'port {} not found'.format(port)
            if port_type == 'i':
                i_ports.append(port)
            if port_type == 'o':
                o_ports.append(port)
            self.mode_ports[name] = {'i': i_ports, 'o': o_ports}

    def get_mode_port(self, name):
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
        istream.add_mode_port(
            'kernel',
            'o_strm_in_dout',
            'o_strm_in_empty_n',
            'i_strm_in_read',
        )
        istream.add_mode_port(
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
        ostream.add_mode_port(
            'kernel',
            'o_strm_out_din',
            'i_strm_out_full_n',
            'o_strm_out_write',
        )
        ostream.add_mode_port(
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
                SyncFIFO.__init__(width, depth)
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

    def __init__(self):
        """TODO: Add docstring."""
        self.interfaces = {'infc': [], 'mode_port': []}

    # read parsed file for port_group information
    def load_config(identifier, type, file):
        """TODO: Add docstring."""

    def config_interface(self, interface, mode_port, **kwargs):
        """TODO: Add docstring."""
        # self.infc


class Task():
    """TODO: Add docstring."""

    def __init__(self):
        """TODO: Add docstring."""
        self.block = {'kernels': [], 'interfaces': []}
        self.interface_set = set()

    def invoke(self, kernel, *args):
        """TODO: Add docstring."""
        self.block['kernels'].append(kernel)
        self.block['interfaces'].append([
            interface for interface in args
            if interface.__class__.__name__ == Interface
        ])
        self.block['communications'].append([
            communication for communication in args
            if communication.__class__.__name__ == Communication
        ])
        for infc in args:
            if infc.__class__.__name__ == Interface:
                if infc not in self.interface_set:
                    self.interface_set.add(infc)

    def to_verilog(self, path):
        """TODO: Add docstring."""

    def to_migen(self):
        """TODO: Add docstring."""
        interface_set = self.interface_set
        block = self.block

        # convert to migen
        class Wrapper(Module):
            """TODO: Add docstring."""

            def __init__(self):
                """TODO: Add docstring."""
                signal_dic = {}
                for infc in interface_set:
                    for port_name in infc.io:
                        signal_name = '{}_{}'.format(infc.name, port_name)
                        signal_dic[signal_name] = Signal(infc.io[port_name])

                for idx in range(len(block['kernels'])):
                    pass
