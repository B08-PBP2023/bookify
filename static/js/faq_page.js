const id_book = document.getElementById("id_for_book").value
const filteredUrl = document.getElementById("filtered_url").dataset.url;


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
                </div>
            </div>
            
        
        
        `
    })
    
    htmlString += `\n
    </div>
    `
    document.getElementById('question_answer_cards').innerHTML = htmlString
}

function addQuestion(id_book) {
    fetch(`../../add_question/${id_book}/`, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshQuestions)
    
    document.getElementById("form").reset()
    return false
}

refreshQuestions()