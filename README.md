# IDAscripts
update a series of IDApython scripts

batch_ida.py: how to execute IDA script in batch

ida_bytes.py: the script used in paper BKWTG
- a script to simply handle stripped binaries, including
  - finding address-taken functions,
  - recording function boundaries,
  - recording byte series in a basic block,
  - recording the address of indirect call site,
  - recording the address and targets of direct call site
