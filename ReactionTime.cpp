#include <SFML/Graphics.hpp>
#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Set up the window
    sf::RenderWindow window(sf::VideoMode(800, 600), "Reaction Time Test");
    window.setFramerateLimit(60);

    // Set up the target box
    sf::RectangleShape target(sf::Vector2f(100, 100));
    target.setFillColor(sf::Color::Red);
    target.setPosition(350, 250);
    target.setOutlineThickness(2);
    target.setOutlineColor(sf::Color::Black);
    bool targetVisible = false;

    // Set up the font and result text
    sf::Font font;
    if (!font.loadFromFile("arial.ttf")) {
        std::cerr << "Error loading font\n";
        return EXIT_FAILURE;
    }

    sf::Text resultText("", font, 30);
    resultText.setPosition(250, 400);
    resultText.setFillColor(sf::Color::Black);

    // Set up timing variables
    std::clock_t startTime, endTime;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
            
            if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left) {
                if (targetVisible) {
                    endTime = std::clock();
                    double reactionTime = static_cast<double>(endTime - startTime) / CLOCKS_PER_SEC * 1000;
                    resultText.setString("Your reaction time: " + std::to_string(reactionTime) + " milliseconds");
                    targetVisible = false;
                }
            }
        }

        window.clear(sf::Color::White);

        // Display the target after a random delay
        if (!targetVisible && (std::clock() - startTime) / CLOCKS_PER_SEC > (std::rand() % 3 + 1)) {
            targetVisible = true;
            startTime = std::clock();
        }

        // Draw the target if visible
        if (targetVisible) {
            window.draw(target);
        }

        // Draw the result text
        window.draw(resultText);

        window.display();
    }

    return EXIT_SUCCESS;
}
