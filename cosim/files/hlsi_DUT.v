/* Machine-generated using Migen */
module top(
	input sys_clk,
	input sys_rst
);

wire bram_intf_in_1_wen;
wire bram_intf_in_1_ren;
wire [31:0] bram_intf_in_1_addr;
wire [31:0] bram_intf_in_1_data_r;
wire [31:0] bram_intf_in_1_data_w;
wire bram_intf_in_2_wen;
wire bram_intf_in_2_ren;
wire [31:0] bram_intf_in_2_addr;
wire [31:0] bram_intf_in_2_data_r;
wire [31:0] bram_intf_in_2_data_w;
wire bram_intf_out_wen;
wire bram_intf_out_ren;
wire [31:0] bram_intf_out_addr;
wire [31:0] bram_intf_out_data_r;
wire [31:0] bram_intf_out_data_w;
wire ctrl_intf_1_done;
wire ctrl_intf_1_idle;
wire ctrl_intf_1_ready;
wire ctrl_intf_1_start;


vadd vadd(
	.ap_clk(sys_clk),
	.ap_rst(sys_rst),
	.ap_start(ctrl_intf_1_start),
	.in1_Dout_A(bram_intf_in_1_data_r),
	.in2_Dout_A(bram_intf_in_2_data_r),
	.out_r_Dout_A(bram_intf_out_data_r),
	.ap_done(ctrl_intf_1_done),
	.ap_idle(ctrl_intf_1_idle),
	.ap_ready(ctrl_intf_1_ready),
	.in1_Addr_A(bram_intf_in_1_addr),
	.in1_Din_A(bram_intf_in_1_data_w),
	.in1_EN_A(bram_intf_in_1_ren),
	.in1_WEN_A(bram_intf_in_1_wen),
	.in2_Addr_A(bram_intf_in_2_addr),
	.in2_Din_A(bram_intf_in_2_data_w),
	.in2_EN_A(bram_intf_in_2_ren),
	.in2_WEN_A(bram_intf_in_2_wen),
	.out_r_Addr_A(bram_intf_out_addr),
	.out_r_Din_A(bram_intf_out_data_w),
	.out_r_EN_A(bram_intf_out_ren),
	.out_r_WEN_A(bram_intf_out_wen)
);

ctrl ctrl(
	.adder_done(ctrl_intf_1_done),
	.adder_idle(ctrl_intf_1_idle),
	.adder_ready(ctrl_intf_1_ready),
	.clk(sys_clk),
	.rst(sys_rst),
	.adder_start(ctrl_intf_1_start)
);

Block_Memory Block_Memory(
	.addr_s(bram_intf_in_1_addr),
	.datw_s(bram_intf_in_1_data_w),
	.ren_s(bram_intf_in_1_ren),
	.sys_clk(sys_clk),
	.sys_rst(sys_rst),
	.wen_s(bram_intf_in_1_wen),
	.datr_s(bram_intf_in_1_data_r)
);

Block_Memory Block_Memory_1(
	.addr_s(bram_intf_in_2_addr),
	.datw_s(bram_intf_in_2_data_w),
	.ren_s(bram_intf_in_2_ren),
	.sys_clk(sys_clk),
	.sys_rst(sys_rst),
	.wen_s(bram_intf_in_2_wen),
	.datr_s(bram_intf_in_2_data_r)
);

Block_Memory Block_Memory_2(
	.addr_s(bram_intf_out_addr),
	.datw_s(bram_intf_out_data_w),
	.ren_s(bram_intf_out_ren),
	.sys_clk(sys_clk),
	.sys_rst(sys_rst),
	.wen_s(bram_intf_out_wen),
	.datr_s(bram_intf_out_data_r)
);

endmodule
