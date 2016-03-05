#include "magickal.h"

using namespace std;

int main(int argc, char** argv) {
  BPYoga::Magickal magickal;
  magickal.from(argv[1]);
  magickal.colorspace("gray");
  magickal.edge(2);
  magickal.background("black");
  magickal.flatten();
  magickal.negate();
  magickal.kuwahara(2);
  magickal.to(argv[2]);
  
  return 0;
}
