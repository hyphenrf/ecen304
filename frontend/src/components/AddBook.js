import React from 'react';
import { connect } from 'react-redux';
import BookForm from './BookForm';
import { startAddBook } from '../redux/Actions/Books';

class AddBook extends React.Component {
    onSubmit = (book) => {
        this.props.startAddBook(book);
        this.props.history.push('/');
    };
    render() {
        return (
            <div>
                <h1>Add Book</h1>
                <BookForm
                    onSubmit={this.onSubmit}
                />
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => ({
    startAddBook: (book) => dispatch(startAddBook(book))
});

export default connect(undefined, mapDispatchToProps)(AddBook);