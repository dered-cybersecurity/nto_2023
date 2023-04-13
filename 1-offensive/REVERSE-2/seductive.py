from pwn import *

context.update(arch='mips', os='linux', bits=32, endian='little')
    #unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_2, &ans); // v0
    #unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_4, &neflag); //a0
    #unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_8, &invflag); //t0
    #unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_9, &flag); //t1
    #unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_3, res); // v1

shellcode = '''
    and  $t1, $t1, $a0
    lui $s0, 0x4a40
    ori $s0, $s0, 0x4d4b
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t2
    lui $s0, 0x3117
    ori $s0, $s0, 0x257b
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t3
    lui $s0, 0x6e22
    ori $s0, $s0, 0x1112
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t4
    lui $s0, 0x0a7d
    ori $s0, $s0, 0x457a
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t5
    lui $s0, 0x3b0e
    ori $s0, $s0, 0x1a4b
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t6
    lui $s0, 0x6851
    ori $s0, $s0, 0x297f
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    xor  $t1, $t1, $t7
    lui $s0, 0x1b08
    ori $s0, $s0, 0x1602
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    move $v0, $v1
    li $s0, 7
    subu $v0, $v0, $s0
    sltu $v0, $zero, $v0
    xori $v1, $v0, 1
'''
Sblock = '''
    {0}  $t1, $t1, ${1}
    lui $s0, {2}
    ori $s0, $s0, {3}
    subu $a0, $t1, $s0
    sltu $v0, $zero, $a0
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    '''

Send = '''
    xori $v0, $v0, 1
    add $v1, $v1, $v0
    move $v0, $v1
    li $s0, 7
    subu $v0, $v0, $s0
    sltu $v0, $zero, $v0
    xori $v1, $v0, 1
'''

shellcode = asm(shellcode)
s = ''.join([ chr(x) for x in shellcode ])

neflag = [ord(i) for i in "nto{Wh0_54id_Th1s_1S_M3d1um}"]
flag = []
for a in range(0, len(neflag), 4):
    flag.append((neflag[a] << 24) + (neflag[a + 1] << 16) + (neflag[a + 2] << 8) + neflag[a+3])
print(flag)
CODE = s.encode('UTF-8')
from unicorn import *
from unicorn.mips_const import *
from capstone import *
#Temmie Village
#
#
 

ADDRESS      = 0x10000


def hook_block(uc, address, size, user_data):
    md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
    print(">>> Tracing instruction at 0x%x, instruction size = 0x%x" %(address, size))
    print(">>> Instruction code at [0x%x] =" %(address))
    tmp = uc.mem_read(address, size)
    print(''.join('{:02x}'.format(x) for x in tmp))
    for i in md.disasm(tmp, address):
        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

def hook_code(uc, address, size, user_data):
    md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
    print(">>> Tracing instruction at 0x%x, instruction size = 0x%x" %(address, size))
    print(">>> Instruction code at [0x%x] =" %(address))
    tmp = uc.mem_read(address, size)
    print(''.join('{:02x}'.format(x) for x in tmp))
    for i in md.disasm(tmp, address):
        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

def test_mips_el(flag):
    #print("Emulate MIPS code (little-endian)")
    try:
        
        mu = Uc(UC_ARCH_MIPS, UC_MODE_MIPS32)

        mu.mem_map(ADDRESS, 2 * 1024 * 1024)

        mu.mem_write(ADDRESS, CODE)

        #mu.hook_add(UC_HOOK_BLOCK, hook_block)
        #mu.hook_add(UC_HOOK_CODE, hook_code)
        mu.reg_write(UC_MIPS_REG_V0, 0x0)
        mu.reg_write(UC_MIPS_REG_T1, flag[0])
        mu.reg_write(UC_MIPS_REG_T2, flag[1])
        mu.reg_write(UC_MIPS_REG_T3, flag[2])
        mu.reg_write(UC_MIPS_REG_T4, flag[3])
        mu.reg_write(UC_MIPS_REG_T5, flag[4])
        mu.reg_write(UC_MIPS_REG_T6, flag[5])
        mu.reg_write(UC_MIPS_REG_T7, flag[6])
        mu.reg_write(UC_MIPS_REG_A0, 0x2c2c2c2c)
        mu.emu_start(ADDRESS, ADDRESS + len(CODE))

        #print(">>> Emulation done. Below is the CPU context")

        REG = mu.reg_read(UC_MIPS_REG_T1)
        print("REG - %x" %REG)
        RES = mu.reg_read(UC_MIPS_REG_V1)
        print("RES - %x" %RES)
        return RES
    except UcError as e:
        print("ERROR: %s" % e)

def get_numbers(flag):
    #print("Emulate MIPS code (little-endian)")
    try:
        
        mu = Uc(UC_ARCH_MIPS, UC_MODE_MIPS32)

        mu.mem_map(ADDRESS, 2 * 1024 * 1024)

        mu.mem_write(ADDRESS, CODE)

        #mu.hook_add(UC_HOOK_BLOCK, hook_block)
        #mu.hook_add(UC_HOOK_CODE, hook_code)
        mu.reg_write(UC_MIPS_REG_V0, 0x0)
        mu.reg_write(UC_MIPS_REG_T1, flag[0])
        mu.reg_write(UC_MIPS_REG_T2, flag[1])
        mu.reg_write(UC_MIPS_REG_T3, flag[2])
        mu.reg_write(UC_MIPS_REG_T4, flag[3])
        mu.reg_write(UC_MIPS_REG_T5, flag[4])
        mu.reg_write(UC_MIPS_REG_T6, flag[5])
        mu.reg_write(UC_MIPS_REG_T7, flag[6])
        mu.reg_write(UC_MIPS_REG_A0, 0x2c2c2c2c)
        mu.emu_start(ADDRESS, ADDRESS + len(CODE))

        #print(">>> Emulation done. Below is the CPU context")

        REG = mu.reg_read(UC_MIPS_REG_T1)
        #print("REG - %x" %REG)
        RES = mu.reg_read(UC_MIPS_REG_V1)
        #print("RES - %x" %RES)
        return REG
    except UcError as e:
        print("ERROR: %s" % e)

#print(s)

RES = 0x2c2c2c2c
ret = 0
ans = ""
ops = ["and", "xor", "xor", "and", "xor", "xor", "and"]
regs =["a0",  "t2",  "t3",  "t4",  "t5",  "t6",  "t7" ]

print(len(flag))
for i in range(len(flag)):
    formatted = Sblock.format(ops[i], regs[i], '0', '0')
    shellcode = asm(formatted)
    CODE = ''.join([ chr(x) for x in shellcode ]).encode()
    flag[0] = get_numbers(flag)
    print(hex(flag[0]))
    low = flag[0] % 0x10000
    high = flag[0] // 0x10000
    ans += Sblock.format(ops[i], regs[i], hex(high), hex(low))
ans += Send
neflag = [ord(i) for i in "nto{Wh0_54id_Th1s_1S_M3d1um}"]
flag = []
for a in range(0, len(neflag), 4):
    flag.append((neflag[a] << 24) + (neflag[a + 1] << 16) + (neflag[a + 2] << 8) + neflag[a+3])

shellcode = asm(ans)
CODE = ''.join([ chr(x) for x in shellcode ]).encode()
test_mips_el(flag)

print('"',end='')
for x in shellcode:
    print('\\x%0.2x' %x, end='')
print('"')
print(len(shellcode))
