let loadedQuestions = [];

async function loadQuiz() {

    try {

        const response = await fetch('/questions');

        if (!response.ok) {
            throw new Error('Failed to load questions');
        }

        loadedQuestions = await response.json();

        const container = document.getElementById('quiz');
        container.innerHTML = '';

        loadedQuestions.forEach((question, index) => {

            const card = document.createElement('div');
            card.className = 'question-card';

            let html = `<h3>${index + 1}. ${question.prompt}</h3>`;

            if (question.type === 'multiple_choice') {

                question.options.forEach(option => {

                    html += `
                        <label class="option">
                            <input type="radio" name="q${index}" value="${option}">
                            ${option}
                        </label>
                    `;
                });
            }

            else if (question.type === 'true_false') {

                html += `
                    <label class="option">
                        <input type="radio" name="q${index}" value="true">
                        True
                    </label>

                    <label class="option">
                        <input type="radio" name="q${index}" value="false">
                        False
                    </label>
                `;
            }

            else if (question.type === 'short_answer') {

                html += `
                    <input type="text" name="q${index}" placeholder="Type your answer">
                `;
            }

            card.innerHTML = html;
            container.appendChild(card);
        });

        document.getElementById('submit-btn').style.display = 'inline-block';

    } catch (error) {

        console.error(error);

        document.getElementById('quiz').innerHTML = `
            <p>Failed to load quiz questions.</p>
        `;
    }
}

document.addEventListener('DOMContentLoaded', function () {

    const form = document.getElementById('quiz-form');

    form.addEventListener('submit', function(e) {

        e.preventDefault();

        let score = 0;

        loadedQuestions.forEach((question, index) => {

            let userAnswer = "";

            const selectedRadio = document.querySelector(`input[name="q${index}"]:checked`);
            const textInput = document.querySelector(`input[name="q${index}"][type="text"]`);

            if (selectedRadio) {
                userAnswer = selectedRadio.value;
            }

            else if (textInput) {
                userAnswer = textInput.value;
            }

            if (
                userAnswer.trim().toLowerCase() ===
                question.answer.trim().toLowerCase()
            ) {
                score++;
            }
        });

        const percentage = ((score / loadedQuestions.length) * 100).toFixed(2);

        document.getElementById('result').innerHTML = `
            <h2>Quiz Results</h2>
            <p>Score: ${score}/${loadedQuestions.length}</p>
            <p>Percentage: ${percentage}%</p>
        `;
    });
});