import React from 'react';
import { connect } from 'react-redux';
import AuthorForm from './AuthorForm';
import { startAddAuthor } from '../redux/Actions/Authors';

class AddAuthor extends React.Component {
    onSubmit = (author) => {
        this.props.startAddAuthor(author);
        this.props.history.push('/');
    };
    render() {
        return (
            <div>
                <h1>Add Author</h1>
                <AuthorForm
                    onSubmit={this.onSubmit}
                />
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch) => ({
    startAddAuthor: (author) => dispatch(startAddAuthor(author))
});

export default connect(undefined, mapDispatchToProps)(AddAuthor);