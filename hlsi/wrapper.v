/* Machine-generated using Migen */
module top(
	input [31:0] myinfc0_data,
	output myinfc0_enable,
	input myinfc0_ready,
	output [31:0] myinfc2_data,
	input myinfc2_enable,
	output myinfc2_ready,
	input sys_clk,
	input sys_rst
);

wire [31:0] myinfc1_data;
wire myinfc1_enable;
wire myinfc1_ready;


knl0 knl0(
	.k0_clk(sys_clk),
	.k0_dataL(myinfc0_data),
	.k0_enableR(myinfc1_enable),
	.k0_readyL(myinfc0_ready),
	.k0_dataR(myinfc1_data),
	.k0_enableL(myinfc0_enable),
	.k0_readyR(myinfc1_ready)
);

knl1 knl1(
	.k1_clk(sys_clk),
	.k1_dataL(myinfc1_data),
	.k1_enableR(myinfc2_enable),
	.k1_readyL(myinfc1_ready),
	.k1_dataR(myinfc2_data),
	.k1_enableL(myinfc1_enable),
	.k1_readyR(myinfc2_ready)
);

endmodule
