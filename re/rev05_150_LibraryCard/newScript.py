#!/usr/bin/env python3

import angr
import claripy
import string

p = angr.Project("liblibrary_card.so")

flag_addr = p.loader.find_symbol("print_flag").rebased_addr

print_flag = p.factory.callable(flag_addr)

print(print_flag(0x824,0x82c,0x82b,0x82c))

# print(ret.result_state.postix.stdout.concentrize())


