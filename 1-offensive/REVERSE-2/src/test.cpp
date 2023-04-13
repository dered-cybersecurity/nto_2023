
#define ERROR 1
#include <iostream>
namespace unicorn{ 
    #include <unicorn/unicorn.h>
}
#include <string>
#include <vector>
#define MIPS_CODE "\x26\x48\x24\x01\x40\x4a\x10\x3c\x4b\x4d\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2a\x01\x17\x31\x10\x3c\x7b\x25\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2b\x01\x22\x6e\x10\x3c\x12\x11\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2c\x01\x7d\x0a\x10\x3c\x7a\x45\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2d\x01\x0e\x3b\x10\x3c\x4b\x1a\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2e\x01\x51\x68\x10\x3c\x7f\x29\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2f\x01\x08\x1b\x10\x3c\x02\x16\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x25\x10\x60\x00\x07\x00\x10\x24\x23\x10\x50\x00\x2b\x10\x02\x00\x01\x00\x43\x38"
#define LEN 217
#define ADDRESS 0x1000
int main()
{
    int flag[7] = {1718378855, 2069325872, 1597322345, 1683969128, 829644593, 1398747956, 1935228797};
    unicorn::uc_err err;
    int ans = 0;
    unicorn::uc_engine* engine;
    int val;
    err = unicorn::uc_open(unicorn::UC_ARCH_MIPS, unicorn::UC_MODE_MIPS32, &engine);
    if(err)
    {
        throw ERROR;
    }
    err = unicorn::uc_mem_map(engine, ADDRESS, 2 * 1024 * 1024, unicorn::UC_PROT_ALL);
    err = unicorn::uc_mem_write(engine, ADDRESS, MIPS_CODE , LEN - 1);
    val = 0;
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_V0, &val); 
    val = 0x2c2c2c2c;
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_A0, &val); 
    val = flag[0];
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_T1, &val); 
    val = flag[1];
    err = unicorn::uc_reg_write(engine, unicorn:: UC_MIPS_REG_T2, &val); 
    val = flag[2];
    err = unicorn::uc_reg_write(engine, unicorn:: UC_MIPS_REG_T3, &val); 
    val = flag[3];
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_T4, &val); 
    val = flag[4];
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_T5, &val); 
    val = flag[5];
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_T6, &val); 
    val = flag[6];
    err = unicorn::uc_reg_write(engine, unicorn::UC_MIPS_REG_T7, &val); 
    err = unicorn::uc_emu_start(engine, ADDRESS, ADDRESS + LEN - 1, 0, 0);
    if(err)
    {
        std::cout << unicorn::uc_strerror(err) <<  std::endl;
        throw ERROR;
    }
    int res;
    unicorn::uc_reg_read(engine, unicorn::UC_MIPS_REG_V1, &res);
    unicorn::uc_close(engine);
    std::cout << res << std::endl;
    return 0;
}