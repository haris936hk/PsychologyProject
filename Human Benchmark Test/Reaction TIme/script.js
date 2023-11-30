document.addEventListener("DOMContentLoaded", function () {
    const target = document.getElementById("target");
    let startTime, endTime;

    function startGame() {
        target.style.backgroundColor = "green";
        startTime = new Date().getTime();
    }

    function endGame() {
        target.style.backgroundColor = "red";
        endTime = new Date().getTime();
        const reactionTime = endTime - startTime;
        alert(`Your reaction time: ${reactionTime} milliseconds`);
        resetGame();
    }

    function resetGame() {
        setTimeout(() => {
            target.style.backgroundColor = "red";
            setTimeout(() => {
                target.style.backgroundColor = "green";
                setTimeout(() => {
                    target.style.backgroundColor = "red";
                }, Math.random() * 2000 + 1000);
            }, Math.random() * 2000 + 1000);
        }, Math.random() * 2000 + 1000);
    }

    target.addEventListener("click", endGame);

    // Start the initial sequence
    resetGame();
});
