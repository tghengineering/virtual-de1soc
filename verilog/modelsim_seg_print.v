// # |--------||--------||--------||--------||--------||--------|
// # |  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  |
// # | X    X || X    X || X    X || X    X || X    X || X    X |
// # | X    X || X    X || X    X || X    X || X    X || X    X |
// # |  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  |
// # | X    X || X    X || X    X || X    X || X    X || X    X |
// # | X    X || X    X || X    X || X    X || X    X || X    X |
// # |  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  ||  XXXX  |
// # |--------||--------||--------||--------||--------||--------|

module test_aux();
	
	reg [6:0] h0 = 7'b111_1111;
	reg [6:0] h1 = 7'b000_0000;
	reg [6:0] h2 = 7'b111_1111;
	reg [6:0] h3 = 7'b000_0000;
	reg [6:0] h4 = 7'b111_1111;
	reg [6:0] h5 = 7'b000_0000;

	initial begin
		repeat(10) begin
		h0 = h0 + 7'b1;
		hex_de1(h0, h1, h2, h3, h4, h5);
		end
	end


	task hex_cell_horiz;
	input [0:0] h0;
		if(!h0)
			$write("|..XXXX..|");
		else 
			$write("|..    ..|");
	endtask

	task hex_cell_verti;
	input [1:0] h;
		case(~h)
			2'b00: $write("|. .... .|");
			2'b01: $write("|. ....X.|");
			2'b10: $write("|.X.... .|");
			2'b11: $write("|.X....X.|");
			default: $write("?");
		endcase
	endtask

	task hex_cell_blank;
		$write("|........|");
	endtask

	task print_blank;
	begin
		hex_cell_blank;
		hex_cell_blank;
		hex_cell_blank;
		hex_cell_blank;
		hex_cell_blank;
		hex_cell_blank;
		$write("\n");
	end
	endtask

	task print_horiz;
		input h0, h1, h2, h3, h4, h5;
	begin
		hex_cell_horiz(h5);
		hex_cell_horiz(h4);
		hex_cell_horiz(h3);
		hex_cell_horiz(h2);
		hex_cell_horiz(h1);
		hex_cell_horiz(h0);
		$write("\n");
	end
	endtask

	task print_verti;
		input [1:0] h0, h1, h2, h3, h4, h5;
	begin
		hex_cell_verti(h5);
		hex_cell_verti(h4);
		hex_cell_verti(h3);
		hex_cell_verti(h2);
		hex_cell_verti(h1);
		hex_cell_verti(h0);
		$write("\n");
	end
	endtask

	task hex_de1;
		input [6:0] h0, h1, h2, h3, h4, h5;

		begin
			print_blank;
			print_horiz(h0[0], h1[0], h2[0], h3[0], h4[0], h5[0]); 
			print_verti({h0[5], h0[1]}, {h1[5], h1[1]}, {h2[5], h2[1]}, {h3[5], h3[1]}, {h4[5], h4[1]}, {h5[5], h5[1]});
			print_verti({h0[5], h0[1]}, {h1[5], h1[1]}, {h2[5], h2[1]}, {h3[5], h3[1]}, {h4[5], h4[1]}, {h5[5], h5[1]});
			print_horiz(h0[6], h1[6], h2[6], h3[6], h4[6], h5[6]); 
			print_verti({h0[4], h0[2]}, {h1[4], h1[2]}, {h2[4], h2[2]},{h3[4], h3[2]}, {h4[4], h4[2]}, {h5[4], h5[2]});
			print_verti({h0[4], h0[2]}, {h1[4], h1[2]}, {h2[4], h2[2]},{h3[4], h3[2]}, {h4[4], h4[2]}, {h5[4], h5[2]});
			print_horiz(h0[3], h1[3], h2[3], h3[3], h4[3], h5[3]); 
			print_blank;
			$write("\n");
		end
	endtask

endmodule