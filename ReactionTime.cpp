#include <iostream>
#include <ctime>
#include <cstdlib>
#include <chrono>
#include <thread>

using namespace std;

int main() {
    srand(static_cast<unsigned>(time(0))); // Seed for random number generation

    cout << "Welcome to the Reaction Time Game!" << endl;
    cout << "Press Enter when you see the prompt." << endl;

    // Wait for a random amount of time before prompting the user
    int delay = rand() % 5000 + 1000; // Delay between 1 and 6 seconds
    this_thread::sleep_for(chrono::milliseconds(delay));

    auto start_time = chrono::high_resolution_clock::now(); // Record start time

    cout << "NOW! Press Enter!" << endl;
    cin.get(); // Wait for user input

    auto end_time = chrono::high_resolution_clock::now(); // Record end time

    // Calculate and display reaction time
    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << "Your reaction time: " << duration.count() << " milliseconds" << endl;

    return 0;
}
