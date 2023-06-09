#include "imports.hpp"
#define MIPS_CODE "\x24\x48\x24\x01\x24\x2c\x10\x3c\x28\x2c\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2a\x01\x4c\x7b\x10\x3c\x77\x1c\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2b\x01\x78\x4e\x10\x3c\x13\x75\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x24\x48\x2c\x01\x50\x4e\x10\x3c\x11\x60\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2d\x01\x0f\x3d\x10\x3c\x42\x51\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x26\x48\x2e\x01\x42\x62\x10\x3c\x26\x62\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x24\x48\x2f\x01\x40\x20\x10\x3c\x24\x60\x10\x36\x23\x20\x30\x01\x2b\x10\x04\x00\x01\x00\x42\x38\x20\x18\x62\x00\x01\x00\x42\x38\x20\x18\x62\x00\x25\x10\x60\x00\x07\x00\x10\x24\x23\x10\x50\x00\x2b\x10\x02\x00\x01\x00\x43\x38"
#define LEN 224
#define ADDRESS 0x1000
unsigned char* transform(const char* c, int len)
{
    unsigned char* ret = new unsigned char[len];
    for(int i = 0; i < len; i++)
        ret[i] = c[i];
    return ret;
}

void call()
{
    unsigned char* code = transform(MIPS_CODE, LEN);
    Interpreter p(ADDRESS,MIPS_CODE, LEN);
    std::string passphrase;
    std::cout << "Welcome back user!!\nPlease Enter passphrase: ";
    std::cin >> passphrase;
    if(passphrase.find("nto{") != 0)
    {
        throw ERROR;
    }
    if(p.check(passphrase))
    {
        std::cout << "Good job!\n";
    }else{
        std::cout << "?\n";
    }
}