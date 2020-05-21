// ADD_BOOK
export const addBook = (book) => ({
    type: 'ADD_BOOK',
    book
});

export const startAddBook = (bookData = {}) => {
    return (dispatch, getState) => {
        const {
            id = 0,
            name = '',
            author = '',
            type = '',
            genre = '',
            description = '',
            ISBN = 0,
            edition = 1,
            price = 0,
            NumOfAvailableCopies = 0,
            NumOfPages = 0,
            dateOfPublication = 0,
            pictures = []
        } = bookData;
        
        const book = {
            name, author, type, genre, description,
            ISBN, edition, price, NumOfAvailableCopies,
            NumOfPages, dateOfPublication,
            pictures
        };

        dispatch(addBook({
            ...book
        }))

        // SEND TO BACKEND
    };
};

// REMOVE_BOOK
export const removeBook = ({ id } = {}) => ({
    type: 'REMOVE_BOOK',
    id
});

export const startRemoveBook = ({ id } = {}) => {
    return (dispatch, getState) => {

        dispatch(removeBook({ id }));
        // SEND TO BACKEND
    }
};

// EDIT_BOOK
export const editBook = (id, updates) => ({
    type: 'EDIT_BOOK',
    id,
    updates
});

export const startEditBook = (id, updates) => {
    return (dispatch, getState) => {

        dispatch(editBook({
            id,
            updates
        }));
        // SEND TO BACKEND
    }
};

