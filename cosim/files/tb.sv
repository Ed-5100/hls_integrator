`timescale 1 ns/10 ps

module tb;

    logic clk, rst;


    // duration for each bit = 20 * timescale = 20 * 1 ns  = 20ns
    localparam period = 20;

    top top(
        .sys_clk(clk),
        .sys_rst(rst)
    );

    always begin
        clk = 1'b1;
        #5; // high for 20 * timescale = 20 ns

        clk = 1'b0;
        #5; // low for 20 * timescale = 20 ns
    end

    initial begin
        rst = 1'b1;
        #10;
        rst = 1'b0;
    end

    initial begin
        $display("Loading brams...");
        for(int i=0;i<8;i++) begin
            top.Block_Memory.bram[i] = i;
            top.Block_Memory_1.bram[i] = i;
            top.Block_Memory_2.bram[i] = 0;
        end
        $display("executing...");
    end

    int tested = 0;

    int counter;

    always_ff @( posedge top.ctrl_intf_1_done ) begin
        if (tested == 0) begin
            $display("testing result...");
            counter = 0;
            for(int i=0;i<8;i++) begin
                if (top.Block_Memory.bram[i] + top.Block_Memory_1.bram[i] == top.Block_Memory_2.bram[i])
                    counter++;
            end
            if (counter == 8)
                $display("pass...");
            else
                $display("fail...");
            tested <= 1'b1;
        end
    end

endmodule
