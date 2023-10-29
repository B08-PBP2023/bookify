async function getUsers() {
    return fetch(`../get_user/`).then((res) => res.json())
    
}

async function getUserWithRoleByName() {
    return fetch(`../get_user_with_role_by_name/`).then((res) => res.json())
}

async function refreshBooks() {
    document.getElementById('book_cards').innerHTML = ``
    
    const books = await getUsers();
    
    let htmlString = ``
    htmlString += `\n
    <div class="row row-cols-1 row-cols-md-3 g-4 py-3 justify-content-center">
    `
    let count=0;
    books.forEach((book) => {
        console.log(book)
        name = book.fields.name
        role = book.fields.role
        count++;
        htmlString += `\n
        <div class="col mx-5">
            <div class="card">
                <div class="card-header text-center fw-semibold bg-info text-white">
                    User ${count}
                </div>
                <div class="card-body text-center">
                    <strong>Name</strong>: ${name} <br>
                    <strong>Role</strong>: ${role} <br>
                </div>
            </div>
        </div>
        `
    })
    
    htmlString += `\n
    </div>
    `
    document.getElementById('book_cards').innerHTML = htmlString
}


refreshBooks()