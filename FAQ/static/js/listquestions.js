const id_book = document.getElementById("id_for_book").value
const filteredUrl = document.getElementById("filtered_url").dataset.url;

async function getQuestions() {
    return fetch("{% url 'FAQ:get_questions_json' %}").then((res) => res.json())
}

async function getQuestionsFiltered(id_book) {
    return fetch(filteredUrl).then((res) => res.json())
}

async function getQuestionsById(id_question) {
    return fetch(`/FAQ/get_questions_by_id_json/${id_question}/`).then((res) => res.json())
}

async function refreshQuestions() {
    document.getElementById('question_cards').innerHTML = ``
    
    const questions = await getQuestionsFiltered(id_book);

    let htmlString = ``
    htmlString += `\n
    <div class="row m-5">
    `


    questions.forEach((question) => {
        htmlString += `\n
        <div class="col mx-5">
            <div class="card">
                <div class="card-header text-center fw-semibold bg-secondary text-white">
                    Pertanyaan
                </div>
                <div class="card-body text-center">
                    ${question.fields.isi_pertanyaan}
                </div>
                <div class="card-footer d-flex justify-content-between">

                    <a>
                        <button type="button" class="form-control btn btn-primary fw-bold" data-bs-toggle="modal" data-bs-target="#jawabanModal" onclick=setValueQuestion(${question.pk})>
                            Jawab
                        </button>
            
                    </a>

                    <a>
                        <button class="form-control btn btn-primary fw-bold" onclick=deleteQuestion(${question.pk})>
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

    document.getElementById('question_cards').innerHTML = htmlString
}
refreshQuestions()

async function setValueQuestion(id_question){
    let isi_pertanyaan_temp = await getQuestionsById(id_question)
    isi_pertanyaan_temp = isi_pertanyaan_temp[0].fields.isi_pertanyaan

    document.getElementById("isi_pertanyaan").value = isi_pertanyaan_temp
    document.getElementById("button_add_jawaban").onclick = function() {
        jawabQuestion(id_question);
    };
}

async function deleteQuestion(id_question) {
    fetch(`../../delete_question/${id_question}/`, {    
        method: "DELETE",
    }).then(refreshQuestions)
    return false
}

async function jawabQuestion(id_question) {
    fetch(`../../jawab_question/${id_book}/`, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshQuestions)

    document.getElementById("form").reset()

    fetch(`../../delete_question/${id_question}/`, {
        method: "DELETE",
    }).then(refreshQuestions)

    return false
}
// document.getElementById("button_add_jawaban").onclick = jawabQuestion