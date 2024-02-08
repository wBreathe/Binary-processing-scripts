

# Binary processing scripts
update a series of IDApython/ghidra/angr/radare2 scripts

## IDA
batch_ida.py: how to execute IDA script in batch

ida_bytes.py: the script used in paper BKWTG
- a script to simply handle stripped binaries, including
  - finding address-taken functions,
  - recording function boundaries,
  - recording byte series in a basic block,
  - recording the address of indirect call site,
  - recording the address and targets of direct call site


## Ghidra
ghidra.py
- automatically execute the ghidra script
control_flow_gen_ghi.py
- a script to generate cfg using networkx
utils_ghi.py
- combined with control_flow_gen_ghi.py
