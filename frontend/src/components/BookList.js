import React from 'react';
import { connect } from 'react-redux';

export class BookList extends React.Component {
  constructor(props) {
    super(props);
  };

  render() {
    return (
      <div>
        <div>
          <div>Books</div>
          <div>Book</div>
        </div>
        {
          props.books.length === 0 ? (
            <p>No Books yet!</p>
          ) : (
              props.books.map((book) => {
                return (
                  <div>
                    <h3>{book.Uname}</h3>
                    <h3>{book.description}</h3>
                  </div>
                )
              })
            )
        }
      </div>
    )
  };
};

const mapStateToProps = (state) => {
  return {
    books: selectUsers(state.books, state.filters)
  };
};

export default connect(mapStateToProps)(BookList);
