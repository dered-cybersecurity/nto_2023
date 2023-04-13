#pragma once
#include "imports.hpp"
using namespace std;
#include <vector>

class Interpreter {
private:
    const char* _code;
    unsigned int _code_len;
    unsigned int _addr;
    int _run(vector<int>);
    static void hook_block(unicorn::uc_engine *uc, uint64_t address, uint32_t size, void *user_data)
    {
    std::cout <<">>> Tracing basic block at 0x" << address << ", block size = 0x" << size << std::endl;
    }
    static void hook_code(unicorn::uc_engine *uc, uint64_t address, uint32_t size, void *user_data)
    {
    std::cout <<">>> Tracing basic block at 0x" << address << ", block size = 0x" << size << std::endl;
    }
public:
    Interpreter(unsigned long,const char*,unsigned long);
    int check(string a);
};
void call();