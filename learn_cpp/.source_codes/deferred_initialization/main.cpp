#include "a.h"
#include "b.h"

extern A a;
extern B b;
 
int main() {
    a.Use();
    b.Use();
}