// ADD_USER
export const addUser = (user) => ({
  type: 'ADD_USER',
  user
});

export const startAddUser = (userData = {}) => {
  return (dispatch, getState) => {
    const {
      name = '',
      email = '',
      dateOfBirth = 0,
      listOfBooks = [],
      Genre = [],
      borrowedBooks = [],
      boughtBooks = [],
      pendingBooks = [],
      ratedBooks = [],
      paymentMethod = '',
      savings = 0,
      address = {},
      password = ''
    } = userData;
    const user = {
      name, email, dateOfBirth,
      listOfBooks, Genre, borrowedBooks,
      boughtBooks, pendingBooks, ratedBooks,
      paymentMethod, savings, address, password,
    };

    // SEND TO BACKEND
    dispatch(addUser({
      ...user
    }));
  };
};

// REMOVE_USER
export const removeUser = ({ id } = {}) => ({
  type: 'REMOVE_USER',
  id
});

export const startRemoveUser = ({ id } = {}) => {
  return (dispatch, getState) => {

    // SEND TO BACKEND
    dispatch(removeUser({
      id
    }));
  }
};

// EDIT_USER
export const editUser = (id, updates) => ({
  type: 'EDIT_USER',
  id,
  updates
});

export const startEditUser = (id, updates) => {
  return (dispatch, getState) => {

    // SEND TO BACKEND
    dispatch(editUser({
      id,
      updates
    }));
  }
};



