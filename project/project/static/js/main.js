    let booksArray = [];
    let userArray = [];
   booksArray = JSON.parse(('{{books|escapejs}}'));
    //userArray = JSON.parse(('{{ users|escapejs }}'));
   
   

    function populateBooks() {
    const columns = document.querySelectorAll('.book-details');
 
    columns.forEach((column, index) => {
        if (index >=booksArray.length) {
          column.parentElement.style.display ='none' ;
        } else {
          const book = booksArray[index];
          
          column.innerHTML = `
                  <p class="ID">Book ID: ${book.id}</p>
                  <div><a href="bookDetails.html?bookid=${book.id} ${userId}"><img src="${book.img}" height="280px"></a></div>
                  <p>${book.price}$</p>
                  <button onclic="add()">Borrow</button>
                    </a>
                    `;
                  }
                });

               
      }
   
              
             
              populateBooks();
    
              
         
      function displayBooks(searchResults) {
      const columns = document.querySelectorAll('.book-details');
      columns.forEach((column, index) => {
        if (index >= searchResults.length) {
         
          column.parentElement.style.display = 'none';
        } else {
          const book = searchResults[index];
          column.innerHTML = `
                    <p class="ID">Book ID: ${book.id}</p>
                    <div><a href="bookDetails.html?bookid=${book.id} "><img src="${book.img}" height="280px"></a></div>
                    <p>${book.price}$</p>
                      <button onclic="add()">Borrow</button>
                      </a>
                      `;
                    }
      });

      
    }

    function searchBooks() {
      const item = document.getElementById('searchInput').value.toLowerCase();
      const result = booksArray.filter(book =>
        book.title.toLowerCase().includes(item.toLowerCase()) || book.author.toLowerCase().includes(item.toLowerCase()) || book.catogry.toLowerCase().includes(item.toLowerCase())
      );

      if (result.length > 0) {
        displayBooks(result);
      } else {
        const contentDiv = document.getElementById('content');
        contentDiv.innerHTML = '<h2>No results found.</h2>';
      }
    }
