import sys
import os
import pickle
import idaapi
import ida_auto
import idautils
import ida_pro
import ida_funcs
import idc
import ida_hexrays
import ida_idp
import ida_ida
import ida_loader
import ida_entry
import ida_idaapi

# becsause the -S script runs very early, we need to load the decompiler
# manually if we want to use it
def init_hexrays():
    ALL_DECOMPILERS = {
        ida_idp.PLFM_386: "hexrays",
        ida_idp.PLFM_ARM: "hexarm",
        ida_idp.PLFM_PPC: "hexppc",
        ida_idp.PLFM_MIPS: "hexmips",
    }
    cpu = ida_idp.ph.id
    decompiler = ALL_DECOMPILERS.get(cpu, None)
    if not decompiler:
        print("No known decompilers for architecture with ID: %d" % ida_idp.ph.id)
        return False
    inf = ida_idaapi.get_inf_structure()
    if inf.inf_is_64bit():
        if cpu == ida_idp.PLFM_386:
            decompiler = "hexx64"
        else:
            decompiler += "64"
    if ida_loader.load_plugin(decompiler) and ida_hexrays.init_hexrays_plugin():
        return True
    else:
        print('Couldn\'t load or initialize decompiler: "%s"' % decompiler)
        return False


def get_code():
    path = idc.get_input_file_path()
    print(path)
    print(idaapi.get_hexrays_version())
    # if os.path.isfile(path+".pkl"):
    #     return True
    
    file = open(path+"_decompile.log","w")
    sys.stdout = file
    # print(f"here:{path}")
    all_data = []
    for func_addr in idautils.Functions():
        print(func_addr)
        dfunc = None
        try:
            dfunc = ida_hexrays.decompile(func_addr)
            if(not dfunc):
                # print(f"Cannot be decompiled: {func_addr}")
                pass
            else:
                sc = dfunc.get_pseudocode()
                lines = []
                func_name = ida_funcs.get_func_name(func_addr)
                func_name = func_name[1:] if func_name.startswith('.') else func_name
                count = 0
                for sline in sc:
                    lines.append(idaapi.tag_remove(sline.line).replace(func_name, '<func>')+'\n') if count==0 else lines.append(idaapi.tag_remove(sline.line)+'\n')
                    count += 1
                print(func_addr, func_name, ''.join(lines))
                all_data.append((func_addr, func_name,  ''.join(lines)))
        except Exception as e:
            print(e)
            print(func_addr)
    file.close()

    return True

if __name__=="__main__":
    idc.Wait()
    if init_hexrays():
        result = get_code()

    idc.Exit(0)
