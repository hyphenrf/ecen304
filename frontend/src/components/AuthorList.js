import React from 'react';
import { connect } from 'react-redux';

export class AuthorList extends React.Component {
  constructor(props) {
    super(props);
  };

  render() {
    return (
      <div>
        <div>
          <div>Authors</div>
          <div>Author</div>
          <div>Genre</div>
        </div>
        {
          props.authors.length === 0 ? (
            <p>No Authors yet!</p>
          ) : (
              props.authors.map((author) => {
                return (
                  <div>
                    <h3>{author.name}</h3>
                    <h3>{author.genre}</h3>
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
    authors: selectAuthors(state.authors, state.filters)
  };
};

export default connect(mapStateToProps)(AuthorList);
