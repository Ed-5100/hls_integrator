
module mem_init(
    input  logic        wen_m0,
    input  logic        ren_m0,
    input  logic [2:0]  addr_m0,
    input  logic [31:0] datw_m0,
    output logic [31:0] datr_m0,

    input  logic        wen_m1,
    input  logic        ren_m1,
    input  logic [2:0]  addr_m1,
    input  logic [31:0] datw_m1,
    output logic [31:0] datr_m1,

    output logic        wen_s,
    output logic        ren_s,
    output logic [2:0]  addr_s,
    output logic [31:0] datw_s,
    input  logic [31:0] datr_s,

    input         sel
);


    always_comb begin
        if (sel == 1'b0) begin
            wen_s   = wen_m0;
            ren_s   = ren_m0;
            addr_s  = addr_m0;
            datw_s  = datw_m0;
            datr_m0 = datr_s;
        end else begin
            wen_s   = wen_m1;
            ren_s   = ren_m1;
            addr_s  = addr_m1;
            datw_s  = datw_m1;
            datr_m1 = datr_s;
        end
    end

endmodule

module ctrl(
    input  logic        clk,
    input  logic        rst,
    output logic        adder_start,
    input  logic        adder_done,
    input  logic        adder_idle,
    input  logic        adder_ready
);

    localparam STRT = 1'd0;
    localparam ADD  = 1'd1;

    logic state;
    logic state_next;

    /*
    initial begin
        forever begin
            clk = 1'b0;
            #10 clk = ~clk;
        end
        rst = 1'b1;
        #20 rst = 1'b0;
    end
    */

    always_ff @( posedge clk ) begin
        if (rst)
            state <= STRT;
        else
            state <= state_next;
    end

    always_comb begin
        state_next = state;
        case (state)
            STRT:
            begin
                state_next = ADD;
            end

            ADD:
            if (adder_done) begin
                state_next = STRT;
            end
            default: state_next = 'x;
        endcase
    end

    logic adder_rst;

    always_comb begin
        adder_rst = 1'b0;
        case (state)
            STRT:
            begin
                adder_start = 1'b0;
                adder_rst = 1'b1;
            end

            ADD:
            begin
                adder_start = 1'b1;
            end

            default:
            begin
                adder_start = 'x;
            end
        endcase
    end

endmodule
