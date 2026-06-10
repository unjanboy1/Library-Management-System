const bookForm = document.getElementById("bookForm");

if(bookForm){

    bookForm.addEventListener("submit", async(e)=>{

        e.preventDefault();

        const title =
            document.getElementById("title").value;

        const author =
            document.getElementById("author").value;

        const category =
            document.getElementById("category").value;

        const quantity =
            document.getElementById("quantity").value;

        const response = await fetch(
            "http://127.0.0.1:5000/books",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify({
                    title,
                    author,
                    category,
                    quantity
                })
            }
        );

        const data = await response.json();

        alert(data.message);

        loadBooks();
    });

}

async function loadBooks(){

    const response =
        await fetch(
            "http://127.0.0.1:5000/books"
        );

    const books =
        await response.json();

    const table =
        document.getElementById(
            "booksTable"
        );

    if(!table) return;

    table.innerHTML = "";

    books.forEach(book=>{

        table.innerHTML += `
        <tr>
            <td>${book.id}</td>
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.category}</td>
            <td>${book.quantity}</td>
        </tr>
        `;
    });

}

loadBooks();