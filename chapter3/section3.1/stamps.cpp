/*
ID: riff.sc1
LANG: C++
TASK: stamps
*/
#include <fstream>

std::ifstream fin("stamps.in");
std::ofstream fout("stamps.out");

int num_stamps_allowed, num_stamp_values;
// I tried to use std::vector but the grader failed me with bad_alloc.
// There's a time and a place for software engineering best practices, but USACO
// ain't it. Might as well use globals too.
int stamp_values[50];
int num_stamps_needed_for[10000 * 200 + 1];

int get_num_stamps_needed(int target) {
  int minimum = 1000;
  for (int i = 0; i < num_stamp_values; ++i) {
    int value = stamp_values[i];
    if (target - value >= 0 && num_stamps_needed_for[target - value] < minimum) {
      minimum = num_stamps_needed_for[target - value];
    }
  }
  return minimum + 1;
}

int main() {
  fin >> num_stamps_allowed >> num_stamp_values;
  for (int i = 0; i < num_stamp_values; ++i) {
    fin >> stamp_values[i];
  }

  num_stamps_needed_for[0] = 0;

  int current_target;
  for (current_target = 1; ; ++current_target) {
    int num_stamps_needed_for_target = get_num_stamps_needed(current_target);
    if (num_stamps_needed_for_target <= num_stamps_allowed) {
      num_stamps_needed_for[current_target] = num_stamps_needed_for_target;
    } else {
      // Not possible to reach target.
      break;
    }
  }

  fout << current_target - 1 << std::endl;
  return 0;
}