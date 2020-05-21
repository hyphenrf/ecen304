// ADD_AUTHOR
export const addAuthor = (author) => ({
    type: 'ADD_AUTHOR',
    author
});

export const startAddAuthor = (authorData = {}) => {
    return (dispatch, getState) => {
        const {
            id = 0,
            name = '',
            dateOfBirth = 0,
            listOfBooks = [],
            Genre = [],
        } = authorData;
        const author = {
            name, dateOfBirth, listOfBooks, Genre, id
        };

        // SEND TO BACKEND
        dispatch(addAuthor({
            ...author
        }));
    };
};

// REMOVE_AUTHOR
export const removeAuthor = ({ id } = {}) => ({
    type: 'REMOVE_AUTHOR',
    id
});

export const startRemoveAuthor = ({ id } = {}) => {
    return (dispatch, getState) => {

        // SEND TO BACKEND
        dispatch(removeAuthor({
            id
        }));
    }
};

// EDIT_AUTHOR
export const editAuthor = (id, updates) => ({
    type: 'EDIT_AUTHOR',
    id,
    updates
});

export const startEditAuthor = (id, updates) => {
    return (dispatch, getState) => {

        // SEND TO BACKEND
        dispatch(editAuthor({
            id,
            updates
        }));
    }
};