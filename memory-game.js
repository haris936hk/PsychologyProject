document.addEventListener('DOMContentLoaded', function () {
    const memoryGame = document.getElementById('memoryGame');
    const cardValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];

    let firstCard = null;
    let secondCard = null;
    let lockBoard = false;

    // Shuffle the cards
    const shuffledCards = shuffle([...cardValues, ...cardValues]);

    // Create card elements and add them to the memory game board
    shuffledCards.forEach(value => {
        const card = document.createElement('div');
        card.className = 'card';
        card.dataset.value = value;
        card.addEventListener('click', flipCard);
        memoryGame.appendChild(card);
    });

    function flipCard() {
        if (lockBoard) return;
        if (this === firstCard) return;

        this.classList.add('flip');

        if (!firstCard) {
            firstCard = this;
            return;
        }

        secondCard = this;
        checkForMatch();
    }

    function checkForMatch() {
        const isMatch = firstCard.dataset.value === secondCard.dataset.value;

        isMatch ? disableCards() : unflipCards();
    }

    function disableCards() {
        firstCard.removeEventListener('click', flipCard);
        secondCard.removeEventListener('click', flipCard);

        resetBoard();
    }

    function unflipCards() {
        lockBoard = true;

        setTimeout(() => {
            firstCard.classList.remove('flip');
            secondCard.classList.remove('flip');

            resetBoard();
        }, 1000);
    }

    function resetBoard() {
        [firstCard, secondCard] = [null, null];
        lockBoard = false;
    }

    function shuffle(array) {
        let currentIndex = array.length, randomIndex;

        while (currentIndex !== 0) {
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;

            [array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
        }

        return array;
    }
});
