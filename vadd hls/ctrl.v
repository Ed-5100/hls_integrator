// Description: ctrl module
// ===========================================================

`timescale 1 ns / 1 ps

module ctrl(
    ap_clk,
    ap_rst,
    ap_start,
    ap_done,
    ap_idle,
    ap_ready,
    grp_add_fu_56_ap_start,
    grp_add_fu_56_ap_done,
    grp_add_fu_56_ap_idle,
    grp_add_fu_56_ap_ready,
    grp_add_fu_56_a_V_read,
    grp_add_fu_56_b_V_read,
    grp_add_fu_56_c_V_write,
    grp_load_fu_63_ap_start,
    grp_load_fu_63_ap_done,
    grp_load_fu_63_ap_idle,
    grp_load_fu_63_ap_ready,
    grp_load_fu_63_a_V_write,
    grp_load_fu_70_ap_start,
    grp_load_fu_70_ap_done,
    grp_load_fu_70_ap_idle,
    grp_load_fu_70_ap_ready,
    grp_load_fu_70_a_V_write,
    grp_store_fu_77_ap_start,
    grp_store_fu_77_ap_done,
    grp_store_fu_77_ap_idle,
    grp_store_fu_77_ap_ready,
    grp_store_fu_77_a_V_read,
    a_V_read,
    a_V_write,
    b_V_read,
    b_V_write,
    c_V_write,
    c_V_read
);

parameter    ap_ST_fsm_state1 = 6'd1;
parameter    ap_ST_fsm_state2 = 6'd2;
parameter    ap_ST_fsm_state3 = 6'd4;
parameter    ap_ST_fsm_state4 = 6'd8;
parameter    ap_ST_fsm_state5 = 6'd16;
parameter    ap_ST_fsm_state6 = 6'd32;

input    ap_clk;
input    ap_rst;

input    ap_start;
output reg    ap_done;
output reg    ap_idle;
output reg    ap_ready;

output    grp_add_fu_56_ap_start;
input    grp_add_fu_56_ap_done;
input    grp_add_fu_56_ap_idle;
input    grp_add_fu_56_ap_ready;
input    grp_add_fu_56_a_V_read;
input    grp_add_fu_56_b_V_read;
input    grp_add_fu_56_c_V_write;

output    grp_load_fu_63_ap_start;
input    grp_load_fu_63_ap_done;
input    grp_load_fu_63_ap_idle;
input    grp_load_fu_63_ap_ready;
input    grp_load_fu_63_a_V_write;

output    grp_load_fu_70_ap_start;
input    grp_load_fu_70_ap_done;
input    grp_load_fu_70_ap_idle;
input    grp_load_fu_70_ap_ready;
input    grp_load_fu_70_a_V_write;

output    grp_store_fu_77_ap_start;
input    grp_store_fu_77_ap_done;
input    grp_store_fu_77_ap_idle;
input    grp_store_fu_77_ap_ready;
input    grp_store_fu_77_a_V_read;
output reg    a_V_read;
output reg    a_V_write;

output reg    b_V_read;
output reg    b_V_write;

output reg    c_V_write;
output reg    c_V_read;


(* fsm_encoding = "none" *) reg   [5:0] ap_CS_fsm;
wire    ap_CS_fsm_state1;
reg    grp_add_fu_56_ap_start_reg;
wire    ap_CS_fsm_state3;
wire    ap_CS_fsm_state4;
reg    grp_load_fu_63_ap_start_reg;
wire    ap_CS_fsm_state2;
reg    grp_load_fu_70_ap_start_reg;
reg    grp_store_fu_77_ap_start_reg;
wire    ap_CS_fsm_state5;
wire    ap_CS_fsm_state6;
reg   [5:0] ap_NS_fsm;
reg    ap_block_state2_on_subcall_done;

// power-on initialization
initial begin
#0 ap_CS_fsm = 6'd1;
#0 grp_add_fu_56_ap_start_reg = 1'b0;
#0 grp_load_fu_63_ap_start_reg = 1'b0;
#0 grp_load_fu_70_ap_start_reg = 1'b0;
#0 grp_store_fu_77_ap_start_reg = 1'b0;
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        ap_CS_fsm <= ap_ST_fsm_state1;
    end else begin
        ap_CS_fsm <= ap_NS_fsm;
    end
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        grp_add_fu_56_ap_start_reg <= 1'b0;
    end else begin
        if ((1'b1 == ap_CS_fsm_state3)) begin
            grp_add_fu_56_ap_start_reg <= 1'b1;
        end else if ((grp_add_fu_56_ap_ready == 1'b1)) begin
            grp_add_fu_56_ap_start_reg <= 1'b0;
        end
    end
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        grp_load_fu_63_ap_start_reg <= 1'b0;
    end else begin
        if (((1'b1 == ap_CS_fsm_state1) & (ap_start == 1'b1))) begin
            grp_load_fu_63_ap_start_reg <= 1'b1;
        end else if ((grp_load_fu_63_ap_ready == 1'b1)) begin
            grp_load_fu_63_ap_start_reg <= 1'b0;
        end
    end
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        grp_load_fu_70_ap_start_reg <= 1'b0;
    end else begin
        if (((1'b1 == ap_CS_fsm_state1) & (ap_start == 1'b1))) begin
            grp_load_fu_70_ap_start_reg <= 1'b1;
        end else if ((grp_load_fu_70_ap_ready == 1'b1)) begin
            grp_load_fu_70_ap_start_reg <= 1'b0;
        end
    end
end

always @ (posedge ap_clk) begin
    if (ap_rst == 1'b1) begin
        grp_store_fu_77_ap_start_reg <= 1'b0;
    end else begin
        if ((1'b1 == ap_CS_fsm_state5)) begin
            grp_store_fu_77_ap_start_reg <= 1'b1;
        end else if ((grp_store_fu_77_ap_ready == 1'b1)) begin
            grp_store_fu_77_ap_start_reg <= 1'b0;
        end
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state4)) begin
        a_V_read = grp_add_fu_56_a_V_read;
    end else begin
        a_V_read = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state2)) begin
        a_V_write = grp_load_fu_63_a_V_write;
    end else begin
        a_V_write = 1'b0;
    end
end

always @ (*) begin
    if (((grp_store_fu_77_ap_done == 1'b1) & (1'b1 == ap_CS_fsm_state6))) begin
        ap_done = 1'b1;
    end else begin
        ap_done = 1'b0;
    end
end

always @ (*) begin
    if (((ap_start == 1'b0) & (1'b1 == ap_CS_fsm_state1))) begin
        ap_idle = 1'b1;
    end else begin
        ap_idle = 1'b0;
    end
end

always @ (*) begin
    if (((grp_store_fu_77_ap_done == 1'b1) & (1'b1 == ap_CS_fsm_state6))) begin
        ap_ready = 1'b1;
    end else begin
        ap_ready = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state4)) begin
        b_V_read = grp_add_fu_56_b_V_read;
    end else begin
        b_V_read = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state2)) begin
        b_V_write = grp_load_fu_70_a_V_write;
    end else begin
        b_V_write = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state6)) begin
        c_V_read = grp_store_fu_77_a_V_read;
    end else begin
        c_V_read = 1'b0;
    end
end

always @ (*) begin
    if ((1'b1 == ap_CS_fsm_state4)) begin
        c_V_write = grp_add_fu_56_c_V_write;
    end else begin
        c_V_write = 1'b0;
    end
end

always @ (*) begin
    case (ap_CS_fsm)
        ap_ST_fsm_state1 : begin
            if (((1'b1 == ap_CS_fsm_state1) & (ap_start == 1'b1))) begin
                ap_NS_fsm = ap_ST_fsm_state2;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state1;
            end
        end
        ap_ST_fsm_state2 : begin
            if (((1'b1 == ap_CS_fsm_state2) & (1'b0 == ap_block_state2_on_subcall_done))) begin
                ap_NS_fsm = ap_ST_fsm_state3;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state2;
            end
        end
        ap_ST_fsm_state3 : begin
            ap_NS_fsm = ap_ST_fsm_state4;
        end
        ap_ST_fsm_state4 : begin
            if (((grp_add_fu_56_ap_done == 1'b1) & (1'b1 == ap_CS_fsm_state4))) begin
                ap_NS_fsm = ap_ST_fsm_state5;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state4;
            end
        end
        ap_ST_fsm_state5 : begin
            ap_NS_fsm = ap_ST_fsm_state6;
        end
        ap_ST_fsm_state6 : begin
            if (((grp_store_fu_77_ap_done == 1'b1) & (1'b1 == ap_CS_fsm_state6))) begin
                ap_NS_fsm = ap_ST_fsm_state1;
            end else begin
                ap_NS_fsm = ap_ST_fsm_state6;
            end
        end
        default : begin
            ap_NS_fsm = 'bx;
        end
    endcase
end

assign ap_CS_fsm_state1 = ap_CS_fsm[32'd0];

assign ap_CS_fsm_state2 = ap_CS_fsm[32'd1];

assign ap_CS_fsm_state3 = ap_CS_fsm[32'd2];

assign ap_CS_fsm_state4 = ap_CS_fsm[32'd3];

assign ap_CS_fsm_state5 = ap_CS_fsm[32'd4];

assign ap_CS_fsm_state6 = ap_CS_fsm[32'd5];

always @ (*) begin
    ap_block_state2_on_subcall_done = ((grp_load_fu_70_ap_done == 1'b0) | (grp_load_fu_63_ap_done == 1'b0));
end

assign grp_add_fu_56_ap_start = grp_add_fu_56_ap_start_reg;

assign grp_load_fu_63_ap_start = grp_load_fu_63_ap_start_reg;

assign grp_load_fu_70_ap_start = grp_load_fu_70_ap_start_reg;

assign grp_store_fu_77_ap_start = grp_store_fu_77_ap_start_reg;

endmodule
