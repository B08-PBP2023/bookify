const id_book = document.getElementById("id_for_book").value
const filteredUrl = document.getElementById("filtered_url").dataset.url;

// async function getQuestionsAnswers() {
//     return fetch("{% url 'FAQ:get_questions_answers_json' %}").then((res) => res.json())
// }

async function getQuestionsAnswersFiltered(id_book) {
    return fetch(filteredUrl).then((res) => res.json())
}

async function refreshQuestions() {
    document.getElementById('question_answer_cards').innerHTML = ``
    
    const questions_answers = await getQuestionsAnswersFiltered(id_book);

    let htmlString = ``
    htmlString += `\n
    <div class="row m-5">
    `
    questions_answers.forEach((question_answer) => {
        htmlString += `\n
        <div class="col mx-5">
            <div class="card">
                <div class="card-header text-center fw-semibold bg-danger text-white">
                    ${question_answer.fields.isi_pertanyaan}
                </div>
                <div class="card-body text-center">
                    ${question_answer.fields.isi_jawaban}
                </div>
    
                <div class="card-footer d-flex justify-content-center">
                    <a>
                        <button class="form-control btn btn-warning fw-bold" onclick=deleteQuestionAnswer(${question_answer.pk})>
                            Delete
                        </button>
                    </a>
                </div>
            </div>
        </div>
        `
    })
    
    htmlString += `\n
    </div>
    `
    document.getElementById('question_answer_cards').innerHTML = htmlString
}
refreshQuestions()

async function deleteQuestionAnswer(id_question) {
    fetch(`../../delete_question_answer/${id_question}/`, {
        method: "DELETE",
    }).then(refreshQuestions)
    return false
}
