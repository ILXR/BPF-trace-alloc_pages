#include <unistd.h>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    cout << sizeof(void *) << endl;
    for (int i = 0; i < 1000; i++)
    {
        printf("malloc 1M vm\n");
        malloc(1000 * 1000);
        sleep(1);
    }
    return 0;
}