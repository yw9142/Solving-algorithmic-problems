#include <iostream>

using namespace std;

int main(void) {
    ios_base::sync_with_stdio(false);
    int Hambuger_price;
    int Drink_price;
    int lowDrink = 2000, lowHam = 2000;

    for (int i = 0; i < 3; i++) {
        cin >> Hambuger_price;
        if (Hambuger_price < lowHam)
            lowHam = Hambuger_price;
    }
    for (int i = 0; i < 2; i++) {
        cin >> Drink_price;
        if (Drink_price < lowDrink)
            lowDrink = Drink_price;
    }

    cout << lowHam + lowDrink - 50 << '\n';
    return (0);
}
