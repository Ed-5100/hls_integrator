create_project project_1 /home/yx388/vivado_project/project_1 -part xc7z020clg484-1 -force
set_property board_part em.avnet.com:zed:part0:1.4 [current_project]
add_files -norecurse {/home/yx388/Litex/hls_integrator/cosim/files/block_memory.v /home/yx388/Litex/hls_integrator/cosim/files/ctrl.sv /home/yx388/Litex/hls_integrator/cosim/files/hlsi_DUT.v /home/yx388/Litex/hls_integrator/cosim/files/tb.sv /home/yx388/Litex/hls_integrator/cosim/files/vadd.v}
update_compile_order -fileset sources_1
set_property top tb [current_fileset -simset sim_1]
launch_simulation
close_sim
close_project
