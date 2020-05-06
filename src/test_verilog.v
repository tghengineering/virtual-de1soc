module MyProject(input [9:0] SW, output [9:0] LEDR);

	assign LEDR = ~SW;

endmodule