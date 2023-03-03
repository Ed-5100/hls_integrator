/* Machine-generated using Migen */
module Block_Memory(
	input wen_s,
	input ren_s,
	input [31:0] addr_s,
	input [31:0] datw_s,
	output [31:0] datr_s,
	input sys_clk,
	input sys_rst
);

wire [2:0] adr;
wire [31:0] dat_r;
wire we;
wire [31:0] dat_w;
wire re;
wire [31:0] slice_proxy;

// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign adr = slice_proxy[2:0];
assign we = wen_s;
assign re = ren_s;
assign dat_w = datw_s;
assign datr_s = dat_r;
assign slice_proxy = (addr_s >>> 2'd2);

reg [31:0] bram[0:7];
reg [2:0] memadr;
always @(posedge sys_clk) begin
	if (we)
		bram[adr] <= dat_w;
	if (re)
		memadr <= adr;
end

assign dat_r = bram[memadr];

endmodule
