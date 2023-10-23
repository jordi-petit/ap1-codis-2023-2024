// referències

#include <iostream>
using namespace std;

void intercanviar(int& x, int& y)
{
    int z = y;
    y = x;
    x = z;
}

void incrementar_un_segon(int& h, int& m, int& s)
{
    ++s;
    if (s == 60) {
        ++m;
        s = 0;
        if (m == 60) {
            m = 0;
            ++h;
            if (h == 24) {
                h = 0;
            }
        }
    }
}

int main()
{
    int a = 4;
    int b = 6;
    cout << a << " " << b << endl;
    intercanviar(a, b);
    cout << a << " " << b << endl;
}

int main()
{
    int h = 23;
    int m = 59;
    int s = 59;
    cout << h << ":" << m << ":" << s << endl;
    incrementar_un_segon(h, m, s);
    cout << h << ":" << m << ":" << s << endl;
}

void descomposicio_horaria(int n, int& h, int& m, int& s)
{
    h = n / 3600;
    m = (n % 3600) / 60;
    s = n % 3600;
}

int main()
{
    int n = 7272;
    int h = 0, m = 0, s = 0;
    descomposicio_horaria(n, h, m, s);
    cout << h << m << s << endl;
}