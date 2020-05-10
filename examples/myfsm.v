`define A_OFF 6'b00_0001
`define B_OFF 6'b00_0010
`define C_OFF 6'b00_0100
`define A_ON 6'b00_1000
`define B_ON 6'b01_0000
`define C_ON 6'b10_0000
`define B0 4'b0001
`define B0x 4'bxxx1
`define B1 4'b0010
`define B2 4'b0100
`define B3 4'b1000

module MyProject(
	input [9:0] SW, 
	input [3:0] KEY,
	input CLOCK_50, 
	output [9:0] LEDR);


endmodule


module MyFSM(
	input clk, 
	input [3:0] din, 
	output out, 
	output [5:0] state_w);

reg [5:0] state = `A_OFF;
reg [5:0] next_state = `A_OFF;

always @ (posedge clk) being
	state <= next_state;
end

always @ (*) being
	case(state):
		`A_OFF : 
			case(din)
				`B1 : next_state <= `B_OFF;
				default : next_state <= `A_OFF; 
			endcase
		`B_OFF : 
			case(din)
				`B1 : next_state <= `B_OFF;
				`B2 : next_state <= `C_OFF;
				default : next_state <= `A_OFF;
			endcase
		`C_OFF : 
			case(din)
				`B1 : next_state <= `B_OFF;
				`B2 : next_state <= `C_OFF;
				`B3 : next_state <= `A_ON;
				default : next_state <= `A_OFF;
			endcase
		`A_ON  : 
			casex(din)
				`B0x : next_state <= `A_OFF;
				`B1 : next_state <= `B_ON;
				default : next_state <= `A_ON;  
			endcase
		`B_ON  : 
			casex(din)
				`B0x : next_state <= `A_OFF;
				`B1 : next_state <= `B_ON;
				`B2 : next_state <= `C_ON;
				`B3 : next_state <= `A_ON;
				default : next_state <= `A_ON;
			endcase
		`C_ON  : 
			casex(din)
				`B0x : next_state <= `A_OFF;
				`B1 : next_state <= `B_ON;
				`B2 : next_state <= `C_ON;
				`B3 : next_state <= `A_OFF;
				default : next_state <= `A_ON;
			endcase
	endcase
end

assign 


endmodule