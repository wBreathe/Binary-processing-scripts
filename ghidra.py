#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################
# File Name: ghidra.py
# Author: Yunru Wang
# E-mail: yunruw@outlook.com
# Created Time: 2024-01-30 14:23
# Last Modified: 2024-02-08 23:41
###########################
import os
import argparse


def main(args):
    file_lst = []
    window_size = 1
    for parent, subdirs, files in os.walk(args.bin_folder):
        file_lst.extend([os.path.join(parent,f) for f in files if files])
    i = 0

    for f in file_lst:
        if(i>=1):
            break
        print(f)
        os.system(f'{args.ghidra_path}support/analyzeHeadless {args.project_dir}\
                {args.project_name}\
                -import {f} \
                -overwrite \
                -scriptPath {args.script_path} \
                -postscript {args.script_name}')
        i+=1


if __name__=="__main__":
    parser = argparse.ArgumentParser(
            prog='ghidrascript',
            description='ghidra python scripts for data              generation in palmtree'
            )
    parser.add_argument('--bin-f', dest='bin_folder',default='/<path to binaries>/', help='binary folder')
    parser.add_argument('--ghidra', dest='ghidra_path',default='/<path to ghidra>/', help='ghidra installation path')
    parser.add_argument('--script-path',dest='script_path', default='/<path to ghidra scripts>/', help='ghidra script path')
    parser.add_argument('--script-name', dest='script_name', default='/<path toghidra scripts>/script_name.py', help='ghidra script name')
    parser.add_argument('--project-dir', dest='project_dir', default='/<path to ghidra project>/', help='ghidra project path')
    parser.add_argument('--project-name', dest='project_name', default='ghidra_project_name', help='ghidra project name')
    args = parser.parse_args()
    main(args)
