#include <cstdlib>

using namespace BPYoga;

void Magickal::convert() {
  string opts = oss.str();
  oss << "convert " << opts;
  system(oss.str().c_str());
}

void Magickal::colorspace(const string& space) {
  oss << " -colorspace " << space;
}

void Magickal::edge(double radius) {
  oss << " -edge " << radius;
}

void Magickal::background(const string& color) {
  oss << " -background " << color;
}

void Magickal::flatten() {
  oss << " -flatten";
}

void Magickal::negate() {
  oss << " -negate";
}

void Magickal::kuwahara(double radius) {
  oss << " -kuwahara " << radius;
}

void Magickal::from(const string& src) {
  string opts = oss.str();
  oss << src << opts;
}

void Magickal::to(const string& dst) {
  oss << " " << dst;
}
