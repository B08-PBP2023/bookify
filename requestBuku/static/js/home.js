async function getBooks() {
    return fetch(`get_books`).then((res) => res.json())
}

async function refreshBooks() {
    document.getElementById('book_cards').innerHTML = ``
    
    const books = await getBooks();
    const searchInput = document.getElementById("filter_judul").value

    let filteredBooks = books.filter(book => {
        return book.fields.title.toLowerCase().includes(searchInput.toLowerCase());
        
    });
    
    console.log(searchInput)


    let htmlString = ``
    htmlString += `\n
    <div class="row row-cols-1 row-cols-md-3 g-4 py-3 justify-content-center">
    `
    filteredBooks.forEach((book) => {
        htmlString += `\n
        <div class="col mx-5">
            <div class="card">
                <div class="card-header text-center fw-semibold bg-success text-white">
                    Buku ${book.pk}
                </div>
                <div class="card-body text-center">
                    <strong>Judul</strong>: ${book.fields.title} <br>
                    <strong>Penulis</strong>: ${book.fields.authors} <br>
                    <strong>Bahasa</strong>: ${book.fields.language_code} <br>
                    <strong>Jumlah Halaman</strong>: ${book.fields.num_pages} <br>
                    <strong>Tanggal Publikasi</strong>: ${book.fields.publication_date} <br>
                    <strong>Penerbit</strong>: ${book.fields.publisher} <br>
                </div>
                <a href="delete/${book.pk}">
                    <button class="form-control btn btn-danger fw-bold">
                        - Delete
                    </button>
                </a>
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