
#include "lib2.h"

#include "lib1.h"

int32_t mul(int32_t a, int32_t b) {
  int32_t result = 0;
  for (size_t i = 0; i < b; i++)
  {
    result = add(result, a);
  }
  return result;
}