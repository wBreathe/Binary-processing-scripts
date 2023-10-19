# -*- coding: utf-8 -*-
import os
from os.path import exists
import subprocess
import time
def batch_ida(PLUGIN_PATH,elf_list,ELF_PATH):
    IDA_PATH="/home/emma/IDA_Pro_v6.4/idaq64"

    for elf in elf_list:
        start = time.clock()
        cmd = IDA_PATH + " -c -A -S" + PLUGIN_PATH + " " + ELF_PATH + elf
        os.system(cmd)
        end = time.clock()
        print("processing time:{time}".format(time=end-start))

if __name__ == "__main__":
    PLUGIN_PATH = "/home/emma/newprogram/code/ida_bytes.py"
    ELF_PATH = "/home/emma/binary/"
    list_dir = "/home/emma/new_temp_data/"
    #op_list = ["clang_O2_m32","clang_O0","clang_O1","clang_O3","clang_O2"]
    op_list = os.listdir(list_dir)
    op_list = ['clang_O1']
    for op in op_list:
        #elf_list = os.listdir(list_dir+op+"/")
        #elf_list = ['gcc','gobmk','dealII','nginx','lighttpd','diff']
        elf_list = os.listdir(list_dir+op+"/")
        elf_list=['exim']
        batch_ida(PLUGIN_PATH,elf_list,ELF_PATH+op+"/")
    
