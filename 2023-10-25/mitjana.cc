/* Programa que calcula la mitjana dels reals presents a l'entrada. */

#include <iostream>
using namespace std;

int main()
{
    double s = 0.0;
    int n = 0;
    double x;
    while (cin >> x) {
        s += x;
        ++n;
    }
    cout << s / n << endl;
}
