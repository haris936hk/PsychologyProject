#include <SFML/Graphics.hpp>
#include <cstdlib>
#include <ctime>
#include <iostream>

class ReactionTimeGame {
public:
    ReactionTimeGame() {
        srand(static_cast<unsigned>(time(0))); // Seed for random number generation

        window.create(sf::VideoMode(400, 200), "Reaction Time Game");
        window.setFramerateLimit(60);

        font.loadFromFile("arial.ttf"); // Replace with the path to your font file

        welcomeText.setFont(font);
        welcomeText.setString("Welcome to the Reaction Time Game!\nPress Enter when you see the prompt.");
        welcomeText.setCharacterSize(20);
        welcomeText.setPosition(20, 20);

        reactionText.setFont(font);
        reactionText.setCharacterSize(20);
        reactionText.setPosition(20, 70);

        startGame();
    }

    void startGame() {
        int delay = rand() % 5000 + 1000; // Delay between 1 and 6 seconds
        sf::sleep(sf::milliseconds(delay));

        welcomeText.setString("Get ready!");

        window.clear();
        window.draw(welcomeText);
        window.display();

        sf::sleep(sf::seconds(1)); // Wait for 1 second

        welcomeText.setString("NOW! Press Enter!");
        window.clear();
        window.draw(welcomeText);
        window.display();

        waitForEnter();

        auto startTime = sf::Clock::getLocalTime();

        welcomeText.setString("Your reaction time: ");
        window.clear();
        window.draw(welcomeText);
        window.display();

        waitForEnter();

        auto endTime = sf::Clock::getLocalTime();
        sf::Time reactionTime = endTime - startTime;

        reactionText.setString("Your reaction time: " + std::to_string(reactionTime.asMilliseconds()) + " milliseconds");
        window.clear();
        window.draw(reactionText);
        window.display();

        sf::sleep(sf::seconds(3)); // Display the result for 3 seconds
        window.close();
    }

    void waitForEnter() {
        sf::Event event;
        while (window.waitEvent(event)) {
            if (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Enter) {
                break;
            }
        }
    }

private:
    sf::RenderWindow window;
    sf::Font font;
    sf::Text welcomeText;
    sf::Text reactionText;
};

int main() {
    ReactionTimeGame game;
    return 0;
}
