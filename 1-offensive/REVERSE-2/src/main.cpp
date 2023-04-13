#include "imports.hpp"
#include <iostream>
#include <typeinfo>

int main() {
    try {
    call();
    }catch(int e)
    {
     if( e == 2)
        std::cout << "Not a passphrase" << std::endl;
     else
        std::cout << "Wow you caused error somehow... " << e << std::endl;
    }
    return 0;
}