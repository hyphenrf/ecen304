// Authors Reducer

const authorsReducerDefaultState = [];

export default (state = authorsReducerDefaultState, action) => {
    switch (action.type) {
        case 'ADD_AUTHOR':
            return [
                ...state,
                action.author
            ];
        case 'REMOVE_AUTHOR':
            return state.filter(({ id }) => id !== action.id);
        case 'EDIT_AUTHOR':
            return state.map((author) => {
                if (author.id === action.id) {
                    return {
                        ...author,
                        ...action.updates
                    };
                } else {
                    return author;
                };
            });
        default:
            return state;
    }
};
