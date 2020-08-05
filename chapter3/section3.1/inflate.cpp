/*
ID: riff.sc1
LANG: C++
TASK: inflate
*/
#include <fstream>

std::ifstream fin("inflate.in");
std::ofstream fout("inflate.out");

int main() {
  int total_time, num_problems;
  fin >> total_time >> num_problems;

  int memo[total_time+1];
  for (int i = 0; i <= total_time; ++i) {
    memo[i] = 0;
  }

  for (int i = 0; i < num_problems; ++i) {
    int points, minutes;
    fin >> points >> minutes;
    for (int t = minutes; t <= total_time; ++t) {
      if (memo[t] < memo[t - minutes] + points) {
        memo[t] = memo[t - minutes] + points;
      }
    }
  }

  fout << memo[total_time] << std::endl;
  return 0;
}