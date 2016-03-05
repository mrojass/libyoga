#include <cstdlib>
#include <iostream>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {
  ostringstream oss;
  oss << "convert img/" << argv[1] << " -colorspace gray -edge 2 "
      << "-background black -flatten -kuwahara 2 "
      << "img/gs-blur-" << argv[1];


  system(oss.str().c_str());
  return 0;
}
