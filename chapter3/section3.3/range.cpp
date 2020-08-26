/*
ID: riff.sc1
LANG: C++
TASK: range
*/
#include <fstream>
#include <string>

std::ifstream fin("range.in");
std::ofstream fout("range.out");
const int kMaxSize = 250;

// farm[n][i][j] indicates whether the n x n square with (i, j) as its top-left
// corner is a good square for grazing.
// Due to space constraints, we only save two maps at a time, rotating the first 
// index. 1x1 squares go into farm[0], 2x2 goes into farm[1], 3x3 goes into
// farm[0], 4x4 goes into farm[1], etc.
bool farm[2][kMaxSize][kMaxSize];

int main() {
  int farm_size;
  fin >> farm_size;

  // Process input.
  std::string farm_data[farm_size];
  for (int i = 0; i < farm_size; ++i) {
    fin >> farm_data[i];
  }

  for (int i = 0; i < farm_size; ++i) {
    for (int j = 0; j < farm_size; ++j) {
      if (farm_data[i][j] == '1') {
        farm[0][i][j] = true;
      } else {
        farm[0][i][j] = false;
      }
    }
  }

  int small = 0;
  int large = 1;
  for (int size = 2; size <= farm_size; ++size) {
    // Build 2x2 squares from 1x1 squares, etc.
    int num_good_squares = 0;
    for (int i = 0; i < farm_size - size + 1; ++i) {
      for (int j = 0; j < farm_size - size + 1; ++j) {
        if (farm[small][i][j] && farm[small][i+1][j] && 
            farm[small][i][j+1] && farm[small][i+1][j+1]) {
          farm[large][i][j] = true;
          ++num_good_squares;
        } else {
          farm[large][i][j] = false;
        }
      }
    }
    if (num_good_squares > 0) {
      fout << size << ' ' << num_good_squares << std::endl;
    }

    // Swap the two arrays.
    small = 1 - small;
    large = 1 - large;
  }

  return 0;
}