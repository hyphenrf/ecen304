import React from 'react';
import { connect } from 'react-redux';
import BookForm from './BookForm';
import { startEditBook, startRemoveBook } from '../redux/Actions/Books';

class AddBook extends React.Component {
    onSubmit = (book) => {
        this.props.startEditBook(this.props.book.firstName, book);
        this.props.history.push('/');
    };
    onRemove = () => {
        this.props.startRemoveBook({ name: this.props.book.name });
        this.props.history.push('/');
    };
    render() {
        return (
            <div>
                <h1>Edit Book</h1>
                <BookForm
                    book={this.props.book}
                    onSubmit={this.onSubmit}
                />
                <button
                    onClick={this.onRemove}
                >
                    Remove
                </button>
            </div>
        )
    }
}

const mapStateToProps = (state, props) => ({
    book: state.books.find((book) => book.firstName === props.match.params.firstName)
});

const mapDispatchToProps = (dispatch) => ({
    startEditBook: (book) => dispatch(startEditBook(book)),
    startRemoveBook: (book) => dispatch(startRemoveBook(book))
});

export default connect(mapStateToProps, mapDispatchToProps)(AddBook);