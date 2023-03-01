from migen.genlib.fifo import syncFIFO
from migen.fhdl.verilog import convert
from migen.fhdl.module import *

class Interface():
    #port direction for connected kernal
    def __init__(self, name,**kwargs):
        self.name = name
        self.io = {}
        for key in kwargs:
            self.io[key] = kwargs[key]
        self.mode_ports = {}
    
    def add_mode_port(self, name, *args):
        i_ports = []
        o_ports = []
        assert len(kwargs) == self.io, "length of mode port io needs to be the same as interface io"
        for i in args:
            port_type, port = i.split("_", maxsplit = 1)
            assert port in self.io, "port {} not found".format(port)
            if port_type == 'i':
                i_ports.append(port)
            if port_type == 'o':
                o_ports.append(port)
            self.mode_ports[name] = {'i' : i_ports, 'o' : o_ports}

    def get_mode_port(self, name):
        return 


class Communication():
    def __init__(self, **kwargs):
        self.type = None
        self.interfaces = {}
        for intf_name in kwargs:
            self.interfaces[intf_name] = kwargs[intf_name]

    def load_verilog(self, source, ios):
        pass
    
    def load_migen_module(self, module, ios):
        self.type = 'm'
        self.module = module
        self.ios = ios

    def get_infc(self, interface):
        pass


class Stream(Communication):
    def __init__(self, width, depth):
        istream = Interface("istream",
            strm_in_dout    = width,
            strm_in_empty_n = 1,
            strm_in_read    = 1,
        )
        istream.add_mode_port('kernal',
            "o_strm_in_dout",
            "o_strm_in_empty_n",
            "i_strm_in_read",
        )
        istream.add_mode_port('fifo',
            "i_strm_in_dout",
            "i_strm_in_empty_n",
            "o_strm_in_read",
        )

        ostream = Interface("ostream",
            strm_out_din    = width,
            strm_out_full_n = 1,
            strm_out_write  = 1,
        )
        ostream.add_mode_port("kernal",
            "o_strm_out_din",
            "i_strm_out_full_n",
            "o_strm_out_write",
        )
        ostream.add_mode_port("fifo",
            "i_strm_out_din",
            "o_strm_out_full_n",
            "i_strm_out_write",
        )

        Communication.__init__(self, 
            istream = (istream, "fifo"),
            ostream = (ostream, "fifo")
        )

        class fifo(syncFIFO):
            def __init__(self, width, depth):
                syncFIFO.__init__(width,depth)
                strm_in_dout    = self.dout
                strm_in_empty_n = self.readable
                strm_in_read    = self.re
                strm_out_din    = self.din
                strm_out_full_n = self.writable
                strm_out_write  = self.we
                self.ios = {"istream": ["strm_in_dout", "strm_in_empty_n", "strm_in_read"], 
                            "ostream": ["strm_out_din", "strm_out_full_n", "strm_out_write"]}
        
        myfifo = fifo(width, depth)
        Communication.load_migen_module(myfifo, myfifo.ios)


class Kernal():
    def __init__(self):
        self.interfaces = {"infc":[], "mode_port":[]}

    #read parsed file for port_group information
    def load_config(, identifier, type, file):
        pass

    def config_interface(self, interface, mode_port, **kwargs):
        self.infc
    

class Task():
    def __init__(self):
        self.block = {"kernals":[], "interfaces":[]}
        self.interface_set = set()

    def invoke(self, kernal, *args):
        self.block["kernals"].append(kernal)
        self.block["interfaces"].append([interface for interface in args if interface.__class__.__name__ == Interface])
        self.block["communications"].append([communication for communication in args if communication.__class__.__name__ == Communication])
        for infc in args:
            if infc.__class__.__name__ == Interface:
                if not infc in self.interface_set:
                    self.interface_set.add(infc)

    def to_verilog(self, path):
        pass

    def to_migen(self):
        #convert to migen
        class Wrapper(Module):
            def __init__(self):
                signal_dic = {}
                for infc in self.interface_set:
                    for port_name in infc.io:
                        signal_name = "{}_{}".format(infc.name, port_name)
                        signal_dic[signal_name] = Signal(infc.io[port_name])

                for idx in len(self.block["kernals"]):
                    

            



