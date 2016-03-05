#ifndef MAGICKAL_H
#define MAGICKAL_H

#include <sstream>

using namespace std;

namespace BPYoga {

  /**
  * Wrapper class for ImageMagick command line utilities.
  */
  class Magickal {
    public:
      void convert();
      void colorspace(const string& space);
      void edge(double radius);
      void background(const string& color);
      void flatten();
      void negate();
      void kuwahara(double radius);

      void from(const string& src);
      void to(const string& dst);

    private:
      ostringstream oss;
  };

  #include "magickal.hpp"

}

#endif
