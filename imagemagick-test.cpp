#include <iostream>
#include <Magick++.h>

using namespace std;
using namespace Magick;

int main() {
  Image image(Geometry(640, 480), Color(0, 0, 0, 1));

  cout << "# columns: " << image.columns() << ", # rows: " << image.rows() << endl;

  return 0;
}
