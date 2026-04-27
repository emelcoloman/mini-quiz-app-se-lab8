let loadedQuestions = [];

async function loadQuiz() {

    const response = await fetch('/questions');
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
                <input type="text" name="q${index}">
            `;
        }

        card.innerHTML = html;
        container.appendChild(card);
    });

    document.getElementById('submit-btn').style.display = 'inline-block';
}