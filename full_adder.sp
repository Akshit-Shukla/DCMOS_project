* D:\Desktop\DCMOS_PROJECT\Spice_Circuits\3-NAND\3-NAND.asc
M1 Vdd A N003 Vdd PMOS l={L1} w={W1}
M2 N003 B N006 N003 PMOS l={L2} w={W2}
M3 Vdd B N001 Vdd PMOS l={L3} w={W3}
M4 Vdd A N001 Vdd PMOS l={L4} w={W4}
M5 N001 Cin N006 N001 PMOS l={L5} w={W5}
M6 Vdd Cin N002 Vdd PMOS l={L6} w={W6}
M7 Vdd B N002 Vdd PMOS l={L7} w={W7}
M8 Vdd A N002 Vdd PMOS l={L8} w={W8}
M9 N002 N006 N005 N002 PMOS l={L9} w={W9}
M10 N005 N006 N018 N013 NMOS l={L10} w={W10}
M11 N018 B 0 N024 NMOS l={L11} w={W11}
M12 N018 Cin 0 N023 NMOS l={L12} w={W12}
M13 N017 A 0 N022 NMOS l={L13} w={W13}
M14 N017 B 0 N021 NMOS l={L14} w={W14}
M15 N016 B 0 N020 NMOS l={L15} w={W15}
M16 N006 Cin N017 N012 NMOS l={L16} w={W16}
M17 N018 A 0 N025 NMOS l={L17} w={W17}
M18 N019 A 0 N026 NMOS l={L18} w={W18}
M19 N010 B N019 N014 NMOS l={L19} w={W19}
M20 N006 Cin N010 N009 NMOS l={L20} w={W20}
M21 N007 Cin N006 N007 PMOS l={L21} w={W21}
M22 Vdd A N004 Vdd PMOS l={L22} w={W22}
M23 N004 B N007 N004 PMOS l={L23} w={W23}
M24 Vdd N005 Sum Vdd PMOS l={L24} w={W24}
M25 Vdd N006 Carry Vdd PMOS l={L25} w={W25}
M26 Sum N005 0 N008 NMOS l={L26} w={W26}
M27 Carry N006 0 N015 NMOS l={L27} w={W27}
M28 N006 A N016 N011 NMOS l={L28} w={W28}
V1 A 0 1
V2 B 0 1
V3 Cin 0 1
V4 Vdd 0 1
.model NMOS NMOS
.model PMOS PMOS
.lib C:\Users\akshi\AppData\Local\LTspice\lib\cmp\standard.mos
.inc C:\Users\akshi\Downloads\ptm_45nm_hp.l

.meas static_current_000 param='I(V4)'
.tran 10m
.backanno
.end
