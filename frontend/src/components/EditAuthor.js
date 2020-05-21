import React from 'react';
import { connect } from 'react-redux';
import AuthorForm from './AuthorForm';
import { startEditAuthor, startRemoveAuthor } from '../redux/Actions/Authors';

class AddAuthor extends React.Component {
    onSubmit = (author) => {
        this.props.startEditAuthor(this.props.author.firstName, author);
        this.props.history.push('/');
    };
    onRemove = () => {
        this.props.startRemoveAuthor({ firstName: this.props.author.firstName });
        this.props.history.push('/');
    };
    render() {
        return (
            <div>
                <h1>Edit Author</h1>
                <AuthorForm
                    author={this.props.author}
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
    author: state.authors.find((author) => author.firstName === props.match.params.firstName)
});

const mapDispatchToProps = (dispatch) => ({
    startEditAuthor: (author) => dispatch(startEditAuthor(author)),
    startRemoveAuthor: (author) => dispatch(startRemoveAuthor(author))
});

export default connect(mapStateToProps, mapDispatchToProps)(AddAuthor);