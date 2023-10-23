#include <cmath>
#include <iostream>
#include <string>
using namespace std;

int maxim(int a, int b)
{
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int factorial(int n)
{
    int f = 1;
    int i = 1;
    while (i <= n) {
        f = f * i;
        i = i + 1;
    }
    return f;
}

int factorial_rec(int n)
{
    if (n == 0) {
        return 1;
    } else {
        return n * factorial_rec(n - 1);
    }
}

int factorial_for(int n)
{
    int f = 1;
    for (int i = 1; i <= n; ++i) {
        f = f * i;
    }
    return f;
}

bool es_primer(int n)
{
    // sup n >= 0
    if (n <= 1) {
        return false;
    }
    int d = 2;
    while (d * d <= n) {
        if (n % d == 0) {
            return false;
        }
        ++d;
    }
    return true;
}

double mitjana(double x, double y)
{
    return (x + y) / 2;
}

void saluda(string nom)
{
    cout << "Hola " << nom << endl;
}

void trigo(double angle)
{
    cout << "sin:" << sin(angle) << endl;
    cout << "cos:" << cos(angle) << endl;
    cout << "tan:" << tan(angle) << endl;
}

int main()
{
    int x, y;
    cin >> x >> y;
    cout << maxim(x, y) << endl;

    int n;
    cin >> n;
    cout << factorial(n) << endl;

    saluda("Pere");
    saluda("a");
}
